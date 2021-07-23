# -*- coding: utf-8 -*-
# flake8: noqa
# fmt: off
"""When step definitions."""
from behave import register_type, when
from behave.runner import Context
import time
import parse
from steps.then_impl import (
    should_be_on_page,
    domestic_search_finder_should_see_page_number,
)
from steps.when_impl import (
    articles_open_any,
    click_on_page_element,
    visit_page,
    generic_fill_out,
    generic_fill_out_and_submit_form,
    generic_country_name_to_fill_country_and_click_on_continue,
    generic_product_name_to_fill_country_and_click_on_continue,
    actor_decides_to_fill_country_and_click_on_continue,
    actor_decides_to_fill_product_and_click_on_continue,
    actor_decides_to_check_random_radio_and_click_on_continue,
    actor_decides_not_to_enter_any_text_and_click_on_page_element,
    actor_decides_to_enter_blank_spaces_click_on_continue,
    actor_decides_to_enter_email_address_and_click_login,
    actor_should_be_able_to_click_on_skipwalkthrough,
    actor_should_be_able_to_click_on_avatar,
    actor_should_be_able_to_click_on_SignOut,
    actor_decides_to_page_tour_and_click_on_page_element,
    actor_decides_to_enter_email_address_and_click_sign_up,
    generic_accept_all_cookies,
    promo_video_watch,
    promo_video_close,
    actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months,
    generic_report_problem_with_page,
    generic_click_on_random_marketplace,
    generic_click_on_random_element,
    generic_open_any_tag,
    generic_download_all_pdfs,
    generic_submit_form,
    generic_visit_current_page_with_lang_parameter,
    generic_open_news_article,
    generic_click_on_random_industry,
    domestic_submit_soo_contact_us_form,
    generic_pick_random_radio_option_and_submit,
    soo_look_for_marketplace,
    generic_search_for_phrase,
    contact_us_navigate_through_options,
    domestic_find_more_about_search_result_type,
    generic_trigger_all_gtm_events,
    generic_unfold_elements_in_section,
    registration_submit_form_and_verify_account,
    sign_out,
    clear_the_cookies,
    sign_in,
    office_finder_find_trade_office,
    click_on_header_menu_button,
    generic_select_dropdown_option,
    language_selector_open,
    articles_share_on_social_media,
    generic_pick_radio_option_and_submit,
    actor_should_be_able_to_enter_products_and_country,
    click_on_link_element_in_page,

)


@when('"{actor_alias}" says that affected goods are "{option}" from overseas')
@when('"{actor_alias}" says that his business is in "{option}"')
@when('"{actor_alias}" says that his business is "{option}"')
@when('"{actor_alias}" says that he represents an "{option}"')
@when('"{actor_alias}" says that he represents a "{option}"')
@when('"{actor_alias}" chooses "{option}" option')
def when_actor_chooses_form_option_and_submits_form(
        context: Context, actor_alias: str, option: str):
    generic_pick_radio_option_and_submit(context, actor_alias, option)


@when('"{actor_alias}" opens any article on the list')
def given_actor_opens_any_article(context, actor_alias):
    articles_open_any(context, actor_alias)


@when('"{actor_alias}" decides to watch "{play_time:d}" seconds of the promotional video')
def when_actor_decides_to_watch_promo_video(
        context, actor_alias, *, play_time: int = None):
    promo_video_watch(context, actor_alias, play_time=play_time)


@when('"{actor_alias}" closes the window with promotional video')
def when_actor_decides_to_close_the_promotional_video(context, actor_alias):
    promo_video_close(context, actor_alias)


@when('"{actor_alias}" goes to the "{page_name}" page')
def when_actor_goes_to_page(context, actor_alias, page_name):
    visit_page(context, actor_alias, page_name)


@when('"{actor_alias}" decides to find out more about "{element_name}"')
@when('"{actor_alias}" decides to use "{element_name}" button')
@when('"{actor_alias}" decides to use "{element_name}" link')
@when('"{actor_alias}" decides to open "{element_name}"')
@when('"{actor_alias}" decides to click on "{element_name}"')
@when('"{actor_alias}" decides to see "{element_name}"')
@when('"{actor_alias}" decides to "{element_name}"')
def when_actor_decides_to_click_on_page_element(
        context, actor_alias, element_name):
    click_on_page_element(context, actor_alias, element_name)


