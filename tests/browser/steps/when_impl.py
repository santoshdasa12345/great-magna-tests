# -*- coding: utf-8 -*-
"""When step implementations."""
import logging
import random
import time
from inspect import signature
from types import MethodType
from typing import Dict
from urllib.parse import urljoin

from behave.model import Table
from behave.runner import Context
from browserpages import (  # search,
    common_language_selector,
    domestic,
    fas,
    get_page_object,
    greatmagna,
    learntoexport,
    profile,
    soo,
    sso,
)
from browserpages.common_actions import (
    accept_all_cookies,
    add_actor,
    assert_catcha_in_dev_mode,
    avoid_browser_stack_idle_timeout_exception,
    barred_actor,
    find_and_click_on_page_element,
    find_elements,
    find_selector_by_name,
    get_actor,
    get_full_page_name,
    get_last_visited_page,
    go_to_url,
    revisit_page_on_access_denied,
    scroll_to,
    selenium_action,
    take_screenshot,
    try_alternative_click_on_exception,
    unauthenticated_actor,
    untick_selected_checkboxes,
    update_actor,
    update_actor_forms_data,
    wait_for_page_load_after_action,
)
from browserutils.cms_api import get_news_articles
from browserutils.gtm import get_gtm_event_definitions, trigger_js_event
from retrying import retry
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared.gov_notify import (
    get_email_verification_code,
    get_verification_link,
)
from great_magna_tests_shared.utils import check_for_errors
from steps import has_action

NUMBERS = {
    "random": 0,
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4,
    "fifth": 5,
    "sixth": 6,
}


def retry_if_webdriver_error(exception):
    """Return True if we should retry on WebDriverException, False otherwise"""
    return isinstance(exception, (TimeoutException, WebDriverException))


def retry_if_assertion_error(exception):
    """Return True if we should retry on AssertionError, False otherwise"""
    return isinstance(exception, AssertionError)


# BrowserStack times out after 60 seconds of inactivity
# https://www.browserstack.com/automate/timeouts
@retry(
    wait_fixed=5000,
    stop_max_attempt_number=5,
    retry_on_exception=retry_if_webdriver_error,
    wrap_exception=False,
)
def visit_page(context: Context, actor_alias: str, page_name: str):
    """Will visit specific page.

    NOTE:
    In order for the retry scheme to work properly you should have
    the webdriver' page load timeout set to value lower than the retry's
    `wait_fixed` timer, e.g `driver.set_page_load_timeout(time_to_wait=30)`
    """

    def is_special_case(page_name: str) -> bool:
        parts = page_name.split(" - ")
        return len(parts) == 3

    if not get_actor(context, actor_alias):
        add_actor(context, unauthenticated_actor(actor_alias))

    page = get_page_object(page_name)

    has_action(page, "visit")

    if is_special_case(page_name) and hasattr(page, "SubURLs"):
        subpage_name = page_name.split(" - ")[1].lower()
        special_url = page.SubURLs[subpage_name]
        logging.debug(
            f"{actor_alias} will visit '{page_name}' subpage using: '{special_url}"
        )
        page.visit(context.driver, page_name=subpage_name)
    else:
        logging.debug(
            f"{actor_alias} will visit '{page_name}' page using: '{page.URL}'"
        )
        page.visit(context.driver)

    take_screenshot(context.driver, f"visit page {page_name}")
    accept_all_cookies(context.driver)
    check_for_errors(context.driver.page_source, context.driver.current_url)
    update_actor(context, actor_alias, visited_page=page)


def set_small_screen(context: Context):
    context.driver.set_window_position(0, 0)
    context.driver.set_window_size(768, 1024)


def should_be_on_page(context: Context, actor_alias: str, page_name: str):
    page = get_page_object(page_name)
    # revisit_page_on_access_denied(context.driver, page, page_name)
    take_screenshot(context.driver, f"should be on {page_name}")
    check_for_errors(context.driver.page_source, context.driver.current_url)
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


def clear_the_cookies(context: Context, actor_alias: str):
    try:
        cookies = context.driver.get_cookies()
        logging.debug("COOKIES: %s", cookies)
        context.driver.delete_all_cookies()
        logging.debug("Successfully cleared cookies for %s", actor_alias)
        cookies = context.driver.get_cookies()
        logging.debug("Driver cookies after clearing them: %s", cookies)
    except WebDriverException:
        logging.error("Failed to clear cookies for %s", actor_alias)


def generic_accept_all_cookies(context: Context, actor_alias: str):
    driver = context.driver
    accept_all_cookies(driver)
    logging.debug(f"{actor_alias} accepted all cookies on {driver.current_url}")


