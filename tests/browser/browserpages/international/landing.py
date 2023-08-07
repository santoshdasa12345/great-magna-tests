# -*- coding: utf-8 -*-
"""International - Landing page"""
import logging
from typing import List

from browserpages import common_selectors
from browserpages.common_actions import (
    Selector,
    check_for_sections,
    check_if_element_is_visible,
    check_url,
    find_element,
    find_selector_by_name,
    go_to_url,
    take_screenshot,
    wait_for_page_load_after_action,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service

NAME = "Landing"
SERVICE = Service.INTERNATIONAL
TYPE = PageType.HOME
URL = URLs.INTERNATIONAL_LANDING.absolute
PAGE_TITLE = "Welcome to great.gov.uk - buy from or invest in the UK"

SELECTORS = {
    "informative banner": {
        "banner": Selector(By.CSS_SELECTOR, "div.informative-banner"),
        "understand how the uk leaving the eu may affect your business": Selector(
            By.CSS_SELECTOR, "div.informative-banner a"
        ),
    },
    "service cards": {
        "service cards section": Selector(By.ID, "featured-cards-section"),
        "cards": Selector(By.CSS_SELECTOR, "#content div.card"),
        "expand to the uk": Selector(
            By.CSS_SELECTOR,
            "#featured-cards-section > div > div > div:nth-child(1) p:nth-child(2) > a:nth-child(1)",
        ),
        "capital investment in the uk": Selector(
            By.CSS_SELECTOR,
            "#featured-cards-section > div > div > div:nth-child(1) p:nth-child(2) > a:nth-child(2)",
        ),
        "how we help you buy from the uk": Selector(
            By.CSS_SELECTOR,
            "#featured-cards-section > div > div > div:nth-child(2) p:nth-child(2) > a:nth-child(1)",
        ),
    },
    "how dit provides help": {
        "how dit provides help section": Selector(
            By.CSS_SELECTOR, "#content > section:nth-child(4)"
        ),
        "help links": Selector(By.CSS_SELECTOR, "#content > section:nth-child(4) a"),
    },
    "tariffs": {
        "tariffs section": Selector(By.ID, "tariffs-section"),
        "continue with trade tariffs": Selector(
            By.CSS_SELECTOR, "#tariffs-section form button"
        ),
    },
    "featured links": {
        "featured links section": Selector(By.ID, "featured-links-section"),
        "featured links": Selector(By.CSS_SELECTOR, "#featured-links-section a"),
        "discover uk industries": Selector(
            By.CSS_SELECTOR,
            "#featured-links-section div.column-third-xl:nth-child(1) a",
        ),
        "how to set up in the uk": Selector(
            By.CSS_SELECTOR,
            "#featured-links-section div.column-third-xl:nth-child(2) a",
        ),
        "tell us what help you need": Selector(
            By.CSS_SELECTOR,
            "#featured-links-section div.column-third-xl:nth-child(3) a",
        ),
    },
    "study or visit the uk": {
        "study or visit the uk section": Selector(By.ID, "study-visit-cta-section"),
        "study in the uk": Selector(By.LINK_TEXT, "Study in the UK"),
        "visit the uk": Selector(By.LINK_TEXT, "Visit the UK"),
    },
    "get started": {
        "itself": Selector(
            By.CSS_SELECTOR,
            "#content > div > div.atlas-container.atlas-p-b-xl > div > a",
        ),
    },
    "invest in the uk": {
        "itself": Selector(
            By.CSS_SELECTOR,
            "#content > div > div.atlas-container.atlas-p-b-xl > nav > a:nth-child(1)",
        ),
    },
    "buy from the uk": {
        "itself": Selector(
            By.CSS_SELECTOR,
            "#content > div > div.atlas-container.atlas-p-b-xl > nav > a:nth-child(2)",
        ),
    },
    "contact dit": {
        "itself": Selector(
            By.CSS_SELECTOR,
            "#content > div > div.atlas-container.atlas-p-b-xl > nav > a:nth-child(3)",
        ),
    },
}
SELECTORS.update(common_selectors.INTERNATIONAL_HEADER)
SELECTORS.update(common_selectors.COOKIE_BANNER)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.INTERNATIONAL_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def open(driver: WebDriver, group: str, element: str, *, same_tab: bool = True):
    selector = SELECTORS[group.lower()][element.lower()]
    link = find_element(driver, selector, element_name=element, wait_for_it=False)
    check_if_element_is_visible(link, element_name=element)
    if same_tab:
        href = link.get_attribute("href")
        logging.debug("Opening '%s' link '%s' in the same tab", element, href)
        driver.get(href)
    else:
        with wait_for_page_load_after_action(driver):
            link.click()
    take_screenshot(driver, NAME + " after clicking on: %s link".format(element))


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()


def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)
