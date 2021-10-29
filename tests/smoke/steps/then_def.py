# -*- coding: utf-8 -*-
# flake8: noqa
# fmt: off
"""Then steps definitions."""
from behave import then
from behave.runner import Context

from steps.then_impl import (
    should_be_on_page,
    should_be_able_to_see_error_message,
    actor_decides_to_click_country_name_change,
    actor_decides_to_click_product_search_change,
    actor_decides_to_click_refine_interaction_change,
    actor_decides_to_click_trade_data_change,
    actor_decides_to_click_proceed,
    actor_should_be_able_to_see_comodity_code,
    actor_clicked_on_start_again,
    should_see_following_sections,
    should_see_sections,
    actor_should_be_able_to_see_confirmation_code_page_from_email_password_and_enter_code,
    actor_decides_to_enter_email_address_and_click_on_reset_password,
    actor_should_be_able_to_click_on_reset_password_link_from_email_password_and_enters_new_password_and_confirm,
    actor_should_be_able_to_enter_products_and_country,
    actor_should_be_able_to_enter_products,
    actor_decides_to_click_checkbox_yes_for_lesson_complete,
    actor_decides_to_click_continue_on_page,
    actor_decides_to_click_continue_for_number_of_times_until_it_reaches_required_page,
    actor_decides_to_click_open_case_study_in_all_lessons_for_number_of_times_until_it_reaches_required_page,
    actor_should_be_able_to_see_progress_bar_for_section,
    actor_decides_to_enter_text,
    actor_decides_to_enter_value,
    actor_decides_to_validate_entered_text,
    actor_decides_to_select_random_item_list_on_page,
    actor_decides_to_select_random_export_plan_on_page,
    actor_fill_business_objectives_details_on_page,
    actor_decides_to_delete_business_objectives_on_page,
    actor_decides_to_delete_country_details_on_page,
    actor_decides_to_click_checkbox_section_complete,
    actor_decides_to_select_random_checkbox_on_page,
    actor_decides_to_select_random_unit_list_on_page,
    actor_decides_to_select_random_payment_terms_on_page,
    actor_decides_to_select_random_time_from_list_on_page,
    actor_decides_to_select_random_currency_from_list_on_page,
    actor_decides_to_click_on_page_with_lesson_link,
    actor_decides_to_enter_value,
    actor_fill_document_details_on_page,
    actor_decides_to_delete_document_details_on_page,
    actor_enters_direct_costs_on_page,
    actor_enters_overhead_costs_on_page,
    actor_decides_to_select_funding_options_on_page,
    actor_decides_to_enter_product_name,
    actor_should_be_able_to_click_on_skipwalkthrough,
    actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months,
    actor_decides_to_click_on_search_again,
    actor_decides_to_click_on_product_and_search_again,
    actor_decides_to_click_on_select_save_random_products,
    actor_fill_trip_details_on_page,
    actor_decides_to_delete_trip_details_on_page,
    actor_decides_to_select_radio_button,
    actor_decides_to_select_random_product_on_page,
    actor_decides_to_enter_country_details,
    actor_decides_to_enter_country_name,
    generic_fill_out_and_submit_form,
    actor_fill_risk_details_on_page,
    actor_should_see_country_details_on_page,
    actor_should_see_last_visited_page_under_section_on_page,
    actor_decides_to_delete_route_to_market_on_page,
    actor_decides_to_delete_funding_options_on_page,
    actor_decides_to_validate_entered_country_details_and_change_from_the_list,
    actor_fills_out_and_submits_the_form,
    actor_decides_to_delete_risk_details_on_page,
    generic_should_be_on_one_of_the_pages,
    promo_video_check_watch_time,
    promo_video_should_not_see_modal_window,
    should_be_on_working_page,
    generic_should_see_expected_page_content,
    generic_should_see_form_choices,
    generic_should_see_message,
    generic_should_see_prepopulated_fields,
    header_check_favicon,
    header_check_logo,
    hpo_agent_should_receive_enquiry_email,
    hpo_should_receive_enquiry_confirmation_email,
    language_selector_should_see_it,
    marketplace_finder_should_see_marketplaces,
    menu_items_should_be_visible,
    office_finder_should_see_correct_office_details,
    pdf_check_expected_details,
    pdf_check_for_dead_links,
    share_page_should_be_prepopulated,
    share_page_via_email_should_have_article_details,
    should_be_on_page,
    should_be_on_page_or_be_redirected_to_page,
    should_not_see_sections,
    should_see_links_in_specific_location,
    should_see_page_in_preferred_language,
    should_see_sections,
    soo_contact_form_should_be_prepopulated,
    stats_and_tracking_elements_should_be_present,
    stats_and_tracking_elements_should_not_be_present,
    promo_video_check_watch_time,
    promo_video_should_not_see_modal_window,
    should_be_on_working_page,
    articles_should_be_on_share_page,
    domestic_search_finder_should_see_page_number,
    erp_should_receive_email_with_link_to_restore_saved_progress,
    # erp_should_see_correct_data_on_summary_page,
    erp_should_see_number_of_product_categories_to_expand,
    erp_should_see_number_of_product_codes_to_select,
    fas_buyer_should_be_signed_up_for_email_updates,
    fas_search_results_filtered_by_industries,
    form_check_state_of_element,
    forms_confirmation_email_should_not_be_sent,
    generic_a_notification_should_be_sent,
    generic_a_notification_should_be_sent_to_specific_dit_office,
    generic_a_notification_should_not_be_sent_to_specific_dit_office,
    generic_check_cookies,
    generic_check_gtm_datalayer_properties,
    generic_check_gtm_events,
    generic_contact_us_should_receive_confirmation_email,
    generic_contact_us_should_receive_confirmation_email_containing_message,
    generic_should_be_able_to_print,
    promo_video_check_watch_time,
    promo_video_should_not_see_modal_window,
    should_be_on_working_page,
)

