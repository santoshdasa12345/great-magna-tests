# -*- coding: utf-8 -*-
"""Then step implementations."""
import logging
from collections import defaultdict
from inspect import signature
from typing import List, Union
from urllib.parse import urlparse
import time
import requests
from behave.model import Table
from behave.runner import Context
from datadiff import diff
from retrying import retry
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By

from great_magna_tests_shared.utils import blue, check_for_errors, get_comparison_details
from great_magna_tests_shared.clients import (
    BASIC_AUTHENTICATOR,
    DIRECTORY_TEST_API_CLIENT,
)
from great_magna_tests_shared.constants import (
    EMAIL_ERP_PROGRESS_SAVED_MSG_SUBJECT,
    FORMS_API_MAILBOXES,
    HPO_AGENT_EMAIL_ADDRESS,
    HPO_AGENT_EMAIL_SUBJECT,
    HPO_ENQUIRY_CONFIRMATION_SUBJECT,
    HPO_PDF_URLS,
)
from great_magna_tests_shared.gov_notify import (
    get_email_confirmation_notification,
    get_email_confirmations_with_matching_string,
    get_verification_link,
)
from great_magna_tests_shared.pdf import extract_text_from_pdf
from browserpages import (
    common_language_selector,
    domestic,
    # erp,
    fas,
    get_page_object,
    invest,
    profile,
)
from browserpages.common_actions import (
    accept_all_cookies,
    assertion_msg,
    avoid_browser_stack_idle_timeout_exception,
    get_actor,
    get_full_page_name,
    get_last_visited_page,
    revisit_page_on_access_denied,
    selenium_action,
    take_screenshot,
    update_actor,
)
from browserpages.domestic import contact_us_office_finder_search_results
from steps import has_action
from browserutils.browser import clear_driver_cookies
from browserutils.forms_api import (
    find_form_submissions,
    find_form_submissions_by_subject_and_action,
    find_form_submissions_for_dit_office,
)
from browserutils.gtm import (
    get_gtm_data_layer_events,
    get_gtm_data_layer_properties,
    replace_string_representations,
)

def should_be_on_page(context: Context, actor_alias: str, page_name: str):
    page = get_page_object(page_name)
    page_source = context.driver.page_source
    # revisit_page_on_access_denied(context.driver, page, page_name)
    take_screenshot(context.driver, f"should be on {page_name}")
    check_for_errors(page_source, context.driver.current_url)
    accept_all_cookies(context.driver)
    has_action(page, "should_be_here")
    if hasattr(page, "SubURLs"):
        special_page_name = page_name.split(" - ")[1].lower()
        if signature(page.should_be_here).parameters.get("page_name"):
            page.should_be_here(context.driver, page_name=special_page_name)
        else:
            raise TypeError(
                f"{page.__name__}.should_be_here() doesn't accept 'page_name' keyword "
                f"argument but it should as this Page Object has 'SubURLs' attribute."
            )
    else:
        page.should_be_here(context.driver)
    update_actor(context, actor_alias, visited_page=page)
    logging.debug(
        f"{actor_alias} is on {page.SERVICE} - {page.NAME} - {page.TYPE} -> " f"{page}"
    )


def should_be_able_to_see_error_message(context, actor_alias, element_name, expected_error_message):
    default_page = "GreatMagna - Login"
    page = get_page_object(default_page)
    has_action(page, "should_be_error_message")
    if page.should_be_error_message(context.driver, element_name, expected_error_message) == False:
        error = f"Error message not found on the page {page.NAME}"
        assert False, error


def actor_decides_to_check_random_radio_and_click_on_continue(
        context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "find_and_select_random_radio_and_click_continue")
    page.find_and_select_random_radio_and_click_continue(context.driver)


def actor_decides_to_click_country_name_change(
        context, actor_alias, element_name):
    page = get_page_object("ImportTariff - CheckYourAnswers")
    has_action(page, "find_and_click_change_link")
    page.find_and_click_change_link(context.driver, "country_name_change")


def actor_decides_to_click_product_search_change(
        context, actor_alias, element_name):
    page = get_page_object("ImportTariff - CheckYourAnswers")
    has_action(page, "find_and_click_change_link")
    current_url = context.driver.current_url
    if "look-up" in current_url:
        page.find_and_click_change_link(context.driver, "lookup_product_search_change")
    else:
        page.find_and_click_change_link(context.driver, "product_search_change")


def actor_decides_to_click_refine_interaction_change(
        context, actor_alias, element_name):
    page = get_page_object("ImportTariff - CheckYourAnswers")
    has_action(page, "find_elements_and_click_change_link")
    page.find_elements_and_click_change_link(context.driver, "refine")


def actor_decides_to_click_trade_data_change(
        context, actor_alias, element_name):
    page = get_page_object("ImportTariff - CheckYourAnswers")
    has_action(page, "find_elements_and_click_change_link")
    page.find_elements_and_click_change_link(context.driver, "tradedata")


def actor_decides_to_click_proceed(
        context, actor_alias, element_name):
    page = get_page_object("ImportTariff - CheckYourAnswers")
    has_action(page, "find_and_click_change_link")
    page.find_and_click_change_link(context.driver, "submit")


def actor_should_be_able_to_see_comodity_code(
        context, actor_alias, code, product):
    page = get_page_object("ImportTariff - Confirmation Code")
    has_action(page, "find_and_select_comodity_code")
    if page.find_and_select_comodity_code(context.driver, code, product) == False:
        error = f"Couldn't find Comodity code on the Confirmation page"
        assert False, error


def actor_clicked_on_start_again(
        context, actor_alias, keyword_to_click):
    page = get_page_object("ImportTariff - Confirmation Code")
    has_action(page, "find_and_click_start_again")
    page.find_and_click_start_again(context.driver, keyword_to_click)


