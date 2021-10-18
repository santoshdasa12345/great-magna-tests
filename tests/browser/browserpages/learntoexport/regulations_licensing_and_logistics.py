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

NAME = "Regulations licensing and logistics"
SERVICE = Service.LEARNTOEXPORT
TYPE = PageType.LESSON
URL = URLs.GREAT_MAGNA_LESSONS_REGULATIONS_LICENSING_AND_LOGISTICS.absolute
PAGE_TITLE = "Regulations licensing and logistics page"

SELECTORS = {
    "Regulations licensing and logistics": {
        "how to adapt your labelling and packaging": Selector(
            By.XPATH, "//span[contains(text(),'How to adapt your labelling and packaging')]"
        ),
        "understand duties and taxes": Selector(
            By.XPATH, "//span[contains(text(),'Understand duties and taxes')]"
        ),
        "understand local market regulations for products": Selector(
            By.CSS_SELECTOR, "#\31 05 > ul > li:nth-child(3) > a"
        ),
        "using harmonised system or commodity codes": Selector(
            By.CSS_SELECTOR, "#\31 05 > ul > li:nth-child(4) > a"
        ),
        "applying rules sof orgin to your product": Selector(
            By.CSS_SELECTOR, "#\31 05 > ul > li:nth-child(4) > a"
        ),
        "choose which incoterms are right for you": Selector(
            By.XPATH, "//span[contains(text(),'Choose which Incoterms are right for you')]"
        ),
        "using freight forwarders": Selector(
            By.CSS_SELECTOR, "#\31 10 > ul > li:nth-child(2) > a"
        ),
        "regulations around ecommerce": Selector(
            By.CSS_SELECTOR, "#\31 12 > ul > li:nth-child(1) > a"
        ),
        "regulations around supplying a service": Selector(
            By.CSS_SELECTOR, "#\31 12 > ul > li:nth-child(2) > a"
        ),
        "understand data regulations and data protection": Selector(
            By.CSS_SELECTOR, "#\31 12 > ul > li:nth-child(3) > a"
        ),
        "how to make uk customs declaration": Selector(
            By.CSS_SELECTOR, "#\31 22 > ul > li:nth-child(1) > a"
        ),
        "understand export licensing": Selector(
            By.CSS_SELECTOR, "#\31 22 > ul > li:nth-child(2) > a"
        ),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)