def articles_open_any(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "open_any_article")
    article_name = page.open_any_article(context.driver)
    update_actor(context, actor_alias, visited_articles=article_name)
    logging.info(f"{actor_alias} opened article: {article_name}")


def click_on_page_element(
    context: Context, actor_alias: str, element_name: str, *, page_name: str = None
):
    if page_name:
        page = get_page_object(page_name)
    else:
        page = get_last_visited_page(context, actor_alias)
    logging.debug(page)
    find_and_click_on_page_element(context.driver, page.SELECTORS, element_name)
    logging.debug(
        "%s decided to click on '%s' on '%s' page", actor_alias, element_name, page.NAME
    )


def click_on_page_element_with_wait(
    context: Context,
    actor_alias: str,
    element_name: str,
    *,
    page_name: str = None,
    wait_for_it: bool = True,
):
    if page_name:
        page = get_page_object(page_name)
    else:
        page = get_last_visited_page(context, actor_alias)
    logging.debug(page)
    find_and_click_on_page_element(
        context.driver, page.SELECTORS, element_name, wait_for_it=wait_for_it
    )
    logging.debug(
        "%s decided to click on '%s' on '%s' page", actor_alias, element_name, page.NAME
    )


@retry(
    wait_fixed=1000,
    stop_max_attempt_number=8,
    retry_on_exception=retry_if_assertion_error,
    wrap_exception=False,
)
def generic_fill_out_and_submit_form(
    context: Context,
    actor_alias: str,
    *,
    custom_details_table: Table = None,
    retry_on_errors: bool = False,
    go_back: bool = False,
    form_name: str = None,
    check_captcha_dev_mode: bool = False,
):
    # if check_captcha_dev_mode:
    #     assert_catcha_in_dev_mode(context.driver)
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


@retry(
    wait_fixed=1000,
    stop_max_attempt_number=8,
    retry_on_exception=retry_if_assertion_error,
    wrap_exception=False,
)
def generic_fill_out(
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
    if form_name:
        error = f"generate_form_details() in {page} should accept 'form_name' but it doesn't"
        assert signature(page.generate_form_details).parameters.get("form_name"), error
        error = f"fill_out() in {page} should accept 'form_name' but it doesn't"
        assert signature(page.fill_out).parameters.get("form_name"), error
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


def generic_submit_form(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "submit")
    page.submit(context.driver)


def actor_decides_to_fill_country_and_click_on_continue(
    context, actor_alias, country_name
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "countrysearch")
    page.countrysearch(context.driver, country_name=country_name)


def generic_country_name_to_fill_country_and_click_on_continue(
    context, actor_alias, element_name, form_name
):
    generic_fill_out(
        context,
        actor_alias,
        custom_details_table=context.table,
        form_name=form_name,
        check_captcha_dev_mode=False,
    )
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "searchcontinue")
    page.searchcontinue(context.driver)


def generic_open_industry_page(context: Context, actor_alias: str, industry_name: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "open_industry")
    page.open_industry(context.driver, industry_name)
    update_actor(context, actor_alias, visited_page=page)
    logging.debug("%s opened '%s' page on %s", actor_alias, industry_name, page.URL)


def generic_product_name_to_fill_country_and_click_on_continue(
    context, actor_alias, element_name, form_name
):
    generic_fill_out(
        context,
        actor_alias,
        custom_details_table=context.table,
        form_name=form_name,
        check_captcha_dev_mode=False,
    )
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "searchcontinue")
    page.searchcontinue(context.driver)


def actor_decides_to_fill_product_and_click_on_continue(
    context, actor_alias, product_name
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "productsearch")
    page.productsearch(context.driver, product_name=product_name)


def actor_decides_to_check_random_radio_and_click_on_continue(context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "find_and_select_random_radio_and_click_continue")
    page.find_and_select_random_radio_and_click_continue(context.driver)


def actor_should_be_on_refine_or_tradedata_page(context, actor_alias):
    actor_should_be_on_appropriate_page(context, actor_alias)


