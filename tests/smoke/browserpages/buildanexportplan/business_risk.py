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

NAME = "Business Risk"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_BUSINESS_RISK.absolute
PAGE_TITLE = "Business Risk Page"

SELECTORS = {
    "business risk": {
        "risk educational": Selector(
            By.XPATH, "//*[@id=\"business-risks\"]/div[2]/table/tbody/tr[1]/td/div[1]/div[1]/div/div/button/i"
        ),
        "risk example": Selector(
            By.XPATH, "//*[@id=\"business-risks\"]/div[2]/table/tbody/tr[1]/td/div[1]/div[1]/button"
        ),
        "risk": Selector(
            By.XPATH, "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[1]/table/tr[2]/td[1]/div/div[1]/button/i" , type=ElementType.INPUT
        ),
        "risk likelihood educational": Selector(
            By.XPATH, "//*[@id=\"business-risks\"]/div[2]/table/tbody/tr[2]/td/div[1]/div[1]/div/div/button/i"
        ),
        "rare": Selector(
            By.XPATH, "//label[contains(text(),'Rare')]"
        ),
        "unlikely": Selector(
            By.XPATH, "//label[contains(text(),'Unlikely')]"
        ),
        "possible": Selector(
            By.XPATH, "//label[contains(text(),'Possible')]"
        ),
        "likely": Selector(
            By.XPATH, "//label[contains(text(),'Likely')]"
        ),
        "certain": Selector(
            By.XPATH, "//label[contains(text(),'Certain')]"
        ),
        "freight and logistics": Selector(
            By.XPATH, "//input[@id='freight_logistics']"
        ),
        "trivial": Selector(
            By.XPATH, "//label[contains(text(),'Trivial')]"
        ),
        "minor": Selector(
            By.XPATH, "//label[contains(text(),'Minor')]"
        ),
        "moderate": Selector(
            By.XPATH, "//label[contains(text(),'Moderate')]"
        ),
        "severe": Selector(
            By.XPATH, "//label[contains(text(),'Severe')]"
        ),
        "major": Selector(
            By.XPATH, "//label[contains(text(),'Major')]"
        ),
        "contingency plan educational": Selector(
            By.XPATH, "//*[@id=\"business-risks\"]/div[2]/table/tbody/tr[4]/td/div[1]/div[1]/div/div/button/i"
        ),
        "contingency plan example": Selector(
            By.CSS_SELECTOR,
            "#business-risks > div.costs.costs--risks.bg-blue-deep-10.p-v-s.m-b-s > table > tbody > tr:nth-child(4) > td > div.learning > div.learning__buttons.m-b-xs > button"
        ),
        "add a risk": Selector(
            By.XPATH, "//*[@id=\"business-risks\"]/button"
        ),
        "export plan home": Selector(
            By.XPATH, "//*[@id=\"business-risk-content\"]/section[4]/div/div/div[2]/div[2]/a/span"
        ),
        "top export plan home": Selector(
            By.XPATH, "//*[@id=\"business-risk-content\"]/section[1]/div/div/div[2]/a/span"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav Adapting Your Product": Selector(
            By.XPATH, "//a[contains(text(),'Adapting Your Product')]"
        ),
        "back": Selector(
            By.XPATH, "//body/div[10]/div/div/div/div[1]/a"
        ),
        "add a target market": Selector(
            By.XPATH, "//button[contains(text(),'Add a target market')]"
        ),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def enter_text(driver: WebDriver, element_name: str):
    text_element = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    text_element.clear()
    text_element.send_keys("Automated tests")


def validate_entered_text(driver: WebDriver, element_name: str):
    text_element = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    if "Automated tests" in text_element.text:
        return True
    return False


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()