@when('"{actor_alias}" decides to enter country name')
def when_actor_fills_out_and_submits_the_form(
        context: Context, actor_alias: str, *, form_name: str = None, check_captcha_dev_mode: bool = False
):
    generic_fill_out(
        context, actor_alias, custom_details_table=context.table, form_name=form_name,
        check_captcha_dev_mode=check_captcha_dev_mode,
    )


@when('"{actor_alias}" decides to enter country name "{country_name}" and click continue')
def when_actor_decides_to_fill_and_click_on_page_element(
        context, actor_alias, country_name, *, form_name: str = None):
    actor_decides_to_fill_country_and_click_on_continue(context, actor_alias, country_name)


@when('"{actor_alias}" decides to enter product name "{product_name}" and click continue')
def when_actor_decides_to_fill_and_click_on_page_element(
        context, actor_alias, product_name, *, form_name: str = None):
    actor_decides_to_fill_product_and_click_on_continue(context, actor_alias, product_name)


@when('"{actor_alias}" decides to select random treatment and click continue')
def when_actor_decides_to_fill_and_click_on_page_element(
        context, actor_alias, *, form_name: str = None):
    actor_decides_to_check_random_radio_and_click_on_continue(context, actor_alias)


@when('"{actor_alias}" decides to enter country name and click "{element_name}"')
def when_actor_decides_to_fill_country_and_click_on_page_element(
        context, actor_alias, element_name, *, form_name: str = None):
    generic_country_name_to_fill_country_and_click_on_continue(context, actor_alias, element_name, form_name)


@when('"{actor_alias}" decides to enter product name and click "{element_name}"')
def when_actor_decides_to_fill_product_and_click_on_page_element(
        context, actor_alias, element_name, *, form_name: str = None):
    generic_product_name_to_fill_country_and_click_on_continue(context, actor_alias, element_name, form_name)


@when('"{actor_alias}" decides not to enter any text and click "{element_name}"')
def when_actor_decides_not_to_enter_any_text_and_click_on_page_element(
        context, actor_alias, element_name, *, form_name: str = None):
    actor_decides_not_to_enter_any_text_and_click_on_page_element(context, actor_alias, element_name)


@when('"{actor_alias}" decides to enter Blank Spaces in product name "{product_name}" and click "{element_name}"')
def when_actor_decides_to_enter_blank_spaces_click_on_continue(
        context, actor_alias, product_name, element_name, *, form_name: str = None):
    actor_decides_to_enter_blank_spaces_click_on_continue(context, actor_alias, product_name, element_name)


@when('"{actor_alias}" decides to enter email address "{email_address}", password "{password}" and click Login')
def when_actor_decides_to_enter_email_address_and_click_login(
        context, actor_alias, email_address, password):
    actor_decides_to_enter_email_address_and_click_login(context, actor_alias, email_address, password)
    time.sleep(2)

@when('"{actor_alias}" should be on the "{page_name}" page')
def when_actor_should_be_on_page(
        context, actor_alias, page_name):
    should_be_on_page(context, actor_alias, page_name)


@when('"{actor_alias}" should be able to click on SkipWalkthrough')
def when_actor_should_be_able_to_click_on_skipwalkthrough(
        context, actor_alias):
    actor_should_be_able_to_click_on_skipwalkthrough(context, actor_alias)


@when('"{actor_alias}" should be able to click on Avatar')
def when_actor_should_be_able_to_click_on_avatar(
        context, actor_alias):
    actor_should_be_able_to_click_on_avatar(context, actor_alias)


@when('"{actor_alias}" should be able to click on SignOut')
def when_actor_should_be_able_to_click_on_SignOut(
        context, actor_alias):
    actor_should_be_able_to_click_on_SignOut(context, actor_alias)


@when('"{actor_alias}" decides to page tour and click "{element_name}"')
def when_actor_decides_to_page_tour_and_click_on_page_element(
        context, actor_alias, element_name, *, form_name: str = None):
    actor_decides_to_page_tour_and_click_on_page_element(context, actor_alias, element_name)


@when('"{actor_alias}" decides to enter email address "{email_address}", password "{password}" and click Sign up')
def when_actor_decides_to_enter_email_address_and_click_sign_up(
        context, actor_alias, email_address, password):
    actor_decides_to_enter_email_address_and_click_sign_up(context, actor_alias, email_address, password)


# @when('"{actor_alias}" decides to accept all cookies')
# def when_actor_decides_to_accept_all_cookies(
#         context, actor_alias):
#     generic_accept_all_cookies(context, actor_alias)