def actor_should_be_on_appropriate_page(context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    current_page_url = str(context.driver.current_url)
    # logging.debug(f"actor_should_be_on_appropriate_page:current_page_url -> {current_page_url}")
    is_refinement_page = False
    is_tradedata_page = False
    is_check_answers_page = False
    if "refine/?interaction" in current_page_url:
        is_refinement_page = True
    if "tradedata/?code" in current_page_url:
        is_tradedata_page = True
    if "check-your-answers" in current_page_url:
        is_check_answers_page = True

    if is_refinement_page:
        should_be_on_page(context, actor_alias, "Search - Refinement interaction")
        return
    if is_tradedata_page:
        should_be_on_page(context, actor_alias, "Search - Tradedata Codes")
        return
    error = f"Landed on unrecognized page"
    assert False, error


def actor_decides_not_to_enter_any_text_and_click_on_page_element(
    context, actor_alias, element_name
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "searchcontinue")
    page.searchcontinue(context.driver)


def actor_select_random_data_click_continue_until_tradedata_or_checkanswers_page(
    context,
    actor_alias,
    max_number_pages,
    is_trade_data_page,
    is_check_your_answers_page,
):
    landed_on_tradedata_page = False
    landed_on_checkanswers_page = False
    counter = 0
    while counter < int(max_number_pages):
        counter += 1
        page = get_last_visited_page(context, actor_alias)
        has_action(page, "find_and_select_random_radio_and_click_continue")
        page.find_and_select_random_radio_and_click_continue(context.driver)
        # time.sleep(1)
        current_page_url = str(context.driver.current_url)
        # logging.debug(f"actor_select_random_data_click_continue_until_tradedata_page:current_page_url -> {current_page_url}")
        if "tradedata/?code" in current_page_url and is_trade_data_page:
            landed_on_tradedata_page = True
            break
        if "check-your-answers" in current_page_url and is_check_your_answers_page:
            landed_on_checkanswers_page = True
            break

    if not landed_on_tradedata_page and not landed_on_checkanswers_page:
        error = f"Couldn't reach Tradedata or CheckYourAnswers page after {max_number_pages} attempts!"
        assert False, error


def actor_select_or_enter_random_data_click_continue_until_checkanswers_page(
    context, actor_alias, max_number_pages
):
    counter = 0
    while counter < int(max_number_pages):
        current_page_url = str(context.driver.current_url)
        # logging.debug(f"current_page_url -> {current_page_url}")
        # time.sleep(1)
        if "tradedata/?code" in current_page_url:
            page = get_page_object("Search - Tradedata codes")
            has_action(page, "find_and_select_random_radio_and_click_continue")
            has_action(page, "searchcontinue")
            page.find_and_select_random_radio_and_click_continue(context.driver)
            page.searchcontinue(context.driver)
        elif "check-your-answers" in current_page_url:
            break
        elif "refine/?interaction" in current_page_url:
            try:
                page = get_page_object("Search - Refinement Interaction")
                has_action(page, "find_and_select_random_radio_and_click_continue")
                page.find_and_select_random_radio_and_click_continue(context.driver)
                # time.sleep(1)
                composition_text_element = context.driver.find_element_by_xpath(
                    '//*[@id="composition_message"]'
                )
                composition_text = str(composition_text_element.text)
                if "The numbers need to add up to 100." in composition_text:
                    page = get_page_object("Search - Refinement Interaction")
                    has_action(page, "find_and_enter_random_composition_percent")
                    page.find_and_enter_random_composition_percent(
                        context.driver, "100"
                    )
                    find_and_click_on_page_element(
                        context.driver, page.SELECTORS, "Continue"
                    )
            except NoSuchElementException:
                pass
        counter += 1


def actor_decides_to_click_back_until_reaches_product_search_page(
    context, actor_alias, element_name, max_number_pages, page_name
):
    counter = 0
    while counter < int(max_number_pages):
        current_page_url = str(context.driver.current_url)
        # logging.debug(f"current_page_url -> {current_page_url}")
        if "tradedata/?code" in current_page_url:
            page = get_page_object("Search - Tradedata codes")
            find_and_click_on_page_element(context.driver, page.SELECTORS, element_name)
        elif "check-your-answers" in current_page_url:
            page = get_page_object("ImportTariff - CheckYourAnswers")
            find_and_click_on_page_element(context.driver, page.SELECTORS, element_name)
        elif "search/" in current_page_url:
            page = get_page_object(page_name)
            break
        elif "refine/?interaction" in current_page_url:
            page = get_page_object("Search - Refinement Interaction")
            find_and_click_on_page_element(context.driver, page.SELECTORS, element_name)
        else:
            error = f"Landed on unrecognized page after {counter} attempts!"
            assert False, error

        counter += 1


def actor_select_random_data_click_continue_until_composition_page(
    context, actor_alias, max_number_pages
):
    landed_on_composition_page = False
    counter = 0
    while counter < int(max_number_pages):
        counter += 1

        current_page_url = str(context.driver.current_url)
        # logging.debug(f"actor_select_random_data_click_continue_until_composition_page:current_page_url -> {current_page_url}")

        try:
            page = get_last_visited_page(context, actor_alias)
            has_action(page, "find_and_select_random_radio_and_click_continue")
            page.find_and_select_random_radio_and_click_continue(context.driver)
            # page = get_last_visited_page(context, actor_alias)
            # logging.debug(
            #     f"actor_select_random_data_click_continue_until_composition_page:get_last_visited_page ->  {page.NAME}")
            # should_be_on_page(context, actor_alias, f"Search - {page.NAMES[1]}")
            composition_text_element = context.driver.find_element_by_xpath(
                '//*[@id="composition_message"]'
            )
            composition_text = str(composition_text_element.text)
            # logging.debug(
            #     f"actor_select_random_data_click_continue_until_composition_page:composition_text ->  {composition_text}")

            if "The numbers need to add up to 100." in composition_text:
                landed_on_composition_page = True
                # logging.debug(
                #     f"actor_select_random_data_click_continue_until_composition_page:Reached Composition page!")
        except NoSuchElementException:
            logging.debug(
                f"actor_select_random_data_click_continue_until_composition_page:Couldn't reach Composition page after {counter} attempts!"
            )

        if landed_on_composition_page:
            break

    if not landed_on_composition_page:
        error = f"Couldn't reach Composition page after {max_number_pages} attempts!"
        assert False, error


def actor_enter_random_composition_data_equal_to_hundred_percent(context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "find_and_enter_random_composition_percent")
    page.find_and_enter_random_composition_percent(context.driver, "100")


def actor_enter_random_composition_data_not_equal_to_hundred_percent(
    context, actor_alias
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "find_and_enter_random_composition_percent")
    page.find_and_enter_random_composition_percent(context.driver, "80")


def actor_decides_to_enter_blank_spaces_click_on_continue(
    context, actor_alias, product_name, element_name
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "productsearch")
    page.productsearch(context.driver, product_name=product_name)
    click_on_page_element(context, actor_alias, element_name)


def actor_decides_to_enter_email_address_and_click_login(
    context, actor_alias, email_address, password
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "login")
    email_address = str(email_address).strip()  # trimming
    password = str(password).strip()  # trimming
    page.login(context.driver, email_address=email_address, password=password)
    time.sleep(2)


def actor_decides_to_enter_email_address_and_click_sign_up(
    context, actor_alias, email_address, password
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "sign_up")
    email_address = email_address.replace("xxxx", str(random.randint(6666, 9999)))
    page.sign_up(context.driver, email_address=email_address, password=password)


def actor_should_be_able_to_click_on_skipwalkthrough(context, actor_alias):
    # time.sleep(5)
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_skip_walk_through")
    # has_action(page, "click_avatar")
    page.click_skip_walk_through(context.driver)
    # page.click_avatar(context.driver)


def actor_should_be_able_to_click_on_avatar(context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_avatar")
    page.click_avatar(context.driver)


def actor_should_be_able_to_click_on_SignOut(context, actor_alias):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_signout")
    page.click_signout(context.driver)


def actor_decides_to_page_tour_and_click_on_page_element(
    context, actor_alias, element_name
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_show_me_around")
    page.click_show_me_around(context.driver)


def promo_video_watch(context: Context, actor_alias: str, *, play_time: int = None):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "play_video")
    page.play_video(context.driver, play_time=play_time)
    logging.debug("%s was able to play the video", actor_alias)


def promo_video_close(context: Context, actor_alias: str):
    learntoexport.choose_the_right_route_to_market.close_video(context.driver)
    logging.debug("%s closed the video", actor_alias)


def click_on_link_element_in_page(
    context: Context, actor_alias: str, element_name: str, *, page_name: str = None
):
    if page_name:
        page = get_page_object(page_name)
    else:
        page = get_last_visited_page(context, actor_alias)
    # logging.debug(page)
    has_action(page, "find_and_click")
    page.find_and_click(context.driver, element_selector_name=element_name)


def generic_submit_form(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "submit")
    page.submit(context.driver)


def actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months(
    context, actor_alias
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "click_on_i_have_exported_in_the_last_12_months")
    page.click_on_i_have_exported_in_the_last_12_months(context.driver)


def domestic_open_random_advice_article(context: Context, actor_alias: str):
    if not get_actor(context, actor_alias):
        add_actor(context, unauthenticated_actor(actor_alias))
    driver = context.driver
    domestic.advice_landing.visit(driver)
    take_screenshot(driver, domestic.advice_landing.NAME)
    check_for_errors(driver.page_source, driver.current_url)
    advice_name = domestic.advice_landing.open_any_article(driver)
    article_name = domestic.advice_article_list.open_any_article(driver)
    domestic.advice_article.should_be_here(driver)
    update_actor(
        context,
        actor_alias,
        visited_page=domestic.advice_article,
        article_url=driver.current_url,
        article_category=advice_name,
        visited_articles=article_name,
    )


def generic_report_problem_with_page(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "report_problem")
    page.report_problem(context.driver)


def generic_click_on_random_marketplace(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "open_random_marketplace")
    page.open_random_marketplace(context.driver)


def domestic_open_random_market(context: Context, actor_alias: str):
    if not get_actor(context, actor_alias):
        add_actor(context, unauthenticated_actor(actor_alias))
    driver = context.driver
    domestic.markets_listing.visit(driver)
    take_screenshot(driver, domestic.markets_listing.NAME)
    check_for_errors(driver.page_source, driver.current_url)
    market_name = domestic.markets_listing.open_random_marketplace(driver)
    domestic.market_country_guide.should_be_here(driver)
    update_actor(
        context,
        actor_alias,
        visited_page=domestic.market_country_guide,
        article_url=driver.current_url,
        visited_articles=market_name,
    )


def generic_click_on_random_element(
    context: Context, actor_alias: str, elements_name: str
):
    page = get_last_visited_page(context, actor_alias)
    selector = find_selector_by_name(page.SELECTORS, elements_name)
    elements = find_elements(context.driver, selector)
    element = random.choice(elements)
    href = f" → {element.get_attribute('href')}" if element.tag_name == "a" else ""
    logging.debug(f"Will click on: '{element.text.strip()}'{href}")
    scroll_to(context.driver, element)
    with wait_for_page_load_after_action(context.driver, timeout=10):
        with try_alternative_click_on_exception(context.driver, element):
            element.click()


def generic_open_any_tag(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "open_any_tag")
    tag = page.open_any_tag(context.driver)
    update_actor(context, actor_alias, last_tag=tag)


def generic_download_all_pdfs(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "download_all_pdfs")
    context.pdfs = page.download_all_pdfs(context.driver)


def generic_visit_current_page_with_lang_parameter(
    context: Context, actor_alias: str, preferred_language: str
):
    page = get_last_visited_page(context, actor_alias)
    url = urljoin(page.URL, f"?lang={preferred_language}")
    context.driver.get(url)


def generic_open_news_article(context: Context, actor_alias: str, ordinal_number: str):
    ordinals = {"first": 1, "second": 2, "third": 3}
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "open_news_article")
    page.open_news_article(context.driver, ordinals[ordinal_number.lower()])


def generic_click_on_random_industry(context: Context, actor_alias: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "open_any_article")
    page.open_any_article(context.driver)


def domestic_submit_soo_contact_us_form(
    context: Context, actor_alias: str, custom_details_table: Table
):
    generic_fill_out_and_submit_form(
        context, actor_alias, custom_details_table=custom_details_table
    )
    domestic.contact_us_soo_3_about_your_products.should_be_here(context.driver)

    generic_fill_out_and_submit_form(context, actor_alias)
    domestic.contact_us_soo_4_your_experience.should_be_here(context.driver)

    generic_fill_out_and_submit_form(context, actor_alias)
    domestic.contact_us_soo_1_contact_details.should_be_here(context.driver)

    generic_fill_out_and_submit_form(context, actor_alias)
    domestic.contact_us_soo_5_thank_you.should_be_here(context.driver)


def generic_pick_random_radio_option_and_submit(
    context: Context, actor_alias: str, ignored: str
):
    ignored = [item.strip().lower() for item in ignored.split(",")]
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "pick_random_radio_option_and_submit")
    new_page = page.pick_random_radio_option_and_submit(context.driver, ignored)
    update_actor(context, actor_alias, visited_page=new_page)