def should_see_following_sections(context: Context, actor_alias: str, sections_table: Table = None, *,
                                  sections_list: list = None, ):
    sections = sections_list or [row[0] for row in sections_table]
    logging.debug(
        "%s will look for following sections: '%s' on %s",
        actor_alias,
        sections,
        context.driver.current_url,
    )
    page = get_last_visited_page(context, actor_alias)
    # page = get_page_object("GreatMagna - Dashboard")
    has_action(page, "should_see_following_sections")
    page.should_see_following_sections(context.driver, sections)


def actor_should_be_able_to_see_confirmation_code_page_from_email_password_and_enter_code(context: Context
                                                                                          , email_address: str,
                                                                                          password: str):
    page = get_page_object("GreatMagna - Sign Up")
    has_action(page, "confirmation_code")
    page.confirmation_code(context.driver, email_address, password)


def actor_decides_to_enter_email_address_and_click_on_reset_password(context: Context, email_address: str):
    page = get_page_object("GreatMagna - forgotten password")
    has_action(page, "fill_out_email_address")
    details_dict = {"emailaddress": email_address}
    page.fill_out_email_address(context.driver, details_dict)


def actor_should_be_able_to_click_on_reset_password_link_from_email_password_and_enters_new_password_and_confirm(
        context: Context, actor_alias: str, email_address: str, password: str, new_password: str):
    page = get_page_object("GreatMagna - forgotten password")
    has_action(page, "read_reset_password_email")
    page.read_reset_password_email(context.driver, email_address, password, new_password)


def actor_should_be_able_to_enter_products_and_country(context, products, country):
    page = get_page_object("GreatMagna - Dashboard")
    has_action(page, "fill_out_products_and_country")
    page.fill_out_products_and_country(context.driver, products, country)


def actor_should_be_able_to_enter_products(context, products):
    page = get_page_object("GreatMagna - Dashboard")
    has_action(page, "fill_out_products")
    page.fill_out_products(context.driver, products)


def actor_decides_to_click_checkbox_yes_for_lesson_complete(context, page_name: str):
    page = get_page_object(page_name)
    has_action(page, "check_lesson_complete_yes")
    page.check_lesson_complete_yes(context.driver, "lesson yes checkbox")


def actor_decides_to_click_checkbox_section_complete(context, page_name: str):
    page = get_page_object(page_name)
    has_action(page, "check_section_complete_yes")
    page.check_section_complete_yes(context.driver, "yes checkbox")


# def actor_decides_to_click_on_bottom_back(context: Context, actor_alias: str,element_name : str):
#     page = get_page_object("LearnToExport - Introduction to Lessons and Learning Page")
#     has_action(page, "bottom_back")
#     page.bottom_back(context.driver,element_name)


def actor_decides_to_click_continue_for_number_of_times_until_it_reaches_required_page(
        context, actor_alias, max_number_pages, from_page_name, to_page_name):
    counter = 0
    while counter < int(max_number_pages):
        page = get_page_object(from_page_name)
        logging.debug("visiting page  - "+ page.NAME)
        has_action(page, "find_and_click")
        page.find_and_click(context.driver, element_selector_name="continue learning")
        time.sleep(1)
        current_page_url = str(context.driver.current_url)
        logging.debug("Last visited page - " + current_page_url)
        logging.debug("to_page_name - " + to_page_name)
        counter += 1
        if to_page_name in current_page_url:
            break


def actor_decides_to_click_open_case_study_in_all_lessons_for_number_of_times_until_it_reaches_required_page(
        context, actor_alias, max_number_pages, from_page_name, to_page_name, element_name):
    counter = 0
    while counter < int(max_number_pages):
        page = get_page_object(from_page_name)
        # logging.debug("visiting page  - "+ page.NAME)
        has_action(page, "find_and_click")
        page.find_and_click_case_study(context.driver, element_selector_name="open case study")
        current_page_url = str(context.driver.current_url)
        # logging.debug("Last visited page - "+current_page_url)
        # time.sleep(1)
        counter += 1
        if to_page_name in current_page_url:
            break


def actor_should_be_able_to_see_progress_bar_for_section(context, actor_alias, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "find_progress_bar")
    page.find_progress_bar(context.driver, element_name)


