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

NAME = "Footer"
SERVICE = Service.GREATMAGNA
TYPE = PageType.SEARCH
URL = URLs.GREAT_MAGNA_DASHBOARD.absolute
PAGE_TITLE = "Dashboard Page "

SELECTORS = {
    "footer": {
        "logo": Selector(
            By.XPATH, "//*[@id=\"footer\"]/nav/div/a/img"
        ),
        "privacy notice": Selector(
            By.XPATH, "//a[contains(text(),'Privacy notice')]"
        ),
        "terms and conditions": Selector(
            By.XPATH, "//a[contains(text(),'Terms and conditions')]"
        ),
        "contact us": Selector(
            By.XPATH, "//a[contains(text(),'Contact us')]"
        ),
        "dit link": Selector(
            By.XPATH, "//a[contains(text(),'Department for International Trade on GOV.UK')]"
        ),
        "dit logo": Selector(
            By.XPATH, "//body/footer[@id='footer']/div[1]/div[1]/img[1]"
        ),
        "copyright": Selector(
            By.XPATH, "//p[contains(text(),'© Crown copyright 2021. All rights reserved.')]"
        ),
    },
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)
