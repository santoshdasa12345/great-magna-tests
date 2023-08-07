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
        "using ecommerce as a route to market": Selector(
            By.XPATH,
            "//body/main/div/section[2]/ol/li[1]/div/ul/li[2]/a"
            # "//span[contains(text(),'Selling direct to your customer')]"
        ),
        "selling direct to your customer": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[1]/div/ul/li[3]/a"
        ),
        "using an agent or distributor": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[1]/div/ul/li[4]/a"
        ),
        "using licensing": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[1]/div/ul/li[5]/a"
        ),
        "setting up joint ventures abroad": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[1]/div/ul/li[6]/a"
        ),
        "setting up a franchise abroad": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[1]/div/ul/li[7]/a"
        ),
        "setting up a business abroad": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[1]/div/ul/li[8]/a"
        ),
        "understand the local business culture": Selector(
            By.CSS_SELECTOR, "//body/main/div/section[2]/ol/li[2]/div/ul/li/a"
        ),
        "understand product liability": Selector(
            By.XPATH, "//span[contains(text(),'Understand product liability')]"
        ),
        "protect your intellectual property abroad": Selector(
            By.XPATH,
            "//span[contains(text(),'Protect your intellectual property abroad')]",
        ),
        "prepare for a trade mission": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[4]/div/ul/li[1]/a"
        ),
        "prepare for a trade show as an attendee": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[4]/div/ul/li[2]/a"
        ),
        "prepare for a trade show as an exhibitor": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[4]/div/ul/li[3]/a"
        ),
        "module_progress": Selector(
            By.CSS_SELECTOR,
            "#learn-root > section.learn__single-category-header > div > div > div:nth-child(1) > div.learn__single-category-header-content > div.learn__category-progress-container",
        ),
        "lessons_progress_bar": Selector(By.XPATH, '//*[@id="55"]/div/p'),
        "lesson_categories_progress": Selector(
            By.CSS_SELECTOR,
            "#learn-root > section > a:nth-child(3) > article > div > div.learn__category-content.learn__category-content--progress-bar > div.learn__category-progress-container > div",
        ),
        "pitching and tendering ina new market": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[6]/div/ul/li[1]/a"
        ),
        "how to draft a contract": Selector(
            By.XPATH, "//span[contains(text(),'How to draft a contract')]"
        ),
        "using samples demos and prototypes": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[6]/div/ul/li[3]/a"
        ),
        "how to handle price negotiations": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[6]/div/ul/li[4]/a"
        ),
        "protect your business from bribery and corruption": Selector(
            By.XPATH,
            "//span[contains(text(),'Protect your business from bribery and corruption')]",
        ),
        "how to operate with business integrity": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[5]/div/ul/li[2]/a"
        ),
        "protect your data abroad": Selector(
            By.XPATH, "//span[contains(text(),'Protect your data abroad')]"
        ),
        # "placeholder lesson": Selector(
        #     By.XPATH, "//body/main/div/section[2]/ol/li[5]/div/ul/li[1]/a/span"
        # ),
        "back": Selector(By.CSS_SELECTOR, "#learn-root > span > a"),
        "ok button": Selector(By.XPATH, "//button[contains(text(),'Ok')]"),
        "adapting your website for export": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[7]/div/ul/li[1]/a"
        ),
        "how to increase sales on your ecommerce website": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[7]/div/ul/li[2]/a"
        ),
        "understanding ecommerce platforms": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[7]/div/ul/li[3]/a"
        ),
        "using online marketplaces": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[7]/div/ul/li[4]/a"
        ),
        "how to localise your online market place": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[7]/div/ul/li[5]/a"
        ),
        "how to manage your inventory for multiple online channels": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[7]/div/ul/li[6]/a"
        ),
        "how to prepare for b2b crossborder sales": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[7]/div/ul/li[7]/a"
        ),
        "how to create digital marketing strategy": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[8]/div/ul/li[1]/a"
        ),
        "using social media to promote and sell internationally": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[8]/div/ul/li[2]/a"
        ),
        "using email marketing for international audiences": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[8]/div/ul/li[3]/a"
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