from steps.when_impl import (
    visit_page,
    click_on_page_element,
    click_on_page_element_with_wait,
    actor_decides_to_check_random_radio_and_click_on_continue,
    actor_should_be_on_refine_or_tradedata_page,
    actor_select_random_data_click_continue_until_tradedata_or_checkanswers_page,
    actor_select_or_enter_random_data_click_continue_until_checkanswers_page,
    actor_decides_to_click_back_until_reaches_product_search_page,
    actor_select_random_data_click_continue_until_composition_page,
    actor_enter_random_composition_data_equal_to_hundred_percent,
    actor_enter_random_composition_data_not_equal_to_hundred_percent,
    promo_video_watch,
    promo_video_close,
    click_on_link_element_in_page,
    actor_decides_to_enter_email_address_and_click_login,

)

@then('"{actor_alias}" visited "{page_name}" page')
def given_actor_visits_page(context, actor_alias, page_name):
    visit_page(context, actor_alias, page_name)

@then('"{actor_alias}" should be on the "{page_name}" page if not be redirected to "{redirect_page}" page')
def then_actor_should_be_on_page_on_international_page(
        context, actor_alias, page_name, redirect_page):
    should_be_on_page_or_be_redirected_to_page(
        context, actor_alias, page_name, redirect_page
    )


@then('"{actor_alias}" should get to a working page')
def then_actor_should_be_on_working_page(context, actor_alias):
    should_be_on_working_page(context, actor_alias)


@then('"{actor_alias}" should be on the "{page_name}" page')
def then_actor_should_be_on_page(context, actor_alias, page_name):
    should_be_on_page(context, actor_alias, page_name)


@then('"{actor_alias}" decides to watch "{play_time:d}" seconds of the promotional video')
def when_actor_decides_to_watch_promo_video(
        context, actor_alias, *, play_time: int = None):
    promo_video_watch(context, actor_alias, play_time=play_time)


@then('"{actor_alias}" closes the window with promotional video')
def when_actor_decides_to_close_the_promotional_video(context, actor_alias):
    promo_video_close(context, actor_alias)


@then('"{actor_alias}" decides to select random treatment and click continue')
def then_actor_decides_to_fill_and_click_on_page_element(
        context, actor_alias, *, form_name: str = None):
    actor_decides_to_check_random_radio_and_click_on_continue(context, actor_alias)


@then('"{actor_alias}" should be on the refine or tradedata page')
def then_actor_should_be_on_refine_or_tradedata_page_after_click_continue_in_search(
        context, actor_alias, *, form_name: str = None):
    actor_should_be_on_refine_or_tradedata_page(context, actor_alias)


@then('"{actor_alias}" decides to click "{element_name}"')
def then_actor_decides_to_click_continue(
        context, actor_alias, element_name):
    click_on_page_element(context, actor_alias, element_name)


@then('"{actor_alias}" should be able to see error message "{error_message}" at element "{element_name}"')
def then_actor_should_be_able_to_see_error_message(
        context, actor_alias, error_message, element_name):
    should_be_able_to_see_error_message(context, actor_alias, element_name, error_message)


@then('"{actor_alias}" decides to click on "{element_name}"')
def then_actor_decides_to_click_on_page_element(
        context, actor_alias, element_name):
    click_on_page_element(context, actor_alias, element_name)


@then('"{actor_alias}" decides to click on section "{element_name}" on page "{page_name}"')
def then_actor_decides_to_click_on_page_element(
        context, actor_alias, element_name, page_name):
    click_on_page_element_with_wait(context, actor_alias, element_name, page_name=page_name)


@then('"{actor_alias}" decides to click on lesson link "{lesson_name}" on page "{page_name}"')
def then_actor_decides_to_click_on_lesson_link(
        context, actor_alias, lesson_name, page_name):
    actor_decides_to_click_on_page_with_lesson_link(context, actor_alias, lesson_name, page_name=page_name)


@then('"{actor_alias}" decides to click with wait "{wait_for_it}" on section "{element_name}" on page "{page_name}"')
def then_actor_decides_to_click_on_page_element_with_wait(
        context, actor_alias, element_name, page_name, wait_for_it):
    wait_or_not = True
    if wait_for_it == "True":
        wait_or_not = True
    else:
        wait_or_not = False
    click_on_page_element_with_wait(context, actor_alias, element_name, page_name=page_name, wait_for_it=wait_or_not)


@then('"{actor_alias}" decides to click on element "{element_name}" on page "{page_name}"')
def then_actor_decides_to_click_on_page_element(
        context, actor_alias, element_name, page_name):
    click_on_link_element_in_page(context, actor_alias, element_name, page_name=page_name)


