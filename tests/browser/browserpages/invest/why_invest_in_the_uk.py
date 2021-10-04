# -*- coding: utf-8 -*-
"""Invest in Great Home Page Object."""
import logging
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Selector,
    check_for_sections,
    check_url,
    find_element,
    go_to_url,
)

NAME = "landing"
URL = URLs.INVEST_WHY_INVEST_IN_THE_UK.absolute
SERVICE = Service.INVEST
TYPE = PageType.LANDING
PAGE_TITLE = "Invest in Great Britain - Home"

SELECTORS = {
    "uk strengths": {
        "uk strengths section": Selector(By.CSS_SELECTOR, "#content > section.atlas-bg--grey-light"),
        "tax and incentives": Selector(By.CSS_SELECTOR, "#content > section.atlas-bg--grey-light > div > div > div:nth-child(1)"),
        "talent and labour": Selector(By.CSS_SELECTOR, "#content > section.atlas-bg--grey-light > div > div > div:nth-child(2)"),
    },
    "get in touch": {
        "get in touch section": Selector(By.CSS_SELECTOR, "#content > section"),
        "get in touch": Selector(By.CSS_SELECTOR,"#content > section > div > a"),
    },
}
SELECTORS.update(common_selectors.INVEST_HEADER)
SELECTORS.update(common_selectors.INVEST_HERO)
SELECTORS.update(common_selectors.BREADCRUMBS)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.INTERNATIONAL_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL)
    logging.debug("All expected elements are visible on '%s' page", PAGE_TITLE)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)

def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)

def clean_name(name: str) -> str:
    return name.split(" - ")[1].strip()


def open_industry(driver: WebDriver, industry_name: str):
    industry_name = clean_name(industry_name)
    selector = Selector(By.PARTIAL_LINK_TEXT, industry_name)
    logging.debug("Looking for: {}".format(industry_name))
    industry_link = find_element(
        driver, selector, element_name="Industry card", wait_for_it=False
    )
    industry_link.click()


def open_guide(driver: WebDriver, guide_name: str):
    guide_name = clean_name(guide_name)
    selector = Selector(By.PARTIAL_LINK_TEXT, guide_name)
    logging.debug("Looking for: {}".format(guide_name))
    guide = find_element(driver, selector, element_name="Guide card", wait_for_it=False)
    guide.click()
