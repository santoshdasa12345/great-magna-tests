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

NAME = "Protect your intellectual property abroad"
SERVICE = Service.LEARNTOEXPORT
TYPE = PageType.LESSON
URL = URLs.GREAT_MAGNA_LESSONS_PROTECT_YOUR_INTELLECTUAL_PROPERTY_ABROAD.absolute
PAGE_TITLE = "Protect your intellectual property abroad"

SELECTORS = {
    "protect your intellectual property abroad": {
        "lesson yes checkbox": Selector(
            By.XPATH, "//label[contains(text(),'Yes')]"
        ),
        "continue learning": Selector(
            By.XPATH, "//a[contains(text(),'Continue learning')]"
        ),
        "bottom back": Selector(
            By.XPATH, "//body/main[@id='content']/div[1]/div[3]/a[1]/i[1]"
        ),
        "top back": Selector(
            By.XPATH, "//*[@id=\"content\"]/div/a/i"
        ),
        "open case study" :Selector(
            By.XPATH, "//button[contains(text(),'Open case study')]"
        ),
        "close case study": Selector(
            By.XPATH, "//*[@id=\"case_study\"]/div/button"
        ),
        "view all lessons": Selector(
            By.XPATH, "//a[contains(text(),'View all lessons')]"
        ),
        "view transcript": Selector(
            By.XPATH, "//span[contains(text(),'View transcript')]"
        ),

    },
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def check_lesson_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()
