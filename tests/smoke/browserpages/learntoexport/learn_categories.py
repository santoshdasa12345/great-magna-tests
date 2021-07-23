import logging
import random
import time
from types import ModuleType
from typing import List, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType, common_selectors
from great_magna_tests_shared.utils import check_url_path_matches_template
from browserpages.common_actions import (
    Actor,
    Selector,
    assertion_msg,
    check_for_sections,
    check_if_element_is_not_present,
    check_if_element_is_visible,
    check_url,
    find_element,
    find_selector_by_name,
    find_elements,
    go_to_url,
    pick_option,
    is_element_present,
    submit_form,
    check_random_radio,
    take_screenshot,
    wait_for_page_load_after_action,
    fill_out_input_fields,
    fill_out_email_address

)

NAME = "Learn Categories"
SERVICE = Service.LEARNTOEXPORT
TYPE = PageType.LESSON
URL = URLs.GREAT_MAGNA_LEARN_TO_EXPORT.absolute
PAGE_TITLE = "Learn Categories"

NAMES = [NAME, "new-lesson-added"]
SubURLs = {
    "learn categories": URL,
    "new-lesson-added": URLs.GREAT_MAGNA_LESSONS_NEW_LESSON_ADDED.absolute_template,
    # "lookup commodity code": URLs.LOOK_UP_COMMODITY_CONFIRMATION.absolute_template

    # "market-research": URLs.GREAT_MAGNA_LESSONS_IDENTIFY_OPPORTUNITIES_AND_RESEARCH_THE_MARKET.absolute_template,
    "opportunity-right-you": URLs.GREAT_MAGNA_LESSONS_CHOOSING_THE_RIGHT_EXPORT_OPPORTUNITIES.absolute_template,
    "move-accidental-exporting-strategic-exporting": URLs.GREAT_MAGNA_LESSONS_MOVE_FROM_ACCIDENTAL_EXPORTING_TO_STRATEGIC_EXPORTING.absolute_template,
    "-market-research": URLs.GREAT_MAGNA_LESSONS_IN_MARKET_RESEARCH.absolute_template,
    "online-research": URLs.GREAT_MAGNA_LESSONS_ONLINE_RESEARCH.absolute_template,
    "quantifying-customer-demand-how-much-might-you-sell": URLs.GREAT_MAGNA_LESSONS_WORK_OUT_CUSTOMER_DEMAND.absolute_template,
    "understand-your-market-size-and-its-segments": URLs.GREAT_MAGNA_LESSONS_UNDERSTAND_YOUR_MARKET_SIZE_AND_ITS_SEGMENTS.absolute_template,
    "understanding-competitor-market-share-and-pricing": URLs.GREAT_MAGNA_LESSONS_UNDERSTANDING_THE_COMPETITION.absolute_template,
    "research-current-market-conditions": URLs.GREAT_MAGNA_LESSONS_RESEARCH_CURRENT_MARKET_CONDITIONS.absolute_template,
    "how-assess-ease-entry-new-market": URLs.GREAT_MAGNA_LESSONS_EASE_OF_ENTRY_INTO_A_NEW_MARKET.absolute_template,
    "local-infrastructure": URLs.GREAT_MAGNA_LESSONS_RESEARCH_LOCAL_INFRASTRUCTURE.absolute_template,
    "understand-how-you-may-need-adapt-your-product-meet-international-standards": URLs.GREAT_MAGNA_LESSONS_ADAPTING_YOUR_PRODUCT_OR_SERVICE.absolute_template,
    "information-you-need-choose-target-country": URLs.GREAT_MAGNA_LESSONS_INFORMATION_YOU_NEED_TO_CHOOSE_A_TARGET_COUNTRY.absolute_template,
    "plot-market-demand-against-ease-entry": URLs.GREAT_MAGNA_LESSONS_CUSTOMER_DEMAND_VS_EASE_OF_ENTRY.absolute_template,
    "prepare-sell-new-country": URLs.GREAT_MAGNA_LESSONS_PREPARE_TO_SELL_INTO_A_NEW_COUNTRY.absolute_template,
    "choose-right-route-market": URLs.GREAT_MAGNA_LESSONS_CHOOSE_THE_RIGHT_ROUTE_TO_MARKET.absolute_template,
    "sell-direct-your-customer": URLs.GREAT_MAGNA_LESSONS_SELLING_DIRECT_TO_YOUR_CUSTOMER.absolute_template,
    "international-e-commerce": URLs.GREAT_MAGNA_LESSONS_SELLING_WITH_INTERNATIONAL_E_COMMERCE.absolute_template,
    "set-joint-ventures-abroad": URLs.GREAT_MAGNA_LESSONS_SETTING_UP_JOINT_VENTURES_ABROAD.absolute_template,
    "setting-franchise-abroad": URLs.GREAT_MAGNA_LESSONS_SETTING_UP_A_FRANCHISE_ABROAD.absolute_template,
    "decide-whether-use-licensing": URLs.GREAT_MAGNA_LESSONS_USING_LICENSING.absolute_template,
    "how-set-business-abroad": URLs.GREAT_MAGNA_LESSONS_SETTING_UP_A_BUSINESS_ABROAD.absolute_template,
    "when-use-agent-or-distributor": URLs.GREAT_MAGNA_LESSONS_USING_AN_AGENT_OR_DISTRIBUTOR.absolute_template,
    "understand-local-business-culture-your-target-market": URLs.GREAT_MAGNA_LESSONS_UNDERSTAND_THE_LOCAL_BUSINESS_CULTURE.absolute_template,
    "understanding-product-liability": URLs.GREAT_MAGNA_LESSONS_UNDERSTAND_PRODUCT_LIABILITY.absolute_template,
    "protect-your-intellectual-property-abroad": URLs.GREAT_MAGNA_LESSONS_PROTECT_YOUR_INTELLECTUAL_PROPERTY_ABROAD.absolute_template,
    "how-prepare-trade-mission": URLs.GREAT_MAGNA_LESSONS_PREPARING_FOR_A_TRADE_MISSION.absolute_template,
    "how-prepare-trade-show-attendee": URLs.GREAT_MAGNA_LESSONS_PREPARING_FOR_A_TRADE_SHOW_AS_AN_ATTENDEE.absolute_template,
    "how-prepare-trade-show-exhibitor": URLs.GREAT_MAGNA_LESSONS_GETTING_READY_FOR_A_TRADE_SHOW_AS_AN_EXHIBITOR.absolute_template,
    "how-adapt-your-website-international-audience": URLs.GREAT_MAGNA_LESSONS_ADAPTING_YOUR_WEBSITE_FOR_AN_INTERNATIONAL_AUDIENCE.absolute_template,
    "understand-digital-marketing": URLs.GREAT_MAGNA_LESSONS_UNDERSTANDING_DIGITAL_MARKETING.absolute_template,
    "using-online-marketplaces": URLs.GREAT_MAGNA_LESSONS_USING_ONLINE_MARKETPLACES.absolute_template,
    "protect-your-business-bribery-and-corruption": URLs.GREAT_MAGNA_LESSONS_PROTECT_YOUR_BUSINESS_FROM_BRIBERY_AND_CORRUPTION.absolute_template,
    "operating-business-integrity": URLs.GREAT_MAGNA_LESSONS_HOW_TO_OPERATE_WITH_BUSINESS_INTEGRITY.absolute_template,
    "protect-your-data-abroad": URLs.GREAT_MAGNA_LESSONS_PROTECT_YOUR_DATA_ABROAD.absolute_template,
    "pitching-and-tendering-in-a-new-market": URLs.GREAT_MAGNA_LESSONS_PITCHING_AND_TENDERING_IN_A_NEW_MARKET.absolute_template,
    "how-draft-contract": URLs.GREAT_MAGNA_HOW_TO_DRAFT_A_CONTRACT.absolute_template,
    "using-samples-prototypes-and-demos": URLs.GREAT_MAGNA_LESSONS_USING_SAMPLES_PROTOTYPES_AND_DEMOS.absolute_template,
    "how-handle-price-negotiations": URLs.GREAT_MAGNA_LESSONS_HOW_TO_HANDLE_PRICE_NEGOTIATIONS.absolute_template,


    # "selling-across-borders-product-and-services-regulations-licensing-and-logistics": URLs.GREAT_MAGNA_LESSONS_REGULATIONS_LICENSING_AND_LOGISTICS.absolute_template,
    "labelling-and-packaging": URLs.GREAT_MAGNA_LESSONS_HOW_TO_ADAPT_YOUR_LABELLING_AND_PACKAGING.absolute_template,
    "understand-duties-and-taxes": URLs.GREAT_MAGNA_LESSONS_UNDERSTAND_DUTIES_AND_TAXES.absolute_template,
    "understand-local-market-regulations-products": URLs.GREAT_MAGNA_LESSONS_UNDERSTAND_LOCAL_MARKET_REGULATIONS_FOR_PRODUCTS.absolute_template,
    "incoterms": URLs.GREAT_MAGNA_LESSONS_CHOOSE_WHICH_INCOTERMS_ARE_RIGHT_FOR_YOU.absolute_template,
    "freight-forwarders": URLs.GREAT_MAGNA_LESSONS_USING_FREIGHT_FORWARDERS.absolute_template,
    "regulations-around-e-commerce": URLs.GREAT_MAGNA_LESSONS_REGULATIONS_AROUND_E_COMMERCE.absolute_template,
    "understand-regulations-around-supplying-service": URLs.GREAT_MAGNA_LESSONS_REGULATIONS_AROUND_SUPPLYING_A_SERVICE.absolute_template,
    "understand-data-regulations-and-data-protection": URLs.GREAT_MAGNA_LESSONS_UNDERSTAND_DATA_REGULATIONS_AND_DATA_PROTECTION.absolute_template,
    "funding-financing-and-getting-paid": URLs.GREAT_MAGNA_LESSONS_FUNDING_FINANCE_AND_GETTING_PAID.absolute_template,
    "how-avoid-cashflow-challenges-when-exporting": URLs.GREAT_MAGNA_LESSONS_AVOID_CASHFLOW_CHALLENGES_WHEN_EXPORTING.absolute_template,
    "funding-and-credit-options-doing-business-across-borders": URLs.GREAT_MAGNA_LESSONS_CHOOSE_THE_RIGHT_FUNDING_AND_CREDIT_OPTIONS.absolute_template,
    "insure-against-non-payment": URLs.GREAT_MAGNA_LESSONS_INSURE_AGAINST_NON_PAYMENT.absolute_template,
    "how-create-export-invoice": URLs.GREAT_MAGNA_LESSONS_CREATE_AN_EXPORT_INVOICE.absolute_template,
    "decide-when-get-paid-export-orders": URLs.GREAT_MAGNA_LESSONS_DECIDE_WHEN_TO_GET_PAID.absolute_template,
    "payment-methods-exporters": URLs.GREAT_MAGNA_LESSONS_CHOOSE_THE_RIGHT_PAYMENT_METHOD.absolute_template,
    "managing-exchange-rates": URLs.GREAT_MAGNA_LESSONS_MANAGE_EXCHANGE_RATES.absolute_template,


}

