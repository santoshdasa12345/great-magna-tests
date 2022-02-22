# -*- coding: utf-8 -*-
"""Profile - Enrol - Enter your confirmation code"""
from types import ModuleType
from typing import List, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType
from browserpages.common_actions import (
    Actor,
    Selector,
    check_for_sections,
    check_url,
    fill_out_input_fields,
    go_to_url,
    submit_form,
)
from browserpages.greatmagna import dashboard

NAME = "Sign Up confirmation code"
SERVICE = Service.GREATMAGNA
TYPE = PageType.FORM
URL = URLs.GREAT_MAGNA_SIGNUP_CONFIRMATION_CODE_LANDING.absolute
PAGE_TITLE = ""

# SELECTORS = {
#
#     # "enrolment progress bar": {"itself": Selector(By.ID, "progress-column")},
#     # "confirmation code message": {
#     #     "message": Selector(
#     #         By.CSS_SELECTOR, "#user-account-verification-header-container p"
#     #     )
#     # },
#     # "an option to resend the code": {
#     #     "resend my code": Selector(By.CSS_SELECTOR, "section form a")
#     # },
#     "confirmation code form": {
#         "itself": Selector(By.CSS_SELECTOR, "section form"),
#         "code": Selector(By.ID, "id_verification-code", type=ElementType.INPUT),
#         "submit": Selector(
#             By.CSS_SELECTOR, "form button.button", type=ElementType.SUBMIT
#         ),
#     },
# }

SELECTORS = {
    "confirmation code": {

        "code": Selector(
            By.XPATH, "//input[@id='code']", type=ElementType.INPUT
        ),
        "submit button": Selector(
            # By.XPATH, "//button[@id='signup-modal-submit-code']"
            By.CSS_SELECTOR,
            "#signup-modal-submit",
            type=ElementType.SUBMIT,
            next_page=dashboard,
        ),

    },
}
def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


# def generate_form_details(actor: Actor) -> dict:
#     return {"code": actor.email_confirmation_code}
#
#
# def fill_out(driver: WebDriver, details: dict):
#     form_selectors = SELECTORS["confirmation code form"]
#     fill_out_input_fields(driver, form_selectors, details)


# def submit(driver: WebDriver) -> Union[ModuleType, None]:
#     return submit_form(driver, SELECTORS["confirmation code form"])

def generate_form_details(actor: Actor, *, custom_details: dict = None) -> dict:
    result = {
        "code": actor.email_confirmation_code,
        # "confirm password": actor.password,
        # "t & c": True,
    }
    if custom_details:
        result.update(custom_details)
    return result


def fill_out(driver: WebDriver, details: dict):
    form_selectors = SELECTORS["confirmation code"]
    fill_out_input_fields(driver, form_selectors, details)
    # tick_checkboxes(driver, form_selectors, details)
    # tick_captcha_checkbox(driver)

def submit(driver: WebDriver) -> Union[ModuleType, None]:
    return submit_form(driver, SELECTORS["confirmation code"])

