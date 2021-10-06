# -*- coding: utf-8 -*-
"""UK Setup Guide - landing page."""
import logging
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import common_selectors
from browserpages.common_actions import (
    Selector,
    check_for_sections,
    check_url,
    find_element,
    go_to_url,
    take_screenshot,
)

NAME = "How to set up in the UK"
SERVICE = Service.INVEST
TYPE = PageType.LANDING
URL = URLs.INVEST_HOW_WE_CAN_HELP.absolute
PAGE_TITLE = "Invest In Great Britain - How we help you"


SELECTORS = {
    "hero": {"self": Selector(By.CSS_SELECTOR, "#content > section.hero")},
    "introduction": {
        "self": Selector(By.CSS_SELECTOR, "#content section.setup-guide .intro"),
        "header": Selector(By.CSS_SELECTOR, "#content section.setup-guide .intro h2"),
        "paragraph": Selector(By.CSS_SELECTOR, "#content section.setup-guide .intro p"),
    },
    "about us": {
        "about us section": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(1)"
        ),
        "about us image": Selector(
            By.CSS_SELECTOR,
            "#content > div.atlas-alternate-bg--3-tone > section:nth-child(1) > div > div > div.atlas-grid__column.atlas-grid__column--right.atlas-grid__column--6-12-m > div > img"
        ),
        "more": Selector(
            By.CSS_SELECTOR,
            "#content > div.atlas-alternate-bg--3-tone > section:nth-child(1) > div > div > div.atlas-grid__column.atlas-grid__column--left.atlas-grid__column--6-12-m > div > button"
        ),
        "less": Selector(
            By.CSS_SELECTOR,
            "#content > div.atlas-alternate-bg--3-tone > section:nth-child(1) > div > div > div.atlas-grid__column.atlas-grid__column--left.atlas-grid__column--6-12-m > div > button"
        ),
    },
    "how we are helping investors": {
        "how we are helping investors section": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(2)"
        ),
        "the office for investment": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(2) > div > div:nth-child(3) > div:nth-child(1) > div > h4 > a"
        ),
        "the venture capital unit": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(2) > div > div:nth-child(3) > div:nth-child(2) > div > h4 > a"
        ),
    },
    "how to expand to the uk": {
        "Establish a base for business in the UK": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(3) > div > div:nth-child(3) > div:nth-child(1) > div"
        ),
        "Get support to move your tech business to the UK": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(3) > div > div:nth-child(3) > div:nth-child(2) > div"
        ),
        "Register a company in the UK": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(3) > div > div:nth-child(3) > div:nth-child(3) > div"
        ),
        "Open a UK business bank account": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(3) > div > div:nth-child(3) > div:nth-child(4) > div"
        ),
        "Access finance in the UK": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(3) > div > div:nth-child(3) > div:nth-child(5) > div"
        ),
        "Research and development support in the UK": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(3) > div > div:nth-child(3) > div:nth-child(6) > div",
        ),
        "UK Visas and migration": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(3) > div > div:nth-child(3) > div:nth-child(7) > div"
        ),
        "Hire skilled workers for your UK Operations": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(3) > div > div:nth-child(3) > div:nth-child(8) > div"
        ),
        "UK tax and incentives": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(3) > div > div:nth-child(3) > div:nth-child(9) > div"
        ),
        "Find a UK Specialist": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(4) > div > div > div.atlas-grid__column.atlas-grid__column--left.atlas-grid__column--6-12-m > a"
        ),
        "Get in touch": Selector(
            By.CSS_SELECTOR, "#content > section > div > a"
        ),
    },
    "find a uk specialist": {
        "find a uk specialist section": Selector(
            By.CSS_SELECTOR, "#content > div.atlas-alternate-bg--3-tone > section:nth-child(4)"
        ),
        "find a uk specialist": Selector(
            By.CSS_SELECTOR,
            "#content > div.atlas-alternate-bg--3-tone > section:nth-child(4) > div > div > div.atlas-grid__column.atlas-grid__column--left.atlas-grid__column--6-12-m > a"
        ),
    },
    "get in touch": {
    "get in touch section": Selector(
        By.CSS_SELECTOR, "#content > section"
    ),
    "get in touch": Selector(
        By.CSS_SELECTOR,
        "#content > section > div > a"),
    },
}
SELECTORS.update(common_selectors.INVEST_HEADER)
SELECTORS.update(common_selectors.BETA_BAR)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.INVEST_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=True)
    logging.debug("All expected elements are visible on '%s' page", PAGE_TITLE)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def open_guide(driver: WebDriver, guide_name: str):
    guide_name = guide_name.split(" - ")[1].strip()
    selector = Selector(By.PARTIAL_LINK_TEXT, guide_name)
    logging.debug("Looking for: {}".format(guide_name))
    guide = find_element(driver, selector, element_name="Guide card", wait_for_it=False)
    guide.click()
    take_screenshot(driver, PAGE_TITLE + " after opening " + guide_name)
