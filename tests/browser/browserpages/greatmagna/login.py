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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from great_magna_tests_shared.utils import check_url_path_matches_template

NAME = "Login"
SERVICE = Service.GREATMAGNA
TYPE = PageType.SEARCH
URL = URLs.GREAT_MAGNA_LOGIN.absolute
PAGE_TITLE = "Login Page "

SELECTORS = {
    "login": {
        "forgotten_password": Selector(
            By.CSS_SELECTOR,
            "#login > div > div.signup__steps-panel > form > a.text-red-80.inline-block"
            # //a[contains(text(),'Forgotten password?')]
        ),
        "emailaddress": Selector(
            By.XPATH, "//input[@id='email']", type=ElementType.INPUT
        ),
        "password": Selector(
            By.XPATH, "//input[@id='password']", type=ElementType.INPUT
        ),
        "login button": Selector(By.XPATH, "//button[@id='signup-modal-submit']"),
        "error message": Selector(By.XPATH, "//li[@class='error-message']"),
        "incorrect username and password": Selector(
            By.CSS_SELECTOR, "#login > form > ul > li"
        ),
        "email - field may not be blank": Selector(
            By.CSS_SELECTOR, "#login > form > div:nth-child(3) > ul > li"
        ),
        "password - field may not be blank": Selector(
            By.CSS_SELECTOR, "#login > form > div:nth-child(4) > ul > li"
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


def find_and_click_change_link(driver: WebDriver, element_selector_name: str):
    change_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    change_link.click()


def fill_out_email_address(driver: WebDriver, details: dict):
    email_address_selectors = SELECTORS["login"]
    logging.debug(email_address_selectors)
    logging.debug(details)
    fill_out_input_fields(driver, email_address_selectors, details)
    fill_input_list = find_element(
        driver, find_selector_by_name(SELECTORS, "login button")
    )
    fill_input_list.click()
    driver.implicitly_wait(000)


def should_be_error_message(
    driver: WebDriver, element_name: str, expected_error_message: str
):
    try:
        selectors = SELECTORS["login"]
        element_selector = selectors[element_name]
        actual_error_message = driver.find_element_by_css_selector(
            element_selector.value
        ).text
        # logging.debug(f"actual_error_message -> {actual_error_message}")
        actual_error_message = actual_error_message.strip()
        if actual_error_message in expected_error_message:
            return True
    except NoSuchElementException as ex:
        logging.debug("Exception : " + ex.msg)
        pass

    return False
