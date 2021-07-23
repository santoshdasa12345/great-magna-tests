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
    fill_out_email_address,
    fill_out_textarea_fields,
)

NAME = "Getting Paid"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_GETTING_PAID.absolute
PAGE_TITLE = "Getting Paid Page"

SELECTORS = {
    "getting paid": {
        "payment methods": Selector(
            By.CSS_SELECTOR,
            "#getting-paid > div > div:nth-child(1) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius"
        ),
        "payment methods notes": Selector(
            By.CSS_SELECTOR, "#method_notes", type=ElementType.INPUT
        ),
        "payment terms": Selector(
            By.CSS_SELECTOR,
            "#getting-paid > div > div:nth-child(2) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius"
        ),
        "payment terms notes": Selector(
            By.CSS_SELECTOR, "#payments_notes", type=ElementType.INPUT
        ),
        "incoterms": Selector(
            By.CSS_SELECTOR,
            "#getting-paid > div > div:nth-child(3) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius"
        ),
        "incoterms notes": Selector(
            By.CSS_SELECTOR, "#incoterms_notes", type=ElementType.INPUT
        ),
        "section complete": Selector(
            By.XPATH, "//label[contains(text(),'Yes')]"
        ),
        "travel plan": Selector(
            By.XPATH, "//span[contains(text(),'Travel and business policies')]"
        ),
        "export plan home": Selector(
            By.CSS_SELECTOR,
            "#costs-and-pricing-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > div.m-t-l > a"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav travel plan": Selector(
            By.XPATH, "//*[@id=\"collapseNav\"]/div/ul/li[9]/a"
        ),
        "back": Selector(
            By.XPATH, "//body/div[10]/div/div/div/div[1]/a"
        ),
        "add a target market": Selector(
            By.XPATH, "//button[contains(text(),'Add a target market')]"
        ),
        "top export plan home": Selector(
            By.XPATH, "//*[@id=\"business-risk-content\"]/section[1]/div/div/div[2]/a/span"
        ),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def enter_text(driver: WebDriver, element_name: str):
    text_element = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    text_element.clear()
    text_element.send_keys("Automated tests")


def validate_entered_text(driver: WebDriver, element_name: str):
    text_element = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    if "Automated tests" in text_element.text:
        return True
    return False


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()


def enter_business_objectives_details(driver: WebDriver, startdate: str, enddate: str, objectives: str, owner: str,
                                      plannedreviews: str):
    input_field_selectors = SELECTORS["business objectives"]
    input_details_dict = {"start date": startdate, "end date": enddate, "owner": owner}
    fill_out_input_fields(driver, input_field_selectors, input_details_dict)

    text_area_details_dict = {"objective text": objectives, "planned review": plannedreviews}
    fill_out_textarea_fields(driver, input_field_selectors, text_area_details_dict)
    time.sleep(1)


def find_and_select_random_item_list(driver: WebDriver, element_selector_name: str):
    payment_methods_btn = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(1) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius")
    payment_methods_btn.click()
    payment_terms_btn = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(2) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius")
    payment_terms_btn.click()
    incoterms_btn = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(3) > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius")
    incoterms_btn.click()
    driver.implicitly_wait(5)
    # select__list body-l bg-white radius
    payment_methods_element = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(1) > div.select.m-b-l > div > ul")
    payment_terms_element = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(2) > div.select.m-b-l > div > ul")
    incoterms_element = driver.find_element_by_css_selector(
        "#getting-paid > div > div:nth-child(3) > div.select.m-b-l > div > ul")

    li_elements = payment_methods_element.find_elements_by_tag_name("li")
    li_elements = payment_terms_element.find_elements_by_tag_name("li")
    li_elements = incoterms_element.find_elements_by_tag_name("li")
    logging.debug("list elements")
    logging.debug(li_elements)
    random_number = 0
    if len(li_elements) > 2:
        random_number = random.randint(1, len(li_elements) - 1)
    random_li_element = li_elements[random_number]
    logging.debug(random_number)
    logging.debug(random_li_element.tag_name)
    logging.debug(random_li_element)
    time.sleep(2)
