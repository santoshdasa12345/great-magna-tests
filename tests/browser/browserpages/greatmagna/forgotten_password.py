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

from great_magna_tests_shared import URLs, settings
from great_magna_tests_shared.enums import PageType, Service
from great_magna_tests_shared.reademail import ReadEmail
from great_magna_tests_shared.utils import check_url_path_matches_template

NAME = "forgotten password"
SERVICE = Service.GREATMAGNA
TYPE = PageType.SEARCH
URL = URLs.GREAT_MAGNA_FORGOTTEN_PASSWORD.absolute
PAGE_TITLE = "Forgotten password Page"

SELECTORS = {
    "forgotten password": {
        "emailaddress": Selector(
            By.XPATH, "//input[@id='id_email']", type=ElementType.INPUT
        ),
        "resetmypassword": Selector(
            By.XPATH, "//button[contains(text(),'Reset my password')]"
        ),
        "newpassword": Selector(
            By.XPATH, "//input[@id='id_password1']", type=ElementType.INPUT
        ),
        "confirmpassword": Selector(
            By.XPATH, "//input[@id='id_password2']", type=ElementType.INPUT
        ),
        "changepassword": Selector(By.XPATH, "//button[@class='button']"),
    },
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def fill_out_email_address(driver: WebDriver, details: dict):
    email_address_selectors = SELECTORS["forgotten password"]
    fill_out_input_fields(driver, email_address_selectors, details)
    reset_password_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "resetmypassword")
    )
    reset_password_btn.click()


def read_reset_password_email(
    driver: WebDriver, emailaddress: str, emailpassword: str, newpassword: str
):
    # create and load the confirmation code email from the test user
    objreadmail = ReadEmail(
        settings.DEV_GMAIL_HOST, emailaddress, emailpassword, settings.EMAIL_FETCH_COUNT
    )
    # search the test user INBOX, read the email body text from the Reset password email
    email_search_criteria = "Reset your password at "
    email_body_text = objreadmail.reademailbody(
        "Reset your great.gov.uk password", email_search_criteria
    )
    # print(email_body_text)

    # check if the email_body_text exists or empty
    if email_body_text:
        # search text position in email_body_text
        reset_link_pos = email_body_text.find(email_search_criteria)
        # check if the required search criteria text found in the email_body_text. -1 indicates not found.
        if reset_link_pos != -1:
            reset_link_text = email_body_text[
                reset_link_pos + len(email_search_criteria) :
            ]
            reset_link_text = reset_link_text.strip()  # trim left and right

            reset_link_end_pos = reset_link_text.find("/about/")
            if reset_link_end_pos != -1:
                reset_link_text = reset_link_text[: reset_link_end_pos + len("/about/")]
                reset_link_text = reset_link_text.strip()  # trim left and right
                # print(reset_link_text)
                driver.get(reset_link_text)
                if driver.find_element_by_xpath(
                    "//h1[contains(text(),'Change Password')]"
                ).is_displayed():
                    driver.find_element_by_xpath(
                        "//input[@id='id_password1']"
                    ).send_keys(newpassword)
                    driver.find_element_by_xpath(
                        "//input[@id='id_password2']"
                    ).send_keys(newpassword)
                    driver.find_element_by_xpath(
                        "//button[contains(text(),'change password')]"
                    ).click()
                else:
                    raise Exception("Could not find Change Password")
            else:
                raise Exception("Could not find about section")
        else:
            raise Exception("Invalid email, link position")
    else:
        raise Exception("Invalid email")


def confirm_password(driver: WebDriver, password: str):
    details_dict = {"password": password}
    confirm_password(driver, details_dict)


def click_forgotten_password(driver: WebDriver, element_name: str):
    forgotten_password = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    forgotten_password.click()