@then('"{actor_alias}" decides to select random classification and click continue')
def then_actor_decides_to_fill_and_click_on_page_element(
        context, actor_alias, *, form_name: str = None):
    actor_decides_to_check_random_radio_and_click_on_continue(context, actor_alias)


@then(
    '"{actor_alias}" decides to select random data and click continue for maximum "{max_number_pages}" times until it reaches Tradedata or CheckYourAnswers page')
def then_actor_select_random_data_click_continue_until_tradedata_page(
        context, actor_alias, max_number_pages):
    actor_select_random_data_click_continue_until_tradedata_or_checkanswers_page(context, actor_alias, max_number_pages,
                                                                                 True, True)


@then(
    '"{actor_alias}" decides to select random data and click continue for maximum "{max_number_pages}" times until it reaches CheckYourAnswers page')
def then_actor_select_random_data_click_continue_until_tradedata_page(
        context, actor_alias, max_number_pages):
    actor_select_random_data_click_continue_until_tradedata_or_checkanswers_page(context, actor_alias, max_number_pages,
                                                                                 False, True)


@then(
    '"{actor_alias}" decides to select/enter random data and click continue for maximum "{max_number_pages}" times until it reaches CheckYourAnswers page')
def then_actor_select_random_data_click_continue_until_tradedata_page(
        context, actor_alias, max_number_pages):
    actor_select_or_enter_random_data_click_continue_until_checkanswers_page(context, actor_alias, max_number_pages)


@then(
    '"{actor_alias}" decides to select random data and click continue for maximum "{max_number_pages}" times until it reaches Tradedata page')
def then_actor_select_random_data_click_continue_until_tradedata_page(
        context, actor_alias, max_number_pages):
    actor_select_random_data_click_continue_until_tradedata_or_checkanswers_page(context, actor_alias, max_number_pages,
                                                                                 True, False)


@then(
    '"{actor_alias}" decides to select random treatment and click continue for maximum "{max_number_pages}" times until it reaches Composition page')
def then_actor_select_random_data_click_continue_until_tradedata_page(
        context, actor_alias, max_number_pages):
    actor_select_random_data_click_continue_until_composition_page(context, actor_alias, max_number_pages)


@then('"{actor_alias}" decides to enter random composition percents Equal to 100 and click "{element_name}"')
def then_actor_enter_random_composition_data_equal_to_hundred_percent(
        context, actor_alias, element_name):
    actor_enter_random_composition_data_equal_to_hundred_percent(context, actor_alias)
    click_on_page_element(context, actor_alias, element_name)


@then('"{actor_alias}" decides to click Country Name "{element_name}"')
def then_actor_decides_to_click_country_name_change(
        context, actor_alias, element_name):
    actor_decides_to_click_country_name_change(context, actor_alias, element_name)


@then('"{actor_alias}" decides to click Search term "{element_name}"')
def then_actor_decides_to_click_product_search_change(
        context, actor_alias, element_name):
    actor_decides_to_click_product_search_change(context, actor_alias, element_name)


@then('"{actor_alias}" decides to click random Refinement "{element_name}"')
def then_actor_decides_to_click_random_refine_change(
        context, actor_alias, element_name):
    actor_decides_to_click_refine_interaction_change(context, actor_alias, element_name)


@then('"{actor_alias}" decides to click proceed "{element_name}"')
def then_actor_decides_to_click_proceed(
        context, actor_alias, element_name):
    actor_decides_to_click_proceed(context, actor_alias, element_name)


@then('"{actor_alias}" should be able to see commodity code "{code}" for "{product}"')
def then_actor_should_be_able_to_see_comodity_code(
        context, actor_alias, code, product):
    actor_should_be_able_to_see_comodity_code(context, actor_alias, code, product)


@then('"{actor_alias}" decides to click on "{keyword_to_click}" to go to Home')
def then_actor_clicked_on_start_again(
        context, actor_alias, keyword_to_click):
    actor_clicked_on_start_again(context, actor_alias, keyword_to_click)


@then('"{actor_alias}" decides to enter random composition percents NotEqual to 100 and click "{element_name}"')
def then_actor_enter_random_composition_data_not_equal_to_hundred_percent(
        context, actor_alias, element_name):
    actor_enter_random_composition_data_not_equal_to_hundred_percent(context, actor_alias)
    click_on_page_element(context, actor_alias, element_name)


@then(
    '"{actor_alias}" decides to click on "{element_name}" for maximum "{max_number_pages}" times until it reaches "{page_name}" page')
def then_actor_decides_to_click_country_name_change(
        context, actor_alias, element_name, max_number_pages, page_name):
    actor_decides_to_click_back_until_reaches_product_search_page(context, actor_alias, element_name, max_number_pages,
                                                                  page_name)


@then('"{actor_alias}" should see following sections')
def then_should_see_sections(context, actor_alias):
    should_see_following_sections(context, actor_alias, sections_table=context.table)


@then(
    '"{actor_alias}" should be able to see confirmation code page from email "{email_address}", password "{password}" and enter code')
def then_should_be_able_to_see_confirmation_code_page_from_email_password_and_enter_code(context, actor_alias,
                                                                                         email_address, password):
    actor_should_be_able_to_see_confirmation_code_page_from_email_password_and_enter_code(context, email_address,
                                                                                          password)


