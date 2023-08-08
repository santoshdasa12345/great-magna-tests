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

NAME = "Export Plan Dashboard Navigation"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_DASHBOARD.absolute
PAGE_TITLE = "Export Plan Dashboard Navigation"

SELECTORS = {
    "Navigation side bar": {
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]",
        ),
        "about your business": Selector(
            By.XPATH, '//*[@id="export-plan-dashboard"]/div[1]/div/a/div[2]/h3'
        ),
        "business objectives": Selector(
            By.XPATH, "//a[contains(text(),'Business objectives')]"
        ),
        "target market research": Selector(
            By.XPATH, "//a[contains(text(),'Target markets research')]"
        ),
        "Adapting Your Product": Selector(
            By.XPATH, "//a[contains(text(),'Adapting Your Product')]"
        ),
        "marketing approach": Selector(
            By.XPATH, "//a[contains(text(),'Marketing approach')]"
        ),
        "costs and pricing": Selector(
            By.XPATH, "//a[contains(text(),'Costs and pricing')]"
        ),
        "funding and credit": Selector(
            By.XPATH, "//a[contains(text(),'Funding and Credit')]"
        ),
        "payment methods": Selector(
            By.XPATH, "//button[contains(text(),'Payment methods')]"
        ),
        "travel and business policies": Selector(
            By.XPATH, "//button[contains(text(),'Travel and business policies')]"
        ),
        "business risks": Selector(
            By.XPATH, "//button[contains(text(),'Business risk')]"
        ),
        "share": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/div[2]/button[1]/i[1]",
        ),
        "download": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/div[2]/button[2]/i[1]",
        ),
        "ok": Selector(By.XPATH, "//button[contains(text(),'Ok')]"),
        "back": Selector(By.XPATH, "//body/div[6]/div[1]/div[1]/div[1]/div[1]/a[1]"),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()