def soo_look_for_marketplace(
    context: Context, actor_alias: str, country: str, category: str
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "search")
    page.search(context.driver, country, category)


def generic_search_for_phrase(context: Context, actor_alias: str, phrase: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "search")
    page.search(context.driver, phrase)


def contact_us_navigate_through_options(context: Context, actor_alias: str, via: str):
    intermediate = [name.strip() for name in via.split("->")]
    # 1) start at the Contact us "choose location" page
    visit_page(context, actor_alias, "Domestic - Contact us")
    # 2) click through every listed option
    for option in intermediate:
        generic_pick_radio_option_and_submit(context, actor_alias, option)


def domestic_find_more_about_search_result_type(
    context: Context, actor_alias: str, type_of: str
):
    should_be_on_page(context, actor_alias, get_full_page_name(domestic.search_results))
    domestic.search_results.click_on_result_of_type(context.driver, type_of)


def generic_trigger_all_gtm_events(
    context: Context, actor_alias: str, tagging_package: str, *, event_group: str = None
):
    events = get_gtm_event_definitions(
        context.driver, tagging_package, event_group=event_group
    )
    assert events, f"No GTM events were found on {context.driver.current_url}"
    for event_group, events in events.items():
        for event in events:
            trigger_js_event(context.driver, event)
    logging.debug(f"{actor_alias} triggered all events for GTM event handlers")