@then('"{actor_alias}" decides to enter emailaddress "{email_address}" and click on reset password')
def then_actor_decides_to_enter_email_address_and_click_on_reset_password(
        context, actor_alias, email_address):
    actor_decides_to_enter_email_address_and_click_on_reset_password(context, email_address)


@then(
    '"{actor_alias}" should be able to click on reset password link from email "{email_address}", "{password}" and enters new password "{new_password}" and confirm')
def then_actor_should_be_able_to_click_on_reset_password_link_from_email_password_and_enters_new_password_and_confirm(
        context, actor_alias, email_address, password, new_password):
    actor_should_be_able_to_click_on_reset_password_link_from_email_password_and_enters_new_password_and_confirm(
        context, actor_alias, email_address, password, new_password)


@then('"{actor_alias}" should be able to enter products "{products}" and country "{country}"')
def then_actor_should_be_able_to_enter_products_and_country(context, actor_alias, products, country):
    actor_should_be_able_to_enter_products_and_country(context, products, country)


@then('"{actor_alias}" should be able to enter products "{products}"')
def then_actor_should_be_able_to_enter_products(context, actor_alias, products):
    actor_should_be_able_to_enter_products(context, products)


@then('"{actor_alias}" decides to click checkbox Yes and click continue on "{page_name}"')
def then_actor_decides_to_click_on_lesson_complete_and_click_continue(context, actor_alias, page_name):
    actor_decides_to_click_checkbox_yes_for_lesson_complete(context, page_name)
    click_on_page_element(context, actor_alias, "Continue learning", page_name=page_name)


@then('"{actor_alias}" decides to click checkbox Yes on "{page_name}"')
def then_actor_decides_to_click_on_lesson_complete_and_click_continue(context, actor_alias, page_name):
    actor_decides_to_click_checkbox_yes_for_lesson_complete(context, page_name)


@then('"{actor_alias}" decides to click section complete on "{page_name}"')
def then_actor_decides_to_click_on_section_complete_and_click_continue(context, actor_alias, page_name):
    actor_decides_to_click_checkbox_section_complete(context, page_name)


# @then('"{actor_alias}" decides to click "{element_name}"')
# def then_actor_decides_to_click_bottom_back(context, actor_alias,element_name):
#     actor_decides_to_click_on_bottom_back(context, actor_alias,element_name)

@then(
    '"{actor_alias}" decides to click continue for maximum "{max_number_pages}" times from page "{from_page_name}" until it reaches "{page_name}"')
def then_actor_decides_to_click_continue_for_number_of_times_until_it_reaches_required_page(
        context, actor_alias, max_number_pages, from_page_name, page_name):
    actor_decides_to_click_continue_for_number_of_times_until_it_reaches_required_page(context, actor_alias,
                                                                                       max_number_pages, from_page_name,
                                                                                       page_name)


@then('"{actor_alias}" should be able to see progress bar for section "{element_name}" on "{page_name}" page')
def then_actor_should_be_able_to_see_progress_bar_for_section(
        context, actor_alias, element_name, page_name):
    actor_should_be_able_to_see_progress_bar_for_section(context, actor_alias, element_name, page_name)


@then('"{actor_alias}" decides to enter text at "{element_name}" on page "{page_name}"')
def then_actor_decides_to_enter_text(context, actor_alias, element_name, page_name):
    actor_decides_to_enter_text(context, element_name, page_name)


@then('"{actor_alias}" decides to validate entered text at "{element_name}" on page "{page_name}"')
def then_actor_decides_to_validate_entered_text(context, actor_alias, element_name, page_name):
    actor_decides_to_validate_entered_text(context, element_name, page_name)


@then('"{actor_alias}" decides to select random item for "{element_name}" on page "{page_name}"')
def then_actor_decides_to_select_random_item_list_on_page(context, actor_alias, element_name, page_name):
    actor_decides_to_select_random_item_list_on_page(context, actor_alias, element_name, page_name)

@then('"{actor_alias}" decides to select random item for payment terms on page "{page_name}"')
def then_actor_decides_to_select_random_payment_terms_on_page(context, actor_alias, page_name):
    actor_decides_to_select_random_payment_terms_on_page(context, actor_alias, page_name)

@then('"{actor_alias}" decides to select random unit for "{element_name}" on page "{page_name}"')
def then_actor_decides_to_select_random_unit_list_on_page(context, actor_alias, element_name, page_name):
    actor_decides_to_select_random_unit_list_on_page(context, actor_alias, element_name, page_name)

@then('"{actor_alias}" decides to select random time from "{element_name}" on page "{page_name}"')
def then_actor_decides_to_select_random_time_from_list_on_page(context, actor_alias, element_name, page_name):
    actor_decides_to_select_random_time_from_list_on_page(context, actor_alias, element_name, page_name)

@then('"{actor_alias}" decides to select random currency in "{element_name}" on page "{page_name}"')
def then_actor_decides_to_select_random_currency_from_list_on_page(context, actor_alias, element_name, page_name):
    actor_decides_to_select_random_currency_from_list_on_page(context, actor_alias, element_name, page_name)