SELECTORS = {
    "categories": {
        "get started": Selector(
            By.XPATH, "//*[@id=\"learn-root\"]/section/a[1]"
        ),
        "identify opportunities": Selector(
            By.XPATH, "//p[contains(text(),'Learn to identify opportunities abroad and find th')]"
        ),
        "prepare to sell": Selector(
            By.XPATH, "//*[@id=\"learn-root\"]/section/a[3]/article"
        ),
        "regulations licensing and logistics": Selector(
            By.XPATH, "//*[@id=\"learn-root\"]/section/a[4]/article"
        ),
        "funding finance and getting paid": Selector(
            By.XPATH, "//*[@id=\"learn-root\"]/section/a[5]/article"
        ),
        "continue learning": Selector(
            By.XPATH, "//a[contains(text(),'Continue learning')]"
        ),

    },
}


def visit(driver: WebDriver, *, page_name: str = None):
    url = SubURLs[page_name] if page_name else URL
    go_to_url(driver, url, page_name or NAME)


def should_be_here(driver: WebDriver, *, page_name: str = None):
    if page_name:
        url = SubURLs[page_name]
        logging.debug(f"visit url info -> {url} {page_name}")
        check_url_path_matches_template(url, driver.current_url)
    else:
        check_url(driver, URL, exact_match=False)