def generic_unfold_elements_in_section(
    context: Context, actor_alias: str, section_name: str
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "unfold_elements_in_section")
    page.unfold_elements_in_section(context.driver, section_name)


def registration_should_get_verification_email(context: Context, actor_alias: str):
    """Will check if the Exporter received an email verification message."""
    logging.debug("Searching for an email verification message...")
    actor = get_actor(context, actor_alias)
    link = get_verification_link(actor.email)
    update_actor(context, actor_alias, email_confirmation_link=link)


def registration_open_email_confirmation_link(context: Context, actor_alias: str):
    """Given Supplier has received a message with email confirmation link
    Then Supplier has to click on that link.
    """
    actor = get_actor(context, actor_alias)
    link = actor.email_confirmation_link

    # Step 1 - open confirmation link
    context.driver.get(link)

    # Step 3 - confirm that Supplier is on SSO Confirm Your Email page
    sso.confirm_your_email.should_be_here(context.driver)
    logging.debug("Supplier is on the SSO Confirm your email address page")


def registration_submit_form_and_verify_account(
    context: Context, actor_alias: str, *, fake_verification: bool = True
):
    actor = get_actor(context, actor_alias)

    generic_fill_out_and_submit_form(
        context, actor_alias, custom_details_table=context.table
    )

    if fake_verification:
        sso.common.verify_account(actor.email)
    else:
        registration_should_get_verification_email(context, actor_alias)
        registration_open_email_confirmation_link(context, actor_alias)
        sso.confirm_your_email.submit(context.driver)
    update_actor(context, actor_alias, registered=True)


