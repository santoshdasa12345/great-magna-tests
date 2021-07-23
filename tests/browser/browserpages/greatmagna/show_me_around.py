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

NAME = "Show Me Around"
SERVICE = Service.GREATMAGNA
TYPE = PageType.SEARCH
URL = URLs.GREAT_MAGNA_LOGIN.absolute
PAGE_TITLE = "Page Tour "

SELECTORS = {
    "show me around": {
        "show me around": Selector(
            By.XPATH, "//button[@id='page-tour-submit']"
        ),
        "next step": Selector(
            By.XPATH, "//button[@id='page-tour-next-step']"
        ),
    },
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def login(driver: WebDriver, email_address: str, password: str):
    details_dict = {"emailaddress": email_address, "password": password}
    fill_out_email_address(driver, details_dict)


def click_show_me_around(driver: WebDriver):
    show_me_around_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "show me around")
    )
    show_me_around_btn.click()