# def visit(driver: WebDriver, *, page_name: str = None):
#     go_to_url(driver, URL, page_name or NAME)
#
# def should_be_here(driver: WebDriver):
#     check_url(driver, URL, exact_match=False)

def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()


def find_progress_bar(driver: WebDriver, element_name: str):
    # search for appropriate section
    # section_element = find_element(
    #     driver, find_selector_by_name(SELECTORS, element_name)
    # )
    # search for parent progress bar div class
    h_ref_link_elements = driver.find_elements_by_class_name("learn__category-link")
    # logging.debug("length of href elements - " + str(len(h_ref_link_elements)))
    for index in range(len(h_ref_link_elements)):
        ##logging.debug("current index - " + str(index))
        h_ref_element = h_ref_link_elements[index]
        article_element = h_ref_element.find_element_by_tag_name("article")
        div_1_element = article_element.find_element_by_tag_name("div")
        # logging.debug("element_name : " + element_name)
        # logging.debug("div_1_element.text : " + div_1_element.text)
        if (element_name.lower() in div_1_element.text.lower()) and ("lessons completed" in div_1_element.text.lower()):
            # progress_bar_element = div_1_element.find_element_by_css_selector(".learn__category-content.learn__category-content--progress-bar")
            # logging.debug("progress_bar_element.text : " + progress_bar_element.text)
            # div_element = progress_bar_element.find_element_by_class_name("learn__category-progress")
            # logging.debug("div_element.text : " + div_element.text)
            # p_tag = div_element.find_element_by_tag_name("p")
            # logging.debug("p_tag.text - "+ p_tag.text)
            break
