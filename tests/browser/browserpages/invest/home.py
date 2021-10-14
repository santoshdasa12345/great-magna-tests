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
URL = URLs.INVEST_HOME.absolute
SERVICE = Service.INVEST
TYPE = PageType.LANDING
PAGE_TITLE = "Invest in Great Britain - Home"

SELECTORS = {
    "header": {
        "self": Selector(By.ID, "body > header > div.atlas-header__main"),
        "logo": Selector(By.XPATH, "//body/header/div[2]/div/a/img"),
        # "invest in the uk": Selector(By.CSS_SELECTOR, "#atlas-nav > ul > li:nth-child(1) > a"),
        # "buy from the uk": Selector(By.CSS_SELECTOR, "#atlas-nav > ul > li:nth-child(2) > a"),
        # "contact": Selector(By.CSS_SELECTOR, "#atlas-nav > ul > li:nth-child(3) > a"),
        "dit logo": Selector(By.ID, "body > header > div.atlas-header__global > div > img"),
    },
    "home": {
        "invest in the uk": Selector(By.CSS_SELECTOR, "#atlas-nav > ul > li:nth-child(1) > a"),
        "buy from the uk header": Selector(By.PARTIAL_LINK_TEXT, "Buy from the UK", type=ElementType.LINK),
        "contact": Selector(By.CSS_SELECTOR, "#atlas-nav > ul > li:nth-child(3) > a"),
        "get started": Selector(By.CSS_SELECTOR, "#content > div > div.atlas-container.atlas-p-b-xl > div > a"),
        "find investment opportunities": Selector(By.CSS_SELECTOR, "#content > div > div.atlas-container.atlas-p-b-xl > nav > a:nth-child(1)"),
        "find a uk specialist": Selector(By.CSS_SELECTOR, "#content > div > div.atlas-container.atlas-p-b-xl > nav > a:nth-child(2)"),
        "buy from the uk": Selector(By.CSS_SELECTOR, "#content > div > div.atlas-container.atlas-p-b-xl > nav > a:nth-child(3)"),
        "contact dit": Selector(By.CSS_SELECTOR, "#content > div > div.atlas-container.atlas-p-b-xl > nav > a:nth-child(4)"),
    },
    "sub heading": {
        "self": Selector(By.ID, "body > header > div.atlas-subnav > div > nav"),
        "why invest in the uk": Selector(By.CSS_SELECTOR, "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(1) > a"),
        "uk nations and regions": Selector(By.CSS_SELECTOR, "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(2) > a"),
        "sectors": Selector(By.CSS_SELECTOR, "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(3) > a"),
        "investment opportunities": Selector(By.CSS_SELECTOR, "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(4) > a"),
        "how we can help": Selector(By.CSS_SELECTOR, "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(5) > a"),
        "invest in the uk": Selector(By.CSS_SELECTOR, "#content > div.atlas-landing__hero"),

    },

    "why invest in the uk": {
        "why invest in the section": Selector(By.CSS_SELECTOR, "#content > div:nth-child(4)"),
        "reason": Selector(By.CSS_SELECTOR, "#content > div:nth-child(4) > div > div.atlas-grid.atlas-grid--masonry > div:nth-child(3) > a"),

    },
    "uk sectors": {
        "uk sectors section": Selector(By.CSS_SELECTOR, "#content > div:nth-child(5)"),
        "uk sectors": Selector(By.CSS_SELECTOR,
                           "#content > div:nth-child(5) > div > div.atlas-grid.atlas-grid--masonry > div:nth-child(3) > a"),

    },
    "uk regions": {
        "uk regions section": Selector(By.CSS_SELECTOR, "#with-regions-map"),
        "regions": Selector(By.CSS_SELECTOR,
                           "#with-regions-map > div > div.atlas-grid.atlas-grid--masonry > div:nth-child(3) > a"),

    },
    "investment opportunities": {
        "investment opportunities section": Selector(By.CSS_SELECTOR, "#content > div:nth-child(7)"),
        "investment opportunities": Selector(By.CSS_SELECTOR,
                           "#content > div:nth-child(7) > div > div.atlas-grid.atlas-grid--masonry > div:nth-child(3) > a"),

    },
    "how we can help": {
        "how we can help section": Selector(By.CSS_SELECTOR, "#content > div:nth-child(8)"),
        "how we can help": Selector(By.CSS_SELECTOR, "#content > div:nth-child(8) > div > div.atlas-grid.atlas-grid--masonry > div:nth-child(3) > a"),
    },
    "contact us": {
        "self": Selector(By.ID, "get-in-touch"),
        "heading": Selector(By.CSS_SELECTOR, "#get-in-touch h2"),
        "text": Selector(By.CSS_SELECTOR, "#get-in-touch p"),
        "speak to us": Selector(
            By.CSS_SELECTOR, "#get-in-touch a", type=ElementType.LINK
        ),
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
