# -*- coding: utf-8 -*-
"""Invest in Great Home Page Object."""
import logging
from typing import List

from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Selector,
    check_for_sections,
    check_url,
    find_element,
    find_selector_by_name,
    go_to_url,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service

NAME = "landing"
URL = URLs.INVEST_LANDING.absolute
SERVICE = Service.INVEST
TYPE = PageType.LANDING
PAGE_TITLE = "Invest in Great Britain - Home"

SELECTORS = {
    "benefits": {
        "self": Selector(By.ID, "benefits"),
        "heading": Selector(By.CSS_SELECTOR, "#benefits h2"),
        "sub-section headings": Selector(By.CSS_SELECTOR, "#benefits h3"),
        "text": Selector(By.CSS_SELECTOR, "#benefits p"),
        "image": Selector(By.CSS_SELECTOR, "#benefits img"),
    },
    "landing": {
        "invest in the uk": Selector(
            By.CSS_SELECTOR, "#atlas-nav > ul > li:nth-child(1) > a"
        ),
        "buy from the uk header": Selector(
            By.PARTIAL_LINK_TEXT, "Buy from the UK", type=ElementType.LINK
        ),
        "contact": Selector(By.CSS_SELECTOR, "#atlas-nav > ul > li:nth-child(3) > a"),
        "get started": Selector(
            By.CSS_SELECTOR,
            "#content > div > div.atlas-container.atlas-p-b-xl > div > a",
        ),
        "find investment opportunities": Selector(
            By.CSS_SELECTOR,
            "#content > div > div.atlas-container.atlas-p-b-xl > nav > a:nth-child(1)",
        ),
        "find a uk specialist": Selector(
            By.CSS_SELECTOR,
            "#content > div > div.atlas-container.atlas-p-b-xl > nav > a:nth-child(2)",
        ),
        "buy from the uk": Selector(
            By.CSS_SELECTOR,
            "#content > div > div.atlas-container.atlas-p-b-xl > nav > a:nth-child(3)",
        ),
        "contact dit": Selector(
            By.CSS_SELECTOR,
            "#content > div > div.atlas-container.atlas-p-b-xl > nav > a:nth-child(4)",
        ),
    },
    "sectors": {
        "self": Selector(By.ID, "industries"),
        "heading": Selector(By.CSS_SELECTOR, "#industries h2"),
        "heading text": Selector(By.CSS_SELECTOR, "#industries h2 ~ div > p"),
        "first": Selector(By.CSS_SELECTOR, "#industries div:nth-child(1) > div > a"),
        "second": Selector(By.CSS_SELECTOR, "#industries div:nth-child(2) > div > a"),
        "third": Selector(By.CSS_SELECTOR, "#industries div:nth-child(3) > div > a"),
        "see more industries": Selector(By.ID, "see-more-industries"),
    },
    "high-potential opportunities": {
        "hpo - section": Selector(By.ID, "high-potential-opportunities"),
        "hpo - headings": Selector(By.CSS_SELECTOR, "#high-potential-opportunities h2"),
        "hpo - texts": Selector(
            By.CSS_SELECTOR, "#high-potential-opportunities h2 ~ div > p"
        ),
        "aquaculture": Selector(By.PARTIAL_LINK_TEXT, "Aquaculture"),
        # "high productivity food production": Selector(
        #     By.PARTIAL_LINK_TEXT, "High productivity food production"
        # ),
        # "high productivity food production (dev)": Selector(
        #     By.PARTIAL_LINK_TEXT, "High productivity food production"
        # ),
        # "high productivity food production (staging)": Selector(
        #     By.PARTIAL_LINK_TEXT, "High productivity food production"
        # ),
        "lightweight": Selector(By.PARTIAL_LINK_TEXT, "Lightweight structures"),
        "photonics": Selector(By.PARTIAL_LINK_TEXT, "Photonics and Microelectronics"),
        "rail": Selector(By.PARTIAL_LINK_TEXT, "Rail infrastructure"),
        "space": Selector(By.PARTIAL_LINK_TEXT, "Space"),
        "sustainable packaging": Selector(
            By.PARTIAL_LINK_TEXT, "Sustainable packaging"
        ),
    },
    "how we help": {
        "how we help - section": Selector(By.ID, "how-we-help"),
        "how we help - icons": Selector(By.CSS_SELECTOR, "#how-we-help ul li img"),
        "how we help - texts": Selector(By.CSS_SELECTOR, "#how-we-help ul li p"),
        "find out more": Selector(
            By.CSS_SELECTOR, "#how-we-help a", type=ElementType.LINK
        ),
    },
    "contact us": {
        "self": Selector(By.ID, "get-in-touch"),
        "heading": Selector(By.CSS_SELECTOR, "#get-in-touch h2"),
        "text": Selector(By.CSS_SELECTOR, "#get-in-touch p"),
        "speak to us": Selector(
            By.CSS_SELECTOR, "#get-in-touch a", type=ElementType.LINK
        ),
    },
    "logo": Selector(By.XPATH, "//body/header/div[2]/div/a"),
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