def sign_out(context: Context, actor_alias: str):
    domestic.actions.go_to_sign_out(context.driver)
    sso.sign_out.submit(context.driver)
    logging.debug("%s signed out", actor_alias)


def sign_in(context: Context, actor_alias: str):
    actor = get_actor(context, actor_alias)
    email = actor.email
    password = actor.password
    sso.sign_in.visit(context.driver)
    take_screenshot(context.driver, sso.sign_in.NAME)
    sso.sign_in.should_be_here(context.driver)
    sso.sign_in.fill_out(context.driver, email, password)
    sso.sign_in.submit(context.driver)
    take_screenshot(context.driver, "after signing in")
    check_for_errors(context.driver.page_source, context.driver.current_url)


def office_finder_find_trade_office(context: Context, actor_alias: str, post_code: str):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "find_trade_office")
    page.find_trade_office(context.driver, post_code)


def click_on_header_menu_button(context: Context):
    try:
        button = context.driver.find_element(by=By.ID, value="js-mobile-button")
    except NoSuchElementException:
        button = context.driver.find_element(by=By.ID, value="mobile-menu-button")
    with selenium_action(context.driver, "click on header menu button"):
        button.click()


def generic_select_dropdown_option(
    context: Context, actor_alias: str, dropdown: str, option: str
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "select_dropdown_option")
    page.select_dropdown_option(context.driver, dropdown, option)


def language_selector_open(
    context: Context, actor_alias: str, *, with_keyboard: bool = False
):
    logging.debug("%s decided to go open language selector", actor_alias)
    page = get_last_visited_page(context, actor_alias)
    common_language_selector.open(
        context.driver, page=page, with_keyboard=with_keyboard
    )


def domestic_search_for_phrase_on_page(
    context: Context, actor_alias: str, phrase: str, page_name: str
):
    visit_page(context, actor_alias, page_name)
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "search")
    page.search(context.driver, phrase)


def domestic_search_result_has_more_than_one_page(
    context: Context, actor_alias: str, min_page_num: int
):
    should_be_on_page(
        context,
        actor_alias,
        f"{domestic.search_results.SERVICE} - {domestic.search_results.NAME}",
    )
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "has_pagination")
    page.has_pagination(context.driver, min_page_num)


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


