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

NAME = "Export Plan Dashboard"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_DASHBOARD.absolute
PAGE_TITLE = "Export Plan Dashboard"

SubURLs = {
    "export plan dashboard": URLs.GREAT_MAGNA_NEW_EXPORT_PLAN.absolute_template,
}

SELECTORS = {
    "Export Plan Dashboard": {
        "about your business": Selector(
            By.XPATH, '//*[@id="export-plan-dashboard"]/div[1]/div/a/div[2]/h3'
        ),
        "business objectives": Selector(
            By.CSS_SELECTOR,
            "#export-plan-dashboard > div:nth-child(2) > div > a > div.section-list__image-container > img"
            # "#export-plan-dashboard > div:nth-child(2) > div > a > div.p-t-s.p-b-xs.p-h-xs"
        ),
        "target markets research": Selector(
            By.XPATH, '//*[@id="export-plan-dashboard"]/div[3]/div/a/div[2]'
        ),
        "adapting your product": Selector(
            By.XPATH, '//*[@id="export-plan-dashboard"]/div[4]/div/a/div[2]/h3'
        ),
        "marketing approach": Selector(
            By.XPATH, "//h3[contains(text(),'Marketing approach')]"
        ),
        "costs and pricing": Selector(
            By.XPATH, "//h3[contains(text(),'Costs and pricing')]"
        ),
        "funding and credit": Selector(
            By.CSS_SELECTOR,
            "#export-plan-dashboard > div:nth-child(7) > div > a > div.p-xs"
            # export-plan-dashboard > div:nth-child(7) > div > a > div.p-t-s.p-b-xs.p-h-xs > p"
        ),
        "getting paid": Selector(By.XPATH, "//h3[contains(text(),'Getting paid')]"),
        "travel plan": Selector(By.XPATH, "//h3[contains(text(),'Travel plan')]"),
        "business risk": Selector(By.XPATH, "//h3[contains(text(),'Business risk')]"),
        "upload logo": Selector(By.XPATH, "//h3[contains(text(),'Upload your logo')]"),
        "save your plan as pdf": Selector(
            By.XPATH, "//span[contains(text(),'Save your plan as a PDF')]"
        ),
        "ok button": Selector(
            By.CSS_SELECTOR,
            "body > div:nth-child(18) > div > div > div > div.modal-inner.text-blue-deep-80.bg-white.radius-bottom-s > div > button",
        ),
        "back": Selector(
            By.CSS_SELECTOR,
            "body > div:nth-child(18) > div > div > div > div.modal-header.modal-header-bg.modal-header-bg--3.radius-top-s.bg-blue-deep-80.p-s > a",
        ),
        "dashboard": Selector(By.XPATH, "//a[contains(text(),'Dashboard')]"),
        "start your free plan": Selector(
            By.CSS_SELECTOR,
            "#content > div > div > div > div:nth-child(2) > div > div > a",
        ),
        "download plan": Selector(By.XPATH, "//body/main/section/aside/a"),
        "delete plan": Selector(By.XPATH, "//body/main/section/aside/div[2]/button"),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


# def should_be_here(driver: WebDriver):
#     check_url(driver, URL, exact_match=False)

# def should_be_here(driver: WebDriver):
#     check_url_path_matches_template( URL,driver.current_url)


def should_be_here(driver: WebDriver, *, page_name: str = None):
    if page_name:
        url = SubURLs[page_name]
        logging.debug(f"visit url info -> {url} {page_name}")
        check_url_path_matches_template(url, driver.current_url)
    else:
        check_url(driver, URL, exact_match=False)


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()