@then('"{actor_alias}" fill business objective details on page "{page_name}"')
def then_actor_fill_business_objectives_details_on_page(context, actor_alias, page_name,element_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_fill_business_objectives_details_on_page(context, actor_alias, row["Position"], row["Objectives"], row["Owner"],
                                                       row["PlannedReviews"], page_name,element_name)


@then('"{actor_alias}" decides to delete business objectives on page "{page_name}"')
def then_actor_decides_to_delete_business_objectives_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_business_objectives_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" decides to delete risk details on page "{page_name}"')
def then_actor_decides_to_delete_risk_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_risk_details_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" fill risk details on page "{page_name}"')
def then_actor_fill_risk_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_fill_risk_details_on_page(context, actor_alias, row["Position"], row["Risktext"], row["Contingencyplan"],
                                        page_name)


@then('"{actor_alias}" decides to delete country details on page "{page_name}"')
def then_actor_decides_to_delete_country_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_country_details_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" decides to select random checkbox "{element_name}" on page "{page_name}"')
def then_actor_decides_to_select_random_checkbox_on_page(context, actor_alias, element_name, page_name):
    actor_decides_to_select_random_checkbox_on_page(context, actor_alias, element_name, page_name)


@then('"{actor_alias}" decides to enter value in "{element_name}" on page "{page_name}"')
def then_actor_decides_to_enter_value(context, actor_alias, element_name, page_name):
    actor_decides_to_enter_value(context, element_name, page_name)


@then('"{actor_alias}" fill document details on page "{page_name}"')
def then_actor_fill_document_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_fill_document_details_on_page(context, actor_alias, row["Position"], row["DocumentName"], row["Notes"],
                                            page_name)


@then('"{actor_alias}" decides to delete document details on page "{page_name}"')
def then_actor_decides_to_delete_document_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_document_details_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" enters direct costs price on page "{page_name}"')
def then_actor_enters_direct_costs_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_enters_direct_costs_on_page(context, actor_alias, row["Productcost"], row["Labourcost"],
                                          row["Additionalmargin"], page_name)


@then('"{actor_alias}" enters overhead costs price on page "{page_name}"')
def then_actor_enters_overhead_costs_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_enters_overhead_costs_on_page(context, actor_alias, row["Product Adaptation"],
                                            row["Freight and Logistics"], row["Agent and Distribution fees"],
                                            row["Marketing"], row["Insurance"], page_name)


@then('"{actor_alias}" decides to select random funding options on page "{page_name}"')
def then_actor_decides_to_select_random_option_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_select_funding_options_on_page(context, actor_alias, row["Position"], row["Amount"], page_name)


@then('"{actor_alias}" decides to enter product name "{product_name}" on page "{page_name}"')
def then_actor_decides_to_enter_product_name(
        context, actor_alias, product_name, *, form_name: str = None, page_name):
    actor_decides_to_enter_product_name(context, actor_alias, product_name, page_name)


@then('"{actor_alias}" decides to enter country name "{country_name}" on the "{page_name}" Page')
def then_actor_decides_to_enter_country_name(
        context, actor_alias, country_name, *, form_name: str = None, page_name):
    actor_decides_to_enter_country_name(context, actor_alias, country_name, page_name)


@then('"{actor_alias}" should be able to click on SkipWalkthrough')
def then_actor_should_be_able_to_click_on_skipwalkthrough(
        context, actor_alias):
    actor_should_be_able_to_click_on_skipwalkthrough(context, actor_alias)


@then('"{actor_alias}" should be able to click on I have exported in the last 12 months')
def when_actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months(
        context, actor_alias):
    actor_should_be_able_to_click_on_i_have_exported_in_the_last_12_months(context, actor_alias)


@then('"{actor_alias}" decides to click on Search again on the "{page_name}" page')
def then_actor_decides_to_click_on_search_again(context, actor_alias, page_name):
    actor_decides_to_click_on_search_again(context, actor_alias, page_name)


@then('"{actor_alias}" decides to click on Product and Search again for "{product_name}" on the "{page_name}" Page')
def then_actor_decides_to_click_on_product_and_search_again(context, actor_alias, product_name, page_name):
    actor_decides_to_click_on_product_and_search_again(context, actor_alias, product_name, page_name)


@then('"{actor_alias}" decides to click on select and save random product options on the "{page_name}" page')
def then_actor_decides_to_click_on_select_save_random_products(context, actor_alias, page_name):
    actor_decides_to_click_on_select_save_random_products(context, actor_alias, page_name)


@then('"{actor_alias}" fill trip details on page "{page_name}"')
def then_actor_fill_trip_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_fill_trip_details_on_page(context, actor_alias, row["Position"], row["TripName"], page_name)


@then('"{actor_alias}" decides to delete trip details on page "{page_name}"')
def then_actor_decides_to_delete_trip_details_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_trip_details_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" decides to select radio button "{element_name}" on page "{page_name}"')
def then_actor_decides_to_select_radio_button(context, actor_alias, element_name, page_name):
    actor_decides_to_select_radio_button(context, element_name, page_name)


@then(
    '"{actor_alias}" decides to enter maximum "{country_max}" country names with display "{display_tab_count}" tabs on page "{page_name}"')
def then_actor_decides_to_enter_country_details(context, actor_alias, country_max, display_tab_count, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_enter_country_details(context, actor_alias, row["CountryName"]
                                               , country_place_number=row["CountryPlaceNumber"]
                                               , country_max=country_max
                                               , display_tab_count=display_tab_count
                                               , page_name=page_name)


@then('"{actor_alias}" fills out and submits the form')
def when_actor_fills_out_and_submits_the_form(
        context: Context, actor_alias: str, *, form_name: str = None, check_captcha_dev_mode: bool = True
):
    generic_fill_out_and_submit_form(
        context, actor_alias, custom_details_table=context.table, form_name=form_name,
        check_captcha_dev_mode=check_captcha_dev_mode,
    )


@then('"{actor_alias}" fills out and submits the contact us form')
def then_actor_fills_out_and_submits_the_form(
        context: Context, actor_alias: str, *, page_name):
    actor_fills_out_and_submits_the_form(context, actor_alias, page_name)


@then('"{actor_alias}" should see country details on page "{page_name}"')
def then_actor_should_see_country_details_on_page(context, actor_alias, page_name):
    actor_should_see_country_details_on_page(context, actor_alias, page_name, on_all_tabs=False)


@then('"{actor_alias}" should see country details on all tabs on page "{page_name}"')
def then_actor_should_see_country_details_on_all_tabs_on_page(context, actor_alias, page_name):
    actor_should_see_country_details_on_page(context, actor_alias, page_name, on_all_tabs=True)


@then('"{actor_alias}" should see "{text_to_see}" text under section "{section_name}" on page "{page_name}"')
def then_actor_should_see_last_visited_page_under_section_on_page(context, actor_alias, text_to_see, section_name,
                                                                  page_name):
    actor_should_see_last_visited_page_under_section_on_page(context, actor_alias, text_to_see, section_name, page_name)


@then('"{actor_alias}" decides to delete route to market on page "{page_name}"')
def then_actor_decides_to_delete_route_to_market_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_route_to_market_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" decides to delete funding options on page "{page_name}"')
def then_actor_decides_to_delete_funding_options_on_page(context, actor_alias, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_delete_funding_options_on_page(context, actor_alias, row["Position"], page_name)


@then('"{actor_alias}" decides to validate entered country details and change from the list "{page_name}"')
def then_actor_decides_to_validate_entered_country_details_and_change_from_the_list(context, actor_alias, country_max,
                                                                                    list_selection, page_name):
    input_data_table = context.table
    for row in input_data_table:
        actor_decides_to_validate_entered_country_details_and_change_from_the_list(context, actor_alias,
                                                                                   row["CountryName"]
                                                                                   , country_place_number=row[
                "CountryPlaceNumber"]
                                                                                   , country_max=country_max
                                                                                   , list_selection=list_selection
                                                                                   , page_name=page_name)


@then('"{actor_alias}" should be on one of the "{expected_pages}" pages')
def then_actor_should_be_on_one_of_the_pages(context: Context, actor_alias: str, expected_pages: str):
    generic_should_be_on_one_of_the_pages(context, actor_alias, expected_pages)


@then(
    '"{actor_alias}" should be able to watch at least first "{expected_watch_time:d}" seconds of the promotional video')
def then_actor_should_watch_the_promo_video(
        context, actor_alias, expected_watch_time: int):
    promo_video_check_watch_time(context, actor_alias, expected_watch_time)


@then('"{actor_alias}" should not see the window with promotional video')
def then_actor_should_not_see_video_modal_window(context, actor_alias):
    promo_video_should_not_see_modal_window(context, actor_alias)


@then('"{actor_alias}" should see the correct favicon')
def then_actor_should_see_correct_favicon(context, actor_alias):
    header_check_favicon(context, actor_alias)


@then('"{actor_alias}" should see content specific to "{industry_name}" page')
def fas_then_actor_should_see_expected_content(
        context: Context, actor_alias: str, industry_name: str):
    generic_should_see_expected_page_content(context, actor_alias, industry_name)


@then('"{actor_alias}" should see search results filtered by "{industry_names}" industry')
def fas_should_see_filtered_search_results(
        context: Context, actor_alias: str, industry_names: str):
    fas_search_results_filtered_by_industries(
        context, actor_alias, industry_names.split(", "))


@then('following web statistics analysis or tracking elements should NOT be present')
def then_stats_and_tracking_elements_should_be_present(context: Context):
    stats_and_tracking_elements_should_not_be_present(context, context.table)


@then('following web statistics analysis or tracking elements should be present')
def then_stats_and_tracking_elements_should_be_present(context: Context):
    stats_and_tracking_elements_should_be_present(context, context.table)


@then('"{actor_alias}" should receive "{subject}" email containing "{message}" message')
def then_should_receive_confirmation_email_from_govnotify(
        context: Context, actor_alias: str, subject: str, message: str):
    generic_contact_us_should_receive_confirmation_email_containing_message(
        context, actor_alias, subject, message=message
    )


@then('"{actor_alias}" should receive an "{subject}" confirmation email')
@then('"{actor_alias}" should receive a "{subject}" confirmation email')
@then('"{actor_alias}" should receive "{subject}" confirmation email from "{service}"')
@then('"{actor_alias}" should receive "{subject}" confirmation email')
@then('"{actor_alias}" should receive "{subject}" email')
def then_should_receive_confirmation_email_from_govnotify(
        context: Context, actor_alias: str, subject: str, *, service: str = None):
    generic_contact_us_should_receive_confirmation_email(
        context, actor_alias, subject, service=service
    )


@then('"{actor_alias}" should receive HPO enquiry confirmation email')
def then_should_receive_hpo_enquiry_confirmation_email(
        context: Context, actor_alias: str):
    hpo_should_receive_enquiry_confirmation_email(context, actor_alias)


@then('HPO Agent should receive HPO enquiry email from "{actor_alias}"')
def then_hpo_agent_should_receive_hpo_enquiry_email(
        context: Context, actor_alias: str):
    hpo_agent_should_receive_enquiry_email(context, actor_alias)


@then('"{actor_alias}" should see that "{element}" in the form is "{state}"')
def then_actor_should_see_form_element_in_specific_stage(
        context: Context, actor_alias: str, element: str, state: str):
    form_check_state_of_element(context, actor_alias, element, state)


@then('"{actor_alias}" should see correct details in every downloaded PDF')
def then_pdfs_should_contain_expected_details(
        context: Context, actor_alias: str):
    pdf_check_expected_details(context, actor_alias, context.table)


@then('there should not be any dead links in every downloaded PDF')
def then_should_not_see_dead_links_in_pdf(context: Context):
    pdf_check_for_dead_links(context)


@then('"{actor_alias}" should see error message saying that mandatory fields are required')
@then('"{actor_alias}" should see that she can "{message}"')
@then('"{actor_alias}" should see that he can "{message}"')
@then('"{actor_alias}" should see "{message}" on the page')
@then('"{actor_alias}" should see "{message}" message')
def then_should_see_message(context: Context, actor_alias: str, *, message: str = None):
    generic_should_see_message(context, actor_alias, message=message)


@then('"{actor_alias}" should see following form choices')
@then('"{actor_alias}" should see following options')
def then_should_see_form_choices(context: Context, actor_alias: str):
    generic_should_see_form_choices(context, actor_alias, context.table)


@then('"{actor_alias}" should see contact details for "{trade_office}" office in "{city}"')
def then_should_see_correct_trade_office_details(
        context: Context, actor_alias: str, trade_office: str, city: str):
    office_finder_should_see_correct_office_details(
        context, actor_alias, trade_office, city)


@then('"{actor_alias}" should not receive a confirmation email')
def then_confirmation_email_should_not_be_sent(context: Context, actor_alias: str):
    forms_confirmation_email_should_not_be_sent(context, actor_alias)


@then('"{actor_alias}" should receive email with a new confirmation code')
def then_actor_should_get_verification_code(context: Context, actor_alias: str):
    generic_get_verification_code(context, actor_alias, resent_code=True)


@then('"{actor_alias}" should receive email confirmation code')
def then_actor_should_get_verification_code(context: Context, actor_alias: str):
    generic_get_verification_code(context, actor_alias)


@then('"{actor_alias}" should see marketplaces which operate globally or in "{country}"')
def then_actor_should_see_expected_marketplaces(
        context: Context, actor_alias: str, country: str):
    marketplace_finder_should_see_marketplaces(context, actor_alias, country)


@then('"{actor_alias}" should see search results page number "{page_num:d}" for "{phrase}"')
def then_actor_should_see_page_number(
        context: Context, actor_alias: str, page_num: int, phrase: str):
    domestic_search_finder_should_see_page_number(context, actor_alias, page_num)


@then('"{actor_alias}" should see form fields populated with his company details')
def then_form_should_be_prepopulated(context: Context, actor_alias: str):
    soo_contact_form_should_be_prepopulated(context, actor_alias)


@then('"{actor_alias}" should see following fields populated with values provided on other forms')
def then_form_should_be_prepopulated_w_personal(context: Context, actor_alias: str):
    generic_should_see_prepopulated_fields(context, actor_alias, context.table)


@then("Google Tag Manager properties should be set to proper values")
def step_check_gtm_data_layer_properties(context: Context):
    generic_check_gtm_datalayer_properties(context, context.table)


@then("following GTM events should be registered")
def then_expected_gtm_events_should_be_registered(context: Context):
    generic_check_gtm_events(context)


@then("following cookies should be set")
def then_expected_cookies_should_be_set(context: Context):
    generic_check_cookies(context)


@then('"{actor_alias}" should see the menu items')
def then_actor_should_see_menu_items(context: Context, actor_alias: str):
    menu_items_should_be_visible(context)


@then('an "{action}" notification entitled "{subject}" should be sent to "{actor_alias}"')
@then('a "{action}" notification entitled "{subject}" should be sent to "{actor_alias}"')
def then_notification_should_be_sent(
        context: Context, action: str, subject: str, actor_alias: str
):
    generic_a_notification_should_be_sent(
        context, actor_alias, action, subject
    )


@then('an email notification about "{actor_alias}"\'s enquiry should be send to "{mailbox_name}"')
def then_notification_should_be_sent_to_specific_dit_office(
        context: Context, actor_alias: str, mailbox_name: str
):
    generic_a_notification_should_be_sent_to_specific_dit_office(
        context, actor_alias, mailbox_name
    )


@then('an email notification about "{actor_alias}"\'s enquiry should NOT be send to "{mailbox_name}"')
def then_notification_should_be_sent_to_specific_dit_office(
        context: Context, actor_alias: str, mailbox_name: str
):
    generic_a_notification_should_not_be_sent_to_specific_dit_office(
        context, actor_alias, mailbox_name
    )


@then('"{actor_alias}" should receive an email with a link to restore saved ERP session')
def then_should_receive_email_from_govnotify_with_link_to_restore_saved_erp_session(
        context: Context, actor_alias: str
):
    erp_should_receive_email_with_link_to_restore_saved_progress(context, actor_alias)


@then('"{actor_alias}" should be able to print out a copy of submitted form')
def then_actor_should_be_able_to_print(context: Context, actor_alias: str):
    generic_should_be_able_to_print(context, actor_alias)


@then('"{actor_alias}" should see "{number_of_product_codes}" product code(s) to select')
def then_erp_user_should_see_expected_number_of_product_codes_to_select(
        context: Context, actor_alias: str, number_of_product_codes: str
):
    erp_should_see_number_of_product_codes_to_select(
        context, actor_alias, number_of_product_codes
    )


@then('"{actor_alias}" should see "{number_of_product_codes}" product category(ies) to expand')
def then_erp_user_should_see_expected_number_of_product_categories_to_compare(
        context: Context, actor_alias: str, number_of_product_codes: str
):
    erp_should_see_number_of_product_categories_to_expand(
        context, actor_alias, number_of_product_codes
    )


@then('"{actor_alias}" should be able to resume giving feedback as "{user_type}" from "{resume_from}" page')
def then_erp_resume_giving_feedback(
        context: Context, actor_alias: str, user_type: str, resume_from: str
):
    erp_follow_user_flow(context, actor_alias, user_type, resume_from=resume_from)


# @then('"{actor_alias}" should see correct data shown on the summary page')
# def then_erp_should_see_correct_data_on_summary(context: Context, actor_alias: str):
#     erp_should_see_correct_data_on_summary_page(context, actor_alias)


@then('"{actor_alias}" should be signed up for email updates of the latest UK companies in selected industry')
def then_buyer_should_be_signed_up_for_email_updates(context: Context, actor_alias: str):
    fas_buyer_should_be_signed_up_for_email_updates(context, actor_alias)


@then('"{actor_alias}" should see correct "{logo_name}" logo')
def then_actor_should_see_correct_logo(context, actor_alias, logo_name):
    header_check_logo(context, actor_alias, logo_name)


@then('"{actor_alias}" should see the language selector')
def then_actor_should_see_language_selector(context, actor_alias):
    language_selector_should_see_it(context, actor_alias)


@then('"{actor_alias}" should see the page in "{preferred_language}"')
def then_page_language_should_be(context, actor_alias, preferred_language):
    should_see_page_in_preferred_language(
        context, actor_alias, preferred_language)


@then('"{actor_alias}" should see links to following "{section}" categories in "{location}"')
def then_should_see_links_to_services(
        context, actor_alias, section, location):
    should_see_links_in_specific_location(
        context, actor_alias, section, context.table, location)


@then('"{actor_alias}" should be taken to a new tab with the "{social_media}" share page opened')
def then_actor_should_be_on_share_page(context, actor_alias, social_media):
    articles_should_be_on_share_page(context, actor_alias, social_media)


@then('"{actor_alias}" should see that "{social_media}" share link contains link to the article')
@then(
    '"{actor_alias}" should see that "{social_media}" share page has been pre-populated with message and the link to the article')
def then_share_page_should_be_prepopulated(context, actor_alias, social_media):
    share_page_should_be_prepopulated(context, actor_alias, social_media)


@then(
    '"{actor_alias}" should see that the share via email link will pre-populate the message subject and body with Article title and URL')
def then_check_share_via_email_link(context, actor_alias):
    share_page_via_email_should_have_article_details(context, actor_alias)


@then('"{actor_alias}" should not see following sections')
@then('"{actor_alias}" should not see following section')
def then_should_not_see_sections(context, actor_alias):
    should_not_see_sections(context, actor_alias, sections_table=context.table)


@then(
    '"{actor_alias}" decides to click open "{element_name}" in all lessons "{max_number_pages}" times from page "{from_page_name}" until it reaches "{page_name}"')
def then_actor_decides_to_click_open_case_study_in_all_lessons_for_number_of_times_until_it_reaches_required_page(
        context, actor_alias, max_number_pages, from_page_name, page_name, element_name):
    actor_decides_to_click_open_case_study_in_all_lessons_for_number_of_times_until_it_reaches_required_page(context,
                                                                                                             actor_alias,
                                                                                                             max_number_pages,
                                                                                                             from_page_name,
                                                                                                             page_name,
                                                                                                             element_name)


@then('"{actor_alias}" decides to enter email address "{email_address}", password "{password}" and click Login')
def when_actor_decides_to_enter_email_address_and_click_login(
        context, actor_alias, email_address, password):
    actor_decides_to_enter_email_address_and_click_login(context, actor_alias, email_address, password)

@then('"{actor_alias}" decides to click continue on "{page_name}" page')
def then_actor_decides_to_click_continue_on_page(
        context, actor_alias, page_name):
    actor_decides_to_click_continue_on_page(context, page_name)

@then('"{actor_alias}" decides to select random product on "{page_name}" page')
def then_actor_decides_to_select_random_product_on_page(
        context, actor_alias, page_name):
    actor_decides_to_select_random_product_on_page(context, page_name)

@then('"{actor_alias}" decides to select random export plan on page "{page_name}"')
def then_actor_decides_to_select_random_export_plan_on_page(context, actor_alias, page_name):
    # input_data_table = context.table
    # for row in input_data_table:
    actor_decides_to_select_random_export_plan_on_page(context, actor_alias, page_name)
