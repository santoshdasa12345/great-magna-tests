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

NAME = "Get Started"
SERVICE = Service.LEARNTOEXPORT
TYPE = PageType.LESSON
URL = URLs.GREAT_MAGNA_LESSONS_GET_STARTED.absolute
PAGE_TITLE = "Get Started Page "

SELECTORS = {
    "get started": {
        "what youll find in each lesson": Selector(
            By.XPATH, "//*[@id=\"330\"]/ul/li[1]/a/span"
        ),
        "how lessons can help": Selector(
            By.XPATH, "//span[contains(text(),'How lessons can help you make an export plan')]"
        ),
        "top back": Selector(
            By.XPATH, "//body/main[@id='content']/div[@id='learn-root']/a[1]/i[1]"
        ),

    },
}

def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def find_and_click(driver: WebDriver, *, page_name: str = None):
    find_and_click(driver, URL, page_name)

# def find_and_select_click_continue(driver: WebDriver, *, page_name: str = None):
#     select_click_continue(driver, URL, page_name)


def find_and_click_case_study(driver: WebDriver, *, page_name: str = None):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()