def contact_us_get_to_page_via(
    context: Context,
    actor_alias: str,
    final_page: str,
    via: str,
    *,
    start_page: str = None,
):
    start_page = start_page or "Domestic - Contact us"
    intermediate = [name.strip() for name in via.split("->")]
    # 1) start at the Contact us "choose location" page
    visit_page(context, actor_alias, start_page)
    # 2) click through every listed option
    for option in intermediate:
        generic_pick_radio_option_and_submit(context, actor_alias, option)
    # 3) check if we're on the appropriate page
    should_be_on_page(context, actor_alias, final_page)


def generic_pick_radio_option_and_submit(
    context: Context, actor_alias: str, option: str
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "pick_radio_option_and_submit")
    new_page = page.pick_radio_option_and_submit(context.driver, option)
    update_actor(context, actor_alias, visited_page=new_page)


def articles_share_on_social_media(
    context: Context, actor_alias: str, social_media: str
):
    avoid_browser_stack_idle_timeout_exception(context.driver)
    context.article_url = context.driver.current_url
    if social_media.lower() == "email":
        domestic.advice_article.check_if_link_opens_email_client(context.driver)
    else:
        domestic.advice_article.check_if_link_opens_new_tab(
            context.driver, social_media
        )
        if not social_media.lower() == "linkedin":
            domestic.advice_article.share_via(context.driver, social_media)
    logging.debug(
        "%s successfully got to the share article on '%s'", actor_alias, social_media
    )


def actor_should_be_able_to_enter_products_and_country(context, products, country):
    page = get_page_object("GreatMagna - Dashboard")
    has_action(page, "fill_out_products_and_country")
    page.fill_out_products_and_country(context.driver, products, country)


def soo_find_and_open_random_marketplace(
    context: Context, actor_alias: str, country: str, category: str
):
    soo_look_for_marketplaces_from_home_page(context, actor_alias, country, category)
    generic_click_on_random_marketplace(context, actor_alias)
    should_be_on_page(
        context, actor_alias, f"{soo.marketplace.SERVICE} - {soo.marketplace.NAME}"
    )


def soo_look_for_marketplaces_from_home_page(
    context: Context, actor_alias: str, country: str, category: str
):
    visit_page(context, actor_alias, f"{soo.home.SERVICE} - {soo.home.NAME}")
    soo_look_for_marketplace(context, actor_alias, country, category)
    should_be_on_page(
        context,
        actor_alias,
        f"{soo.search_results.SERVICE} - {soo.search_results.NAME}",
    )


def generic_create_great_account(
    context: Context, actor_alias: str, business_type: str
):
    page_name = f"Profile - Enter your email address and set a password ({business_type})"  # noqa

    visit_page(context, actor_alias, page_name)
    generic_fill_out_and_submit_form(context, actor_alias)
    should_be_on_page(
        context,
        actor_alias,
        f"Profile - Enter your confirmation code ({business_type})",
    )

    generic_get_verification_code(context, actor_alias)
    generic_fill_out_and_submit_form(context, actor_alias)

    if business_type == "LTD, PLC or Royal Charter":
        should_be_on_page(
            context,
            actor_alias,
            f"Profile - Enter your business details ({business_type})",
        )
        generic_fill_out_and_submit_form(
            context, actor_alias, retry_on_errors=True, go_back=True
        )
        should_be_on_page(
            context,
            actor_alias,
            f"Profile - Enter your business details [step 2] ({business_type})",
        )
        generic_fill_out_and_submit_form(context, actor_alias)
        should_be_on_page(
            context, actor_alias, f"Profile - Enter your details ({business_type})"
        )
        generic_fill_out_and_submit_form(context, actor_alias)
    elif business_type == "Sole trader or other type of business":
        should_be_on_page(
            context,
            actor_alias,
            f"Profile - Enter your business details ({business_type})",
        )
        generic_fill_out_and_submit_form(
            context, actor_alias, retry_on_errors=False, go_back=False
        )
        should_be_on_page(
            context, actor_alias, f"Profile - Enter your details ({business_type})"
        )
        generic_fill_out_and_submit_form(context, actor_alias)
    elif business_type == "UK taxpayer":
        should_be_on_page(
            context, actor_alias, f"Profile - Enter your details ({business_type})"
        )
        generic_fill_out_and_submit_form(context, actor_alias)

    should_be_on_page(
        context, actor_alias, f"Profile - Account created ({business_type})"
    )


def generic_at_least_n_news_articles(
    context: Context, n: int, visitor_type: str, service: str
):
    context.articles = get_news_articles(service, visitor_type)
    error = (
        f"Expected to find at least {n} news articles on {service} but "
        f"got {len(context.articles)}"
    )
    assert len(context.articles) >= n, error