def actor_decides_to_enter_text(context, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_text")
    page.enter_text(context.driver, element_name)


def actor_decides_to_validate_entered_text(context, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "validate_entered_text")
    if False == page.validate_entered_text(context.driver, element_name):
        error = f"Randomly entered text not found in the text input area on the page {page.NAME}"
        assert False, error


def actor_decides_to_select_random_item_list_on_page(context, actor_alias, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "find_and_select_random_item_list")
    page.find_and_select_random_item_list(context.driver, element_name)

def actor_decides_to_select_random_payment_terms_on_page(context, actor_alias, page_name):
    page = get_page_object(page_name)
    has_action(page, "find_and_select_random_payment_terms")
    page.find_and_select_random_payment_terms(context.driver)

def actor_decides_to_select_random_unit_list_on_page(context, actor_alias, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "find_and_select_random_unit_list")
    page.find_and_select_random_unit_list(context.driver, element_name)

def actor_decides_to_select_random_time_from_list_on_page(context, actor_alias, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "find_and_select_random_time_list")
    page.find_and_select_random_time_list(context.driver, element_name)

def actor_decides_to_select_random_currency_from_list_on_page(context, actor_alias, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "find_and_select_random_currency_list")
    page.find_and_select_random_currency_list(context.driver, element_name)

def actor_fill_business_objectives_details_on_page(context, actor_alias, position,objectives,
                                                   owner, plannedreviews, page_name,element_name):
    page = get_page_object(page_name)
    has_action(page, "enter_business_objectives_details")
    page.enter_business_objectives_details(context.driver, position,objectives, owner,
                                           plannedreviews,element_name)


def actor_decides_to_delete_business_objectives_on_page(context, actor_alias, position, page_name):
    page = get_page_object(page_name)
    has_action(page, "delete_all_business_objectives")
    page.delete_all_business_objectives(context.driver, position)


def actor_decides_to_delete_risk_details_on_page(context, actor_alias, position, page_name):
    page = get_page_object(page_name)
    has_action(page, "delete_all_risk_details")
    page.delete_all_risk_details(context.driver, position)


def actor_fill_risk_details_on_page(context, actor_alias, position, risktext, contingencyplan, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_risk_details")
    page.enter_risk_details(context.driver, position, risktext, contingencyplan)


def actor_decides_to_delete_country_details_on_page(context, actor_alias, position, page_name):
    page = get_page_object(page_name)
    has_action(page, "delete_all_country_details")
    page.delete_all_country_details(context.driver, position)


def actor_decides_to_delete_route_to_market_on_page(context, actor_alias, position, page_name):
    page = get_page_object(page_name)
    has_action(page, "delete_all_route_to_market")
    page.delete_all_route_to_market(context.driver, position)


def actor_decides_to_delete_funding_options_on_page(context, actor_alias, position, page_name):
    page = get_page_object(page_name)
    has_action(page, "delete_all_funding_options")
    page.delete_all_funding_options(context.driver, position)


def should_see_sections(
        context: Context,
        actor_alias: str,
        sections_table: Table = None,
        *,
        sections_list: list = None,
):
    sections = sections_list or [row[0] for row in sections_table]
    logging.debug(
        "%s will look for following sections: '%s' on %s",
        actor_alias,
        sections,
        context.driver.current_url,
    )
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "should_see_sections")
    page.should_see_sections(context.driver, sections)


def actor_decides_to_select_random_checkbox_on_page(context, actor_alias, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "random_select_checkbox")
    page.random_select_checkbox(context.driver, element_name)


def actor_decides_to_enter_value(context, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_value")
    page.enter_value(context.driver, element_name)


def actor_fill_document_details_on_page(context, actor_alias, position, documentname, notes, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_document_details")
    page.enter_document_details(context.driver, position, documentname, notes)


def actor_decides_to_delete_document_details_on_page(context, actor_alias, position, page_name):
    page = get_page_object(page_name)
    has_action(page, "delete_all_document_details")
    page.delete_all_document_details(context.driver, position)


def actor_enters_direct_costs_on_page(context, actor_alias, productcost, labourcost, additionalmargin, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_direct_costs")
    page.enter_direct_costs(context.driver, productcost, labourcost, additionalmargin)


def actor_enters_overhead_costs_on_page(context, actor_alias, productadaptation, freightandlogistics,
                                        agentanddistributionfees, marketing, finance, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_overhead_costs")
    page.enter_overhead_costs(context.driver, productadaptation, freightandlogistics, agentanddistributionfees,
                              marketing, finance)


def actor_decides_to_select_funding_options_on_page(context, actor_alias, position, amount, page_name):
    page = get_page_object(page_name)
    has_action(page, "find_and_select_random_funding_options")
    page.find_and_select_random_funding_options(context.driver, position, amount)


def actor_decides_to_enter_product_name(context, actor_alias, product_name, page_name):
    logging.debug(f"Page name = {page_name}")
    page = get_page_object(page_name)
    logging.debug(f"Page name = {page.NAME}")
    has_action(page, "fill_out_product")
    page.fill_out_product(context.driver, product_name)


def actor_decides_to_enter_country_name(context, actor_alias, country_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "fill_out_country")
    page.fill_out_country(context.driver, country=country_name)


def actor_should_be_able_to_click_on_skipwalkthrough(
        context, actor_alias):
    # time.sleep(5)
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_skip_walk_through")
    # has_action(page, "click_avatar")
    page.click_skip_walk_through(context.driver)
    # page.click_avatar(context.driver)


def actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months(
        context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_on_i_have_exported_in_the_last_12_months")
    page.click_on_i_have_exported_in_the_last_12_months(context.driver)


def actor_decides_to_click_on_search_again(context, actor_alias, page_name):
    page = get_page_object(page_name)
    has_action(page, "search_again_top_bottom")
    page.search_again_top_bottom(context.driver)


def actor_decides_to_click_on_product_and_search_again(context, actor_alias, product_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "select_product_search_again_top_bottom")
    page.select_product_search_again_top_bottom(context.driver, product_name)


def actor_decides_to_click_on_select_save_random_products(context, actor_alias, page_name):
    page = get_page_object(page_name)
    has_action(page, "search_select_save_random_next")
    page.search_select_save_random_next(context.driver)


def actor_fill_trip_details_on_page(context, actor_alias, position, tripname, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_trip_details")
    page.enter_trip_details(context.driver, position, tripname)


def actor_decides_to_delete_trip_details_on_page(context, actor_alias, position, page_name):
    page = get_page_object(page_name)
    has_action(page, "delete_all_trip_details")
    page.delete_all_trip_details(context.driver, position)


def actor_decides_to_select_radio_button(context, element_name, page_name):
    page = get_page_object(page_name)
    has_action(page, "select_radio_button")
    page.select_radio_button(context.driver, element_name=element_name)


def actor_decides_to_enter_country_details(context, actor_alias, countryname, country_place_number, country_max
                                           , display_tab_count, page_name):
    page = get_page_object(page_name)
    has_action(page, "enter_country_details")
    page.enter_country_details(context.driver, countryname
                               , country_place_number=int(country_place_number)
                               , country_max=int(country_max)
                               , display_tab_count=int(display_tab_count))


def generic_fill_out_and_submit_form(
        context: Context,
        actor_alias: str,
        *,
        custom_details_table: Table = None,
        retry_on_errors: bool = False,
        go_back: bool = False,
        form_name: str = None,
        check_captcha_dev_mode: bool = True,
):
    if check_captcha_dev_mode:
        assert_catcha_in_dev_mode(context.driver)
    actor = get_actor(context, actor_alias)
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "generate_form_details")
    has_action(page, "fill_out")
    has_action(page, "submit")
    if form_name:
        error = f"generate_form_details() in {page} should accept 'form_name' but it doesn't"
        assert signature(page.generate_form_details).parameters.get("form_name"), error
        error = f"fill_out() in {page} should accept 'form_name' but it doesn't"
        assert signature(page.fill_out).parameters.get("form_name"), error
        error = f"submit() in {page} should accept 'form_name' but it doesn't"
        assert signature(page.submit).parameters.get("form_name"), error
    if custom_details_table:
        custom_details_table.require_column("field")
        custom_details_table.require_column("value")
        value_mapping = {"unchecked": False, "checked": True, "empty": None}
        custom_details = {}
        for row in custom_details_table.rows:
            key = row["field"].lower()
            value = row["value"]
            custom_details[key] = value_mapping.get(value, value)
        if form_name:
            details = page.generate_form_details(
                actor, custom_details=custom_details, form_name=form_name
            )
        else:
            details = page.generate_form_details(actor, custom_details=custom_details)
    else:
        if form_name:
            details = page.generate_form_details(actor, form_name=form_name)
        else:
            details = page.generate_form_details(actor)
    logging.debug(f"{actor_alias} will fill out the form with: {details}")

    update_actor_forms_data(context, actor, details)

    if form_name:
        page.fill_out(context.driver, details, form_name=form_name)
    else:
        page.fill_out(context.driver, details)

    if hasattr(page, "get_form_details"):
        logging.debug(f"Getting form details from filled out form: {page}")
        form_data = page.get_form_details(context.driver)
        if form_data:
            update_actor_forms_data(context, actor, form_data)
    else:
        if details:
            update_actor_forms_data(context, actor, details)

    if form_name:
        page.submit(context.driver, form_name=form_name)
    else:
        page.submit(context.driver)
    # if retry_on_errors:
    #     check_for_errors_or_non_trading_companies(context.driver, go_back=go_back)


def generic_submit_form(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "submit")
    page.submit(context.driver)


def actor_should_see_country_details_on_page(context, actor_alias, page_name, on_all_tabs: bool = False):
    page = get_page_object(page_name)
    has_action(page, "check_country_details")
    page.check_country_details(context.driver, on_all_tabs=on_all_tabs)


def actor_should_see_last_visited_page_under_section_on_page(context, actor_alias, text_to_see, section_name,
                                                             page_name):
    page = get_last_visited_page(context, actor_alias)
    page_to_be_landed = get_page_object(page_name)
    print(page.NAME)
    if page.NAME != text_to_see:
        raise Exception("Last visited page is incorrect - " + str(page.NAME))


def actor_decides_to_validate_entered_country_details_and_change_from_the_list(context, actor_alias, countryname,
                                                                               country_place_number, country_max
                                                                               , list_selection, page_name):
    page = get_page_object(page_name)
    has_action(page, "vallidate_entered_country_details")
    page.validate_entered_country_details(context.driver, countryname
                                          , country_place_number=int(country_place_number)
                                          , country_max=int(country_max)
                                          , list_selection=int(list_selection))


def actor_fills_out_and_submits_the_form(context, actor_alias, page_name):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "fills_out_submit")
    page.fills_out_submit(context.driver)


def generic_should_be_on_one_of_the_pages(
        context: Context, actor_alias: str, expected_pages: str
):
    expected_pages = [page.strip() for page in expected_pages.split(",")]
    urls = [get_page_object(name).URL for name in expected_pages]
    logging.debug(f"Will check {context.driver.current_url} against {urls}")
    results = defaultdict()
    for page_name in expected_pages:
        try:
            should_be_on_page(context, actor_alias, page_name)
            results[page_name] = True
            break
        except AssertionError:
            results[page_name] = False

    with assertion_msg(
            f"{actor_alias} expected to land on one of the following pages: {urls}, "
            f"instead we got to: {context.driver.current_url}"
    ):
        assert any(list(results.values()))


def promo_video_check_watch_time(
        context: Context, actor_alias: str, expected_watch_time: int
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "get_video_watch_time")
    watch_time = page.get_video_watch_time(context.driver)
    with assertion_msg(
            "%s expected to watch at least first '%d' seconds of the video but" " got '%d'",
            actor_alias,
            expected_watch_time,
            watch_time,
    ):
        assert watch_time >= expected_watch_time
    logging.debug(
        "%s was able to watch see at least first '%d' seconds of the"
        " promotional video",
        actor_alias,
        expected_watch_time,
    )


def promo_video_should_not_see_modal_window(context: Context, actor_alias: str):
    domestic.home.should_not_see_video_modal_window(context.driver)
    logging.debug(
        "As expected %s can't see promotional video modal window", actor_alias
    )


def should_be_on_working_page(context: Context, actor_alias: str):
    check_for_errors(context.driver.page_source, context.driver.current_url)
    logging.debug(f"{actor_alias} is on {context.driver.current_url}")


def should_be_on_working_page(context: Context, actor_alias: str):
    check_for_errors(context.driver.page_source, context.driver.current_url)
    logging.debug(f"{actor_alias} is on {context.driver.current_url}")


def should_be_on_page_or_be_redirected_to_page(
        context: Context, actor_alias: str, page_name: str, redirect_page: str
):
    try:
        should_be_on_page(context, actor_alias, page_name)
    except AssertionError:
        should_be_on_page(context, actor_alias, redirect_page)
        logging.debug(f"{actor_alias} was redirected to '{redirect_page}' page")


def should_see_sections(
        context: Context,
        actor_alias: str,
        sections_table: Table = None,
        *,
        sections_list: list = None,
):
    sections = sections_list or [row[0] for row in sections_table]
    logging.debug(
        "%s will look for following sections: '%s' on %s",
        actor_alias,
        sections,
        context.driver.current_url,
    )
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "should_see_sections")
    page.should_see_sections(context.driver, sections)


def should_not_see_sections(
        context: Context, actor_alias: str, sections_table: Table = None
):
    sections = [row[0] for row in sections_table]
    logging.debug(f"sections {sections}")
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "should_not_see_section")
    for section in sections:
        page.should_not_see_section(context.driver, section)
        logging.debug(
            "As expected %s cannot see '%s' section on %s page",
            actor_alias,
            section,
            page.NAME,
        )


def should_see_links_in_specific_location(
        context: Context,
        actor_alias: str,
        section: str,
        links: Union[list, Table],
        location: str,
):
    page = get_page_object(location)
    has_action(page, "should_see_link_to")
    if isinstance(links, Table):
        links = [row[0] for row in links]
    for link in links:
        page.should_see_link_to(context.driver, section, link)
        logging.debug("%s can see link to '%s' in '%s'", actor_alias, link, location)


def articles_should_be_on_share_page(
        context: Context, actor_alias: str, social_media: str
):
    page_name = f"{social_media} - share on {social_media}"
    social_media_page = get_page_object(page_name)
    has_action(social_media_page, "should_be_here")
    social_media_page.should_be_here(context.driver)
    logging.debug("%s is on the '%s' share page", actor_alias, social_media)


def share_page_should_be_prepopulated(
        context: Context, actor_alias: str, social_media: str
):
    page_name = f"{social_media} - share on {social_media}"
    page = get_page_object(page_name)
    has_action(page, "check_if_populated")
    shared_url = context.article_url
    page.check_if_populated(context.driver, shared_url)
    clear_driver_cookies(driver=context.driver)
    logging.debug(
        "%s saw '%s' share page populated with appropriate data",
        actor_alias,
        social_media,
    )


def share_page_via_email_should_have_article_details(
        context: Context, actor_alias: str
):
    driver = context.driver
    body = driver.current_url
    subject = domestic.advice_article.get_article_name(driver)
    domestic.advice_article.check_share_via_email_link_details(driver, subject, body)
    logging.debug(
        "%s checked that the 'share via email' link contain correct subject: "
        "'%s' and message body: '%s'",
        actor_alias,
        subject,
        body,
    )


def promo_video_check_watch_time(
        context: Context, actor_alias: str, expected_watch_time: int
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "get_video_watch_time")
    watch_time = page.get_video_watch_time(context.driver)
    with assertion_msg(
            "%s expected to watch at least first '%d' seconds of the video but" " got '%d'",
            actor_alias,
            expected_watch_time,
            watch_time,
    ):
        assert watch_time >= expected_watch_time
    logging.debug(
        "%s was able to watch see at least first '%d' seconds of the"
        " promotional video",
        actor_alias,
        expected_watch_time,
    )


def promo_video_should_not_see_modal_window(context: Context, actor_alias: str):
    domestic.home.should_not_see_video_modal_window(context.driver)
    logging.debug(
        "As expected %s can't see promotional video modal window", actor_alias
    )


def header_check_logo(context: Context, actor_alias: str, logo_name: str):
    domestic.actions.check_logo(context.driver, logo_name)
    logging.debug(f"As expected {actor_alias} can see correct {logo_name} logo")


def header_check_favicon(context: Context, actor_alias: str):
    domestic.actions.check_dit_favicon(context.driver)
    logging.debug("As expected %s can see correct DIT favicon", actor_alias)


def language_selector_should_see_it(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    common_language_selector.should_see_it_on(context.driver, page=page)
    logging.debug("As expected %s can see language selector", actor_alias)


def should_see_page_in_preferred_language(
        context: Context, actor_alias: str, preferred_language: str
):
    common_language_selector.check_page_language_is(context.driver, preferred_language)
    logging.debug(
        f"{actor_alias} can see '{context.driver.current_url}' page in "
        f"'{preferred_language}"
    )


def fas_search_results_filtered_by_industries(
        context: Context, actor_alias: str, industry_names: List[str]
):
    fas.search_results.should_see_filtered_results(context.driver, industry_names)
    logging.debug(
        "%s can see results filtered by %s (%s)",
        actor_alias,
        industry_names,
        context.driver.current_url,
    )


def generic_should_see_expected_page_content(
        context: Context, actor_alias: str, expected_page_name: str

):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "should_see_content_for")
    page.should_see_content_for(context.driver, expected_page_name)
    logging.debug(
        "%s found content specific to %s on %s",
        actor_alias,
        expected_page_name,
        context.driver.current_url,
    )


def stats_and_tracking_elements_should_be_present(context: Context, names: Table):
    element_names = [row[0] for row in names]

    for name in element_names:
        invest.pixels.should_be_present(context.driver, name)


def stats_and_tracking_elements_should_not_be_present(context: Context, names: Table):
    element_names = [row[0] for row in names]

    for name in element_names:
        invest.pixels.should_not_be_present(context.driver, name)


def hpo_should_receive_enquiry_confirmation_email(context: Context, actor_alias: str):
    actor = get_actor(context, actor_alias)
    get_email_confirmations_with_matching_string(
        recipient_email=actor.email,
        subject=HPO_ENQUIRY_CONFIRMATION_SUBJECT,
        strings=HPO_PDF_URLS,
    )


def hpo_agent_should_receive_enquiry_email(context: Context, actor_alias: str):
    actor = get_actor(context, actor_alias)
    logging.debug(
        f"Looking for a notification sent to HPO agent: {HPO_AGENT_EMAIL_ADDRESS}"
    )
    get_email_confirmations_with_matching_string(
        recipient_email=HPO_AGENT_EMAIL_ADDRESS,
        subject=HPO_AGENT_EMAIL_SUBJECT,
        strings=[actor.email] + HPO_PDF_URLS,
    )


def form_check_state_of_element(
        context: Context, actor_alias: str, element: str, state: str
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "check_state_of_form_element")
    page.check_state_of_form_element(context.driver, element, state)
    logging.debug(
        f"{actor_alias} saw {element} in expected {state} state on "
        f"{context.driver.current_url}"
    )


def pdf_check_expected_details(
        context: Context, actor_alias: str, details_table: Table
):
    pdfs = context.pdfs
    pdf_texts = [
        (pdf["href"], extract_text_from_pdf(pdf_bytes=pdf["pdf"])) for pdf in pdfs
    ]
    details = {
        item[0].split(" = ")[0]: item[0].split(" = ")[1] for item in details_table
    }
    for href, text in pdf_texts:
        for name, value in details.items():
            error_message = (
                f"Could not find {name}: {value} in PDF text downloaded from " f"{href}"
            )
            assert value in text, error_message
            logging.debug(
                f"{actor_alias} saw correct {name} in the PDF downloaded from "
                f"{href}"
            )
    context.pdf_texts = pdf_texts


def pdf_check_for_dead_links(context: Context):
    pdf_texts = context.pdf_texts
    links = set(
        [
            word
            for _, text in pdf_texts
            for word in text.split()
            if any(item in word for item in ["http", "https", "www"])
        ]
    )
    logging.debug(f"Links found in PDFs: {links}")
    for link in links:
        parsed = urlparse(link)
        if not parsed.netloc:
            link = f"http://{link}"
        response = requests.get(link)
        error_message = (
            f"Expected 200 from {link} but got {response.status_code} instead"
        )
        assert response.status_code == 200, error_message
    logging.debug("All links in PDFs returned 200 OK")


def generic_should_see_message(context: Context, actor_alias: str, message: str = None):
    message = message or "This field is required"
    page_source = context.driver.page_source
    assertion_error = (
        f"Expected message '{message}' is not present on {context.driver.current_url}"
    )
    assert message in page_source, assertion_error
    logging.debug(
        f"{actor_alias} saw expected: '{message}' on {context.driver.current_url}"
    )


# BrowserStack times out after 60 seconds of inactivity
# https://www.browserstack.com/automate/timeouts
@retry(wait_fixed=5000, stop_max_attempt_number=7, wrap_exception=False)
def generic_contact_us_should_receive_confirmation_email(
        context: Context, actor_alias: str, subject: str, *, service: str = None
):
    avoid_browser_stack_idle_timeout_exception(context.driver)
    actor = get_actor(context, actor_alias)
    confirmation = get_email_confirmation_notification(
        email=actor.email, subject=subject, service=service
    )
    assert confirmation


def erp_should_receive_email_with_link_to_restore_saved_progress(
        context: Context, actor_alias: str
):
    avoid_browser_stack_idle_timeout_exception(context.driver)
    actor = get_actor(context, actor_alias)

    link = get_verification_link(
        actor.email, subject=EMAIL_ERP_PROGRESS_SAVED_MSG_SUBJECT
    )
    with assertion_msg(f"Could not find an email with link to restore saved progress"):
        assert link
    update_actor(context, actor_alias, saved_progress_link=link)


def generic_contact_us_should_receive_confirmation_email_containing_message(
        context: Context, actor_alias: str, subject: str, message: str
):
    actor = get_actor(context, actor_alias)
    confirmation = get_email_confirmations_with_matching_string(
        recipient_email=actor.email, subject=subject, strings=[message]
    )
    assert confirmation
    logging.debug(
        f"Found an email notification containing expected message: '{message}' send to "
        f"{actor.email}"
    )


@retry(wait_fixed=5000, stop_max_attempt_number=5)
def generic_a_notification_should_be_sent(
        context: Context, actor_alias: str, action: str, subject: str
):
    actor = get_actor(context, actor_alias)
    submissions = find_form_submissions_by_subject_and_action(
        email=actor.email, subject=subject, action=action
    )
    logging.debug(f"Email submissions from '{actor.email}': {submissions}")
    error = (
        f"Expected to find 1 '{action}' notification entitled '{subject}' sent to "
        f"'{actor.email}', but found {len(submissions)}"
    )
    assert len(submissions) == 1, error

    if not submissions[0]["is_sent"]:
        message = (
            f"A '{action}' notification entitled '{subject}' was NOT sent to "
            f"'{actor.email}' yet!"
        )
        logging.warning(message)
        blue(message)


def generic_a_notification_should_be_sent_to_specific_dit_office(
        context: Context, actor_alias: str, mailbox_name: str
):
    actor = get_actor(context, actor_alias)
    mailbox_email = FORMS_API_MAILBOXES[mailbox_name]
    submissions = find_form_submissions_for_dit_office(
        mailbox=mailbox_email, sender=actor.email
    )
    logging.debug(
        f"Email submissions from '{actor.email}' to '{mailbox_email}': {submissions}"
    )
    error = (
        f"Expected to find 1 notification sent to '{mailbox_email}' about contact "
        f"enquiry from {actor.email}, but found {len(submissions)}"
    )
    assert len(submissions) == 1, error

    error = (
        f"A notification about enquiry from '{actor.email}' was NOT sent to "
        f"{mailbox_name} mailbox: '{mailbox_email}'!"
    )
    assert submissions[0]["is_sent"], error
    logging.debug(
        f"A notification about enquiry from {actor.email} was successfully sent to "
        f"{mailbox_name} mailbox: {mailbox_email}"
    )


def generic_a_notification_should_not_be_sent_to_specific_dit_office(
        context: Context, actor_alias: str, mailbox_name: str
):
    actor = get_actor(context, actor_alias)
    forms_data = actor.forms_data
    uuid = None
    for data in forms_data.values():
        if "full name" in data:
            uuid = data["full name"]
            break
        if "family name" in data:
            uuid = data["family name"]
            break
        if "last name" in data:
            uuid = data["last name"]
            break
        if "lastname" in data:
            uuid = data["lastname"]
            break
    assert uuid, f"Could not find last name UUID in user's form data: {forms_data}"
    mailbox_email = FORMS_API_MAILBOXES[mailbox_name]
    submissions = find_form_submissions_for_dit_office(
        mailbox=mailbox_email, sender=actor.email, uuid=uuid
    )
    logging.debug(
        f"Email submissions from '{actor.email}' to '{mailbox_email}': {submissions}"
    )
    error = (
        f"Expected to find at least 1 notification sent to '{mailbox_email}' about "
        f"contact enquiry from blocked email address: {actor.email}, but found "
        f"{len(submissions)}"
    )
    assert len(submissions) >= 1, error

    error = (
        f"An unnecessary notification about enquiry from '{actor.email}' was sent to "
        f"'{mailbox_name}': '{mailbox_email}'!"
    )
    assert not submissions[0]["is_sent"], error
    logging.debug(
        f"Unfortunately a notification about enquiry from {actor.email} was sent to "
        f"{mailbox_name} mailbox: {mailbox_email}"
    )


def generic_should_see_form_choices(
        context: Context, actor_alias: str, option_names: Table
):
    option_names = [row[0] for row in option_names]
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "should_see_form_choices")
    page.should_see_form_choices(context.driver, option_names)


def office_finder_should_see_correct_office_details(
        context: Context, actor_alias: str, trade_office: str, city: str
):
    contact_us_office_finder_search_results.should_see_office_details(
        context.driver, trade_office, city
    )
    logging.debug(
        f"{actor_alias} found contact details for trade '{trade_office}' office"
        f" in '{city}'"
    )


@retry(wait_fixed=5000, stop_max_attempt_number=3, wrap_exception=False)
def forms_confirmation_email_should_not_be_sent(context: Context, actor_alias: str):
    actor = get_actor(context, actor_alias)
    submissions = find_form_submissions(actor.email)
    assert submissions, f"No form submissions found for {actor_alias}"
    error = (
        f"Expected to find an unsent submission for {actor_alias} but found a sent"
        f" one. Check spam filters"
    )
    assert not submissions[0]["is_sent"], error


def marketplace_finder_should_see_marketplaces(
        context: Context, actor_alias: str, country: str
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "should_see_marketplaces")
    page.should_see_marketplaces(context.driver, country)


def domestic_search_finder_should_see_page_number(
        context: Context, actor_alias: str, page_num: int
):
    should_be_on_page(
        context,
        actor_alias,
        f"{domestic.search_results.SERVICE} - {domestic.search_results.NAME}",
    )
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "should_see_page_number")
    page.should_see_page_number(context.driver, page_num)


def generic_should_be_on_one_of_the_pages(
        context: Context, actor_alias: str, expected_pages: str
):
    expected_pages = [page.strip() for page in expected_pages.split(",")]
    urls = [get_page_object(name).URL for name in expected_pages]
    logging.debug(f"Will check {context.driver.current_url} against {urls}")
    results = defaultdict()
    for page_name in expected_pages:
        try:
            should_be_on_page(context, actor_alias, page_name)
            results[page_name] = True
            break
        except AssertionError:
            results[page_name] = False

    with assertion_msg(
            f"{actor_alias} expected to land on one of the following pages: {urls}, "
            f"instead we got to: {context.driver.current_url}"
    ):
        assert any(list(results.values()))


def soo_contact_form_should_be_prepopulated(context: Context, actor_alias: str):
    actor = get_actor(context, actor_alias)
    page = get_last_visited_page(context, actor_alias)

    form_po = profile.enrol_enter_your_business_details_step_2
    form_data_key = f"{form_po.SERVICE} - {form_po.NAME} - {form_po.TYPE}"
    form_data = actor.forms_data[form_data_key]

    has_action(page, "check_if_populated")
    page.check_if_populated(context.driver, form_data)


def generic_should_see_prepopulated_fields(
        context: Context, actor_alias: str, table: Table
):
    table.require_columns(["form", "fields"])
    expected_form_fields = {
        row.get("form"): [
            field.strip() for field in row.get("fields").split(",") if field
        ]
        for row in table
    }
    error = f"Expected to check at least 1 list of form fields but got 0"
    assert expected_form_fields, error

    actor = get_actor(context, actor_alias)
    page = get_last_visited_page(context, actor_alias)

    field_values_to_check = {}
    for form_name, fields in expected_form_fields.items():
        form_page_object = get_page_object(form_name)
        form_full_page_name = get_full_page_name(form_page_object)
        submitted_form_data = actor.forms_data[form_full_page_name]
        for field in fields:
            field_values_to_check[field] = submitted_form_data[field]

    logging.debug(
        f"Will check if form on '{get_full_page_name(page)}' is populated with "
        f"following values: {field_values_to_check}"
    )
    has_action(page, "check_if_populated")
    page.check_if_populated(context.driver, field_values_to_check)


def generic_check_gtm_datalayer_properties(context: Context, table: Table):
    row_names = [
        "businessUnit",
        "loginStatus",
        "siteLanguage",
        "siteSection",
        "siteSubsection",
        "userId",
    ]
    table.require_columns(row_names)
    raw_properties = {name: row.get(name) for name in row_names for row in table}
    expected_properties = replace_string_representations(raw_properties)
    found_properties = get_gtm_data_layer_properties(context.driver)

    with assertion_msg(
            f"Expected to see following GTM data layer properties:\n"
            f"'{expected_properties}'\n but got:\n'{found_properties}'\non: "
            f"{context.driver.current_url}\ndiff:\n"
            f"{diff(expected_properties, found_properties)}"
    ):
        assert expected_properties == found_properties


def table_to_list_of_dicts(table: Table) -> List[dict]:
    """Convert behave's table to a list of dictionaries"""
    result = []
    for row in table:
        result.append({name: row.get(name) for name in table.headings})
    return result


def generic_check_gtm_events(context: Context):
    required_columns = ["action", "element", "event", "type", "value"]
    context.table.require_columns(required_columns)
    expected_gtm_events = table_to_list_of_dicts(context.table)

    for event in expected_gtm_events:
        if event["type"] == "Empty string":
            event["type"] = ""
        if event["value"] == "Empty string":
            event["value"] = ""
        if event["type"] == "Not present":
            event.pop("type")
        if event["value"] == "Not present":
            event.pop("value")
    logging.debug(f"Expected GTM events: {expected_gtm_events}")
    registered_gtm_events = get_gtm_data_layer_events(context.driver)

    missing_events = [
        event for event in expected_gtm_events if event not in registered_gtm_events
    ]
    with assertion_msg(
            f"Could not find following GTM events:\n{missing_events}\n"
            f"among following GTM events:\n{registered_gtm_events}\n"
            f"registered on: {context.driver.current_url}\n"
            f"Diff:\n{diff(expected_gtm_events, registered_gtm_events)}"
    ):
        assert not missing_events

    with assertion_msg(
            f"Expected to find {len(expected_gtm_events)} registered GTM event(s) but "
            f"found {len(registered_gtm_events)} instead: "
            f"{registered_gtm_events}"
    ):
        assert len(expected_gtm_events) == len(registered_gtm_events)


def generic_check_cookies(context: Context):
    required_columns = ["name", "value"]
    context.table.require_columns(required_columns)
    expected_cookies = table_to_list_of_dicts(context.table)
    driver = context.driver
    try:
        current_cookies = driver.get_cookies()
    except WebDriverException as ex:
        logging.error(f"Failed to get cookies on {driver.current_url}")
        raise ex
    for cookie in expected_cookies:
        name = cookie["name"]
        value = cookie["value"]
        error = f"Could not find '{name}' cookie on {driver.current_url}"
        assert any(c["name"] == name for c in current_cookies), error
        logging.debug(f"Found expected '{name}' cookie")
        for c in current_cookies:
            if c["name"] == name:
                error = f"Expected {name} cookie to be '{value}' but got '{c['value']}' instaed"
                assert c["value"] == value, error
                logging.debug(
                    f"As expected {name} cookie was set to expected '{value}'"
                )


def menu_items_should_be_visible(context: Context):
    ids = ["great-header-nav-mobile", "great-header-mobile-nav", "great-header-nav"]
    for value in ids:
        try:
            element = context.driver.find_element(by=By.ID, value=value)
            break
        except NoSuchElementException:
            continue
    else:
        raise
    with selenium_action(context.driver, f"Menu items should be visible"):
        take_screenshot(context.driver, "mobile menu")
        assert element.is_displayed()


def generic_should_be_able_to_print(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "should_be_able_to_print")
    take_screenshot(context.driver, "should_be_able_to_print")
    page.should_be_able_to_print(context.driver)
    logging.debug(
        f"{actor_alias} is able to print out contents of: {context.driver.current_url}"
    )


def erp_should_see_number_of_product_codes_to_select(
        context: Context, actor_alias: str, comparison_description: str
):
    comparison_details = get_comparison_details(comparison_description)

    page = get_last_visited_page(context, actor_alias)
    has_action(page, "should_see_number_of_product_codes_to_select")
    take_screenshot(context.driver, "should_see_number_of_product_codes_to_select")
    check_for_errors(context.driver.page_source, context.driver.current_url)
    page.should_see_number_of_product_codes_to_select(
        context.driver, comparison_details
    )
    logging.debug(
        f"{actor_alias} saw: {comparison_description} product code(s) to select"
    )


def erp_should_see_number_of_product_categories_to_expand(
        context: Context, actor_alias: str, comparison_description: str
):
    comparison_details = get_comparison_details(comparison_description)

    page = get_last_visited_page(context, actor_alias)
    has_action(page, "should_see_number_of_product_categories_to_expand")
    take_screenshot(context.driver, "should_see_number_of_product_categories_to_expand")
    check_for_errors(context.driver.page_source, context.driver.current_url)
    page.should_see_number_of_product_categories_to_expand(
        context.driver, comparison_details
    )
    logging.debug(
        f"{actor_alias} saw: {comparison_description} product categories(s) to expand"
    )


# def erp_should_see_correct_data_on_summary_page(context: Context, actor_alias: str):
#     actor = get_actor(context, actor_alias)
#     take_screenshot(context.driver, "should_see_correct_data_on_summary_page")
#     erp.summary.should_see_correct_data_on_summary_page(
#         context.driver, actor.forms_data
#     )
#     logging.debug(f"{actor_alias} saw: all expected data on the ERP Summary page")

@retry(wait_fixed=5000, stop_max_attempt_number=5)
def fas_buyer_should_be_signed_up_for_email_updates(context: Context, actor_alias: str):
    actor = get_actor(context, actor_alias)
    response = DIRECTORY_TEST_API_CLIENT.get(
        f"testapi/buyer/{actor.email}/", authenticator=BASIC_AUTHENTICATOR,
    )
    with assertion_msg(
            f"Expected 200 OK but got {response.status_code} from {response.url}"
    ):
        assert response.status_code == 200
        assert response.json()["email"] == actor.email
        assert response.json()["name"] == actor.alias
        assert response.json()["company_name"] == "AUTOMATED TESTS"
    logging.debug(
        f"{actor_alias} successfully signed up for email updates. "
        f"Here's Buyer's data: {response.json()}"
    )


def generic_search_for_phrase(context: Context, actor_alias: str, phrase: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "search")
    page.search(context.driver, phrase)


def actor_decides_to_click_on_page_with_lesson_link(
        context: Context, actor_alias: str, lesson_name: str, *, page_name: str = None, wait_for_it: bool = True
):
    if page_name:
        page = get_page_object(page_name)
    else:
        page = get_last_visited_page(context, actor_alias)
    has_action(page, "find_and_click_lesson_link")
    page.find_and_click_lesson_link(context.driver, lesson_name)

def actor_decides_to_click_continue_on_page(context:Context,page_name):
    page = get_page_object(page_name)
    has_action(page, "click_on_continue")
    page.click_on_continue(context.driver)

def actor_decides_to_select_random_product_on_page(
        context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "find_and_select_random_product_and_click_continue")
    page.find_and_select_random_product_and_click_continue(context.driver)

def actor_decides_to_select_random_export_plan_on_page(context, actor_alias,page_name):
    page = get_page_object(page_name)
    has_action(page, "find_and_select_random_export_plan")
    page.find_and_select_random_export_plan(context.driver)
