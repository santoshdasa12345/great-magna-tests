import logging
import random
import time
from types import ModuleType
from typing import List, Union

from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Actor,
    Selector,
    assertion_msg,
    check_for_sections,
    check_if_element_is_not_present,
    check_if_element_is_visible,
    check_random_radio,
    check_url,
    fill_out_email_address,
    fill_out_input_fields,
    find_element,
    find_elements,
    find_selector_by_name,
    go_to_url,
    is_element_present,
    pick_option,
    submit_form,
    take_screenshot,
    wait_for_page_load_after_action,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from great_magna_tests_shared.utils import check_url_path_matches_template

NAME = "search"
SERVICE = Service.GREATMAGNA
TYPE = PageType.SEARCH
URL = URLs.GREAT_MAGNA_SEARCH.absolute
PAGE_TITLE = "Search Page"

SELECTORS = {
    "search": {
        "products": Selector(
            By.XPATH,
            "//body/nav[@id='personalisation-bar']/span[@id='set-product-button']/span[1]/button[1]",
            type=ElementType.INPUT,
        ),
        "country": Selector(
            By.XPATH,
            "//body/nav[@id='personalisation-bar']/span[@id='set-country-button']/span[1]/button[1]",
            type=ElementType.INPUT,
        ),
        # "skipwalkthrough": Selector(
        #     By.XPATH, "//*[@id=\"page-tour-skip\"]"
        # ),
        "searchagain": Selector(By.XPATH, "//button[@class='back-button m-f-l m-t-m']"),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def fill_out_products_and_country(driver: WebDriver, products: str, country: str):
    fill_out_input_fields(driver, products, country)


def fill_out_products(driver: WebDriver, products: str):
    fill_out_input_fields(driver, products)