def sso_actor_received_email_confirmation_code(
    context: Context, actor_alias: str, business_type: str
):
    page_name = (
        f"Profile - Enter your email address and set a password ({business_type})"
    )
    visit_page(context, actor_alias, page_name)
    generic_fill_out_and_submit_form(context, actor_alias)
    end_page_name = f"Profile - Enter your confirmation code ({business_type})"
    should_be_on_page(context, actor_alias, end_page_name)
    generic_get_verification_code(context, actor_alias)


def generic_get_verification_code(
    context: Context, actor_alias: str, *, resent_code: bool = False
):
    """Will check if the Exporter received an email verification message."""
    logging.debug("Searching for an email verification message...")
    actor = get_actor(context, actor_alias)
    code = get_email_verification_code(actor.email, resent_code=resent_code)
    update_actor(context, actor_alias, email_confirmation_code=code)


def registration_create_and_verify_account(
    context: Context, actor_alias: str, *, fake_verification: bool = True
):
    visit_page(context, actor_alias, "SSO - Registration")
    registration_submit_form_and_verify_account(
        context, actor_alias, fake_verification=fake_verification
    )


def profile_start_registration_as(
    context: Context, actor_alias: str, business_type: str
):
    if not get_actor(context, actor_alias):
        add_actor(context, unauthenticated_actor(actor_alias))
    profile.enrol_select_business_type.visit(context.driver)
    second_page = profile.enrol_select_business_type.pick_radio_option_and_submit(
        context.driver, name=business_type
    )
    should_be_on_page(
        context, actor_alias, f"{second_page.SERVICE} - {second_page.NAME}"
    )


def fas_search_for_companies(
    context: Context, actor_alias: str, *, keyword: str = None, sector: str = None
):
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "search")
    optional_parameter_keywords = ["n/a", "no", "empty", "without", "any"]
    if keyword and keyword.lower() in optional_parameter_keywords:
        keyword = None
    if sector and sector.lower() in optional_parameter_keywords:
        sector = None
    page.search(context.driver, keyword=keyword, sector=sector)
    logging.debug(
        "%s will visit '%s' page using: '%s'", actor_alias, page.NAME, page.URL
    )


def fas_searched_for_companies(
    context: Context, actor_alias: str, *, keyword: str = None, sector: str = None
):
    visit_page(context, actor_alias, f"{fas.landing.SERVICE} - {fas.landing.NAME}")
    fas_search_for_companies(context, actor_alias, keyword=keyword, sector=sector)
    should_be_on_page(
        context,
        actor_alias,
        f"{fas.search_results.SERVICE} - {fas.search_results.NAME}",
    )


def language_selector_change_to(
    context: Context, actor_alias: str, preferred_language: str
):
    page = get_last_visited_page(context, actor_alias)
    logging.debug(
        f"{actor_alias} decided to change language on {visit_page} to"
        f" {preferred_language}"
    )
    common_language_selector.open(context.driver, page=page)
    common_language_selector.change_to(context.driver, page, preferred_language)


def fas_view_selected_company_profile(
    context: Context, actor_alias: str, profile_number: str
):
    number = NUMBERS[profile_number]
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "open_profile")
    page.open_profile(context.driver, number)
    logging.debug(
        "%s clicked on '%s' button on %s",
        actor_alias,
        profile_number,
        context.driver.current_url,
    )


def fas_view_article(context: Context, actor_alias: str, article_number: str):
    number = NUMBERS[article_number]
    page = get_last_visited_page(context, actor_alias)
    has_action(page, "open_article")
    page.open_article(context.driver, number)
    logging.debug(
        "%s clicked on '%s' article on %s",
        actor_alias,
        article_number,
        context.driver.current_url,
    )


def generic_remove_previous_field_selections(
    context: Context, actor_alias: str, selector_name: str
):
    page = get_last_visited_page(context, actor_alias)
    selector = find_selector_by_name(page.SELECTORS, selector_name)
    untick_selected_checkboxes(context.driver, selector)


def language_selector_close(context: Context, actor_alias: str):
    logging.debug("%s decided to close language selector", actor_alias)
    page = get_last_visited_page(context, actor_alias)
    common_language_selector.close(context.driver, page=page)


def generic_get_in_touch(
    context: Context, actor_alias: str, page_name: str, custom_details_table: Table
):
    visit_page(context, actor_alias, page_name)
    generic_fill_out_and_submit_form(
        context, actor_alias, custom_details_table=custom_details_table
    )