@when('"{actor_alias}" should be able to click on I have exported in the last 12 months')
def when_actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months(
        context, actor_alias):
    actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months(context, actor_alias)


@when('"{actor_alias}" decides to use one of the "{elements_name}"')
def when_actor_clicks_on_random_element(
        context: Context, actor_alias: str, elements_name: str
):
    generic_click_on_random_element(context, actor_alias, elements_name)


# -- TYPE CONVERTER: For a simple, on/off values
@parse.with_pattern(r".*")
def parse_on_off(text: str) -> bool:
    result = True if text.lower() == "on" else False
    return result


# REGISTER TYPE-CONVERTER: With behave
register_type(OnOff=parse_on_off)


@when('"{actor_alias}" decides to find new markets for her business')
@when('"{actor_alias}" decides to find new markets for his business')
@when('"{actor_alias}" fills out and submits the form with captcha dev check turned "{check_captcha_dev_mode:OnOff}"')
@when(
    '"{actor_alias}" fills out and submits "{form_name}" with "captcha in dev mode" check turned "{check_captcha_dev_mode:OnOff}"')
@when('"{actor_alias}" fills out and submits "{form_name}" form')
@when('"{actor_alias}" fills out and submits the form')
def when_actor_fills_out_and_submits_the_form(
        context: Context, actor_alias: str, *, form_name: str = None, check_captcha_dev_mode: bool = True
):
    generic_fill_out_and_submit_form(
        context, actor_alias, custom_details_table=context.table, form_name=form_name,
        check_captcha_dev_mode=check_captcha_dev_mode,
    )


@when('"{actor_alias}" downloads all visible PDFs')
def when_actor_downloads_all_visible_pdfs(context: Context, actor_alias: str):
    generic_download_all_pdfs(context, actor_alias)


@when('"{actor_alias}" submits the form')
def when_actor_submits_the_form(context: Context, actor_alias: str):
    generic_submit_form(context, actor_alias)


@when('"{actor_alias}" manually change the page language to "{preferred_language}"')
def when_actor_sets_lang_url_query_param(
        context: Context, actor_alias: str, preferred_language: str):
    generic_visit_current_page_with_lang_parameter(
        context, actor_alias, preferred_language)


@when('"{actor_alias}" opens "{ordinal_number}" news article')
def when_actor_opens_news_article(
        context: Context, actor_alias: str, ordinal_number: str):
    generic_open_news_article(context, actor_alias, ordinal_number)


@when('"{actor_alias}" decides to read about one of listed industries')
def when_actor_clicks_on_random_industry(context: Context, actor_alias: str):
    generic_click_on_random_industry(context, actor_alias)


@when('"{actor_alias}" chooses any available option except "{ignored}"')
def when_actor_chooses_random_form_option_except(
        context: Context, actor_alias: str, ignored: str):
    generic_pick_random_radio_option_and_submit(context, actor_alias, ignored)


@when('"{actor_alias}" navigates via "{via}"')
def given_actor_navigates_via_contact_us_options(
        context: Context, actor_alias: str, via: str):
    contact_us_navigate_through_options(context, actor_alias, via)


@when('"{actor_alias}" is on the "{page_name}" page')
def when_actor_is_on_page(context: Context, actor_alias: str, page_name: str):
    should_be_on_page(context, actor_alias, page_name)


@when('"{actor_alias}" decides to report a problem with the page')
def when_actor_reports_problem_with_page(context: Context, actor_alias: str):
    generic_report_problem_with_page(context, actor_alias)


@when('"{actor_alias}" searches for marketplaces in "{country}" to sell "{category}"')
def when_actor_looks_for_marketplace_using_countries_and_products(
        context: Context, actor_alias: str, country: str, category: str):
    soo_look_for_marketplace(context, actor_alias, country, category)


@when('"{actor_alias}" randomly selects a marketplace')
@when('"{actor_alias}" selects a random market')
def when_actor_selects_marketplace(context: Context, actor_alias: str):
    generic_click_on_random_marketplace(context, actor_alias)


@when('"{actor_alias}" submits the SOO contact-us form')
def when_actor_submits_soo_contact_us_form(
        context: Context, actor_alias: str):
    domestic_submit_soo_contact_us_form(
        context, actor_alias, custom_details_table=context.table
    )


@when('"{actor_alias}" searches using "{phrase}"')
def when_actor_search_for_phrase(
        context: Context, actor_alias: str, phrase: str):
    generic_search_for_phrase(context, actor_alias, phrase)


