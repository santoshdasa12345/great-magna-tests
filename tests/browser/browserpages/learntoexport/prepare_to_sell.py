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

NAME = "Prepare to sell"
SERVICE = Service.LEARNTOEXPORT
TYPE = PageType.LESSON
URL = URLs.GREAT_MAGNA_LESSONS_PREPARE_TO_SELL_INTO_A_NEW_COUNTRY.absolute
PAGE_TITLE = "Prepare to sell page"

SELECTORS = {
    "Prepare to sell": {
        "choose the right route to market": Selector(
            By.XPATH, "//span[contains(text(),'Choose the right route to market')]"
        ),
        "Selling direct to your customer": Selector(
            By.XPATH, "//span[contains(text(),'Selling direct to your customer')]"
        ),
        "sell with international e commerce": Selector(
            By.XPATH, "//span[contains(text(),'Selling with international e-commerce')]"
        ),
        "understand the local business culture": Selector(
            By.XPATH, "//span[contains(text(),'Understand the local business culture in your targ')]"
        ),
        "understand product liability": Selector(
            By.XPATH, "//span[contains(text(),'Understand product liability')]"
        ),
        "protect your intellectual property abroad": Selector(
            By.XPATH, "//span[contains(text(),'Protect your intellectual property abroad')]"
        ),
        "decide whether to use licensing": Selector(
            By.XPATH, "//span[contains(text(),'Decide whether to use licensing')]"
        ),
        "set up joint ventures abroad": Selector(
            By.XPATH, "//span[contains(text(),'Set up joint ventures abroad')]"
        ),
        "setting up a franchise abroad": Selector(
            By.XPATH, "//span[contains(text(),'Setting up a franchise abroad')]"
        ),
        "how to set up a business abroad": Selector(
            By.XPATH, "//span[contains(text(),'How to set up a business abroad')]"
        ),
        "how to adapt your website for an international audience": Selector(
            By.XPATH, "//span[contains(text(),'How to adapt your website for an international aud')]"
        ),
        "module_progress": Selector(
            By.XPATH, "#learn-root > section.learn__single-category-header > div > div > div:nth-child(1) > div.learn__single-category-header-content > div.learn__category-progress-container"
        ),
        "lessons_progress_bar": Selector(
            By.XPATH, "//*[@id=\"55\"]/div/p"
        ),
        "lesson_categories_progress": Selector(
            By.CSS_SELECTOR, "4. #learn-root > section > a:nth-child(3) > article > div > div.learn__category-content.learn__category-content--progress-bar > div.learn__category-progress-container > div"
        ),
        "how to prepare for a trade mission": Selector(
            By.XPATH, "//span[contains(text(),'How to prepare for a trade mission')]"
        ),
        "how to prepare for a trade show as an attendee": Selector(
            By.XPATH, "//span[contains(text(),'How to prepare for a trade show as an attendee')]"
        ),
        "how to prepare for a trade show as an exhibitor": Selector(
            By.XPATH, "//span[contains(text(),'How to prepare for a trade show as an exhibitor')]"
        ),
        "understand digital marketing": Selector(
            By.XPATH, "//span[contains(text(),'Understand digital marketing')]"
        ),
        "how to draft a contract": Selector(
            By.XPATH, "//span[contains(text(),'How to draft a contract')]"
        ),
        "operating with business integrity": Selector(
            By.XPATH, "//span[contains(text(),'Operating with business integrity')]"
        ),
        "protect your business from bribery and corruption": Selector(
            By.XPATH, "//span[contains(text(),'Protect your business from bribery and corruption')]"
        ),
        "protect your data abroad": Selector(
            By.XPATH, "//span[contains(text(),'Protect your data abroad')]"
        ),
        "placeholder lesson": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[5]/div/ul/li[1]/a/span"
        ),
        "back" : Selector(
            By.XPATH, "//body/div[7]/div/div/div/div[1]/a"
        ),
        "ok button": Selector(
            By.XPATH, "//button[contains(text(),'Ok')]"
        ),
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
