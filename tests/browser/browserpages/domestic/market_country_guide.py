# -*- coding: utf-8 -*-
"""Domestic - Country Guide page"""
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
from browserpages.domestic import actions as domestic_actions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from great_magna_tests_shared.utils import check_url_path_matches_template

NAME = "Markets"
SERVICE = Service.DOMESTIC
TYPE = PageType.GUIDE
URL = URLs.DOMESTIC_MARKETS_GUIDE.absolute_template

NAMES = [
    "Brazil",
    "China",
    "Denmark",
    "Germany",
    "Ireland",
    "Italy",
    "Japan",
    "Morocco",
    "South Korea",
    "The Netherlands",
    "Turkey",
]
SubURLs = {
    "brazil": URL.format(country="brazil"),
    "china": URL.format(country="china"),
    "denmark": URL.format(country="denmark"),
    "germany": URL.format(country="germany"),
    "ireland": URL.format(country="ireland"),
    "italy": URL.format(country="italy"),
    "japan": URL.format(country="japan"),
    "morocco": URL.format(country="morocco"),
    "south korea": URL.format(country="south-korea"),
    "the netherlands": URL.format(country="netherlands"),
    "turkey": URL.format(country="turkey"),
}
SELECTORS = {
    "description": {
        # "intro": Selector(By.ID, "country-guide-teaser-section"),
        "description": Selector(By.ID, "country-guide-section-one"),
        "statistics": Selector(By.ID, "country-guide-statistics-section"),
    },
    "opportunities for exporters": {
        "self": Selector(By.ID, "country-guide-section-two"),
        "accordions": Selector(By.ID, "country-guide-accordions"),
    },
    "doing business in": {"self": Selector(By.ID, "country-guide-section-three")},
    "next steps": {
        "self": Selector(By.ID, "country-guide-need-help-section"),
        "read more advice about doing business abroad": Selector(
            By.CSS_SELECTOR,
            "#country-guide-need-help-section a[href='/advice/']",
            type=ElementType.LINK,
        ),
        "get in touch with one of our trade advisers": Selector(
            By.CSS_SELECTOR,
            "#country-guide-need-help-section a[href$='office-finder/']",
            type=ElementType.LINK,
        ),
    },
    "next steps staging": {
        "check duties and customs procedures for exporting goods": Selector(
            By.CSS_SELECTOR,
            "#country-guide-need-help-section > div > div:nth-child(2) > div:nth-child(2) > div > div > a",
            type=ElementType.LINK,
            is_visible=False,
        ),
    },
    "compare now": {
        "self": Selector(
            By.CSS_SELECTOR,
            "#country-guide-learning-banner > div > div > div.cta-container > a",
        ),
    },
}
SELECTORS.update(common_selectors.DOMESTIC_HEADER)
SELECTORS.update(common_selectors.DOMESTIC_HERO_WO_LINK)
SELECTORS.update(common_selectors.BREADCRUMBS)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.DOMESTIC_FOOTER)


def visit(driver: WebDriver, *, page_name: str = None):
    url = SubURLs[page_name] if page_name else URL
    go_to_url(driver, url, page_name or NAME)


def should_be_here(driver: WebDriver, *, page_name: str = None):
    check_url_path_matches_template(URL, driver.current_url)


def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def search(driver: WebDriver, phrase: str):
    domestic_actions.search(driver, phrase)


def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()