@when('"{actor_alias}" decides to find out more about random "{type_of}" result')
def when_actor_decides_to_find_out_more_about_result_type(
        context: Context, actor_alias: str, type_of: str):
    domestic_find_more_about_search_result_type(context, actor_alias, type_of)


@when('"{actor_alias}" should see search results page number "{page_num:d}" for "{phrase}"')
def then_actor_should_see_page_number(
        context: Context, actor_alias: str, page_num: int, phrase: str):
    domestic_search_finder_should_see_page_number(context, actor_alias, page_num)


@when('"{actor_alias}" triggers all GTM events defined for "{tagging_package}"')
def when_actor_triggers_all_gtm_events(
        context: Context, actor_alias: str, tagging_package: str
):
    generic_trigger_all_gtm_events(context, actor_alias, tagging_package)


@when('"{actor_alias}" triggers all GTM "{event_group}" events defined for "{tagging_package}"')
def when_actor_triggers_all_gtm_events(
        context: Context, actor_alias: str, event_group: str, tagging_package: str
):
    generic_trigger_all_gtm_events(
        context, actor_alias, tagging_package, event_group=event_group
    )


@when('"{actor_alias}" unfolds all elements in "{section_name}" section')
def when_actor_unfolds_elements_in_section(context: Context, actor_alias: str, section_name: str):
    generic_unfold_elements_in_section(context, actor_alias, section_name)


@when('"{actor_alias}" accepts all cookies')
def when_user_accepts_all_cookies(context: Context, actor_alias: str):
    generic_accept_all_cookies(context, actor_alias)


###############################################################################
# Currently unused but useful steps
###############################################################################


@when('"{actor_alias}" completes the registration and fake email verification process')
def when_actor_registers_fake_email_verification(context, actor_alias):
    registration_submit_form_and_verify_account(
        context, actor_alias, fake_verification=True)


@when('"{actor_alias}" signs out')
def when_actor_signs_out(context, actor_alias):
    sign_out(context, actor_alias)


@when('"{actor_alias}" completes the registration and real email verification process')
def when_actor_registers_real_email_verification(context, actor_alias):
    registration_submit_form_and_verify_account(
        context, actor_alias, fake_verification=False)


@when('"{actor_alias}" clears the cookies')
def when_actor_clears_the_cookies(context, actor_alias):
    clear_the_cookies(context, actor_alias)


@when('"{actor_alias}" signs in')
def when_actor_signs_in(context, actor_alias):
    sign_in(context, actor_alias)


@when('"{actor_alias}" searches for local trade office near "{post_code}"')
def when_actor_looks_for_trade_office(context: Context, actor_alias: str, post_code: str):
    office_finder_find_trade_office(context, actor_alias, post_code)


@when('"{actor_alias}" clicks the Menu button')
def when_actor_clicks_header_menu_button(context: Context, actor_alias: str):
    click_on_header_menu_button(context)


@when('"{actor_alias}" selects "{option}" from "{dropdown_name}" dropdown')
def when_actor_selects_form_option(
        context: Context, actor_alias: str, option: str, dropdown_name: str):
    generic_select_dropdown_option(context, actor_alias, dropdown_name, option)


@when('"{actor_alias}" opens up the language selector using her keyboard')
@when('"{actor_alias}" opens up the language selector using his keyboard')
def when_actor_opens_up_language_selector_with_keyboard(context, actor_alias):
    language_selector_open(context, actor_alias, with_keyboard=True)


@when('"{actor_alias}" decides to see related news articles by using one of the tags')
def when_actor_open_tag(context: Context, actor_alias: str):
    generic_open_any_tag(context, actor_alias)


@when('"{actor_alias}" decides to share the article via "{social_media}"')
def when_actor_shares_article(context, actor_alias, social_media):
    articles_share_on_social_media(context, actor_alias, social_media)

@when('"{actor_alias}" should be able to enter products "{products}" and country "{country}"')
def then_actor_should_be_able_to_enter_products_and_country(context, actor_alias, products, country):
    actor_should_be_able_to_enter_products_and_country(context, products, country)

@when('"{actor_alias}" decides to click on element "{element_name}" on page "{page_name}"')
def then_actor_decides_to_click_on_page_element(
        context, actor_alias, element_name, page_name):
    click_on_link_element_in_page(context, actor_alias, element_name, page_name=page_name)
