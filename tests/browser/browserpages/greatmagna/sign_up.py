import logging
import random
import time
from types import ModuleType
from typing import List, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import (
    NoSuchElementException,
)
from great_magna_tests_shared import URLs, settings
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType, common_selectors
from great_magna_tests_shared.reademail import ReadEmail
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

NAME = "Sign up"
SERVICE = Service.GREATMAGNA
TYPE = PageType.SEARCH
URL = URLs.GREAT_MAGNA_SIGNUP.absolute_template
PAGE_TITLE = "Sign up Page"

SubURLs = {
    "sign up": URL,
    #Sign up learn to export,where to export, make an export plan
    "?next=/learn/categories/": URLs.GREAT_MAGNA_SIGNUP_LEARN_TO_EXPORT.absolute_template,
    "?next=/where-to-export/": URLs.GREAT_MAGNA_SIGNUP_WHERE_TO_EXPORT.absolute_template,
    "?next=/export-plan/dashboard/": URLs.GREAT_MAGNA_SIGNUP_MAKE_AN_EXPORT_PLAN.absolute_template,

}

SELECTORS = {
    "sign up": {
        "emailaddress": Selector(
            By.XPATH, "//input[@name='email']", type=ElementType.INPUT
        ),
        "password": Selector(
            By.XPATH, "//input[@id='password']", type=ElementType.INPUT
        ),
        "sign up button": Selector(
            By.XPATH, "//button[@id='signup-modal-submit']"
        ),
        "code": Selector(
            By.XPATH, "//input[@id='code']", type=ElementType.INPUT

        ),
        "submit": Selector(
            By.XPATH, "//button[@id='signup-modal-submit-code']"
        ),
        "continue": Selector(
            By.XPATH, "//a[@id='signup-modal-submit-success']"  # # #signup-modal-submit-success
        ),
        "add a target market": Selector(
            By.XPATH, "//button[contains(text(),'Add a target market')]"
        ),
        "search country": Selector(
            By.CSS_SELECTOR, "#search-input", type=ElementType.INPUT
        ),
        "google login": Selector(
            By.CSS_SELECTOR, "#signup-modal-google", type=ElementType.INPUT
        ),
        "sign in": Selector(
            By.CSS_SELECTOR, "#signup-modal-log-in"
        ),

    },
}
SubURLs = {
    "sign up": URL,
    "required":
        URLs.GREAT_MAGNA_SIGNUP.absolute_template,
}

def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver, *, page_name: str = None):
    check_url(driver, URL, exact_match=False)
    #check_url_path_matches_template(URL, driver.current_url)
    # url = SubURLs[page_name.lower()] if page_name else URL
    # check_url(driver, url, exact_match=False)
    # msg = f"Got 404 on {driver.current_url}"
    # assert "This page cannot be found" not in driver.page_source, msg


def sign_up(driver: WebDriver, email_address: str, password: str):
    details_dict = {"emailaddress": email_address, "password": password}
    fill_out_email_address(driver, details_dict)


def fill_out_email_address(driver: WebDriver, details: dict):
    email_address_selectors = SELECTORS["sign up"]
    fill_out_input_fields(driver, email_address_selectors, details)
    fill_input_list = find_element(driver, find_selector_by_name(SELECTORS, "sign up button"))
    fill_input_list.click()


def confirmation_code(driver: WebDriver, email: str, password: str):
    time.sleep(2)
    logging.debug("email: " + email)
    logging.debug("password: " + password)
    readMailBody = ReadEmail(settings.DEV_GMAIL_HOST, email, password, settings.EMAIL_FETCH_COUNT)
    email_body_text = readMailBody.reademailbody(settings.EMAIL_SEARCH_SUBJECT, settings.EMAIL_SEARCH_CRITERIA)

    # check if the email_body_text exists or empty
    if email_body_text:
        # search text position in email_body_text
        c_code_pos = email_body_text.find(settings.EMAIL_SEARCH_CRITERIA)
        confirmation_code = '00000'  # default
        # check if the required search criteria text found in the email_body_text. -1 indicates not found.
        if c_code_pos != -1:
            confirmation_code = email_body_text[c_code_pos + len(settings.EMAIL_SEARCH_CRITERIA):c_code_pos + len(
                settings.EMAIL_SEARCH_CRITERIA) + settings.CONFIRMATION_CODE_LENGTH]
        confirmation_code = confirmation_code.strip()  # trim left and right

        if confirmation_code.isdigit():
            details = {"code": confirmation_code}
        else:
            raise Exception("Failed to fetch the confirmation code from User email.")
    else:
        raise Exception("Failed to fetch the confirmation code from User email.")

    confirmation_code_selectors = SELECTORS["sign up"]
    fill_out_input_fields(driver, confirmation_code_selectors, details)
    fill_input_list = find_element(driver, find_selector_by_name(SELECTORS, "submit"))
    fill_input_list.click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@id='signup-modal-submit-success']").click()


# def should_be_error_message(driver: WebDriver, expectederrormessage: str):
#     error_span_element = driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/ul[1]/li[1]")
#     actual_error_message = str(error_span_element.get_attribute("text"))
#     actual_error_message = actual_error_message.strip()
#     if actual_error_message in expectederrormessage:
#         return True
#     return False

def should_be_error_message(driver: WebDriver, element_name: str, expected_error_message: str):
    try:
        selectors = SELECTORS["login"]
        element_selector = selectors[element_name]
        actual_error_message = driver.find_element_by_css_selector(element_selector.value).text
        # logging.debug(f"actual_error_message -> {actual_error_message}")
        actual_error_message = actual_error_message.strip()
        if actual_error_message in expected_error_message:
            return True
    except NoSuchElementException as ex:
        logging.debug("Exception : " + ex.msg)
        pass

    return False


def fill_out_country(driver: WebDriver, country: str):

    driver.find_element_by_xpath("add a target market").click()

    driver.find_element_by_css_selector("#search-input").clear()
    driver.find_element_by_css_selector("#search-input").send_keys(country)

    input_elements = driver.find_elements_by_tag_name("input")
         # logging.debug(input_elements)
    for input_element in input_elements:
             # logging.debug(input_element.text)
        if input_element.text == country.lower():
            input_element.click()


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()
