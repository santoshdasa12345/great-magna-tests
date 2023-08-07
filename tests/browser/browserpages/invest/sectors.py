# -*- coding: utf-8 -*-
"""Regional landing page."""
import logging
from typing import List

from browserpages import common_selectors
from browserpages.common_actions import (
    Selector,
    check_for_sections,
    check_url,
    go_to_url,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service

NAME = "Regions"
SERVICE = Service.INTERNATIONAL
TYPE = PageType.LANDING
URL = URLs.INVEST_SECTORS.absolute
PAGE_TITLE = "Invest in Great Britain - "

SELECTORS = {
    "regions list": {
        "scotland": Selector(By.PARTIAL_LINK_TEXT, "Scotland"),
        "northern ireland": Selector(By.PARTIAL_LINK_TEXT, "Northern Ireland"),
        "north of england": Selector(By.PARTIAL_LINK_TEXT, "North of England"),
        "wales": Selector(By.PARTIAL_LINK_TEXT, "Wales"),
        "midlands": Selector(By.PARTIAL_LINK_TEXT, "Midlands"),
        "south of england": Selector(By.PARTIAL_LINK_TEXT, "South of England"),
    },
    # "the uk map": {
    #     "the uk map - svg": Selector(By.CSS_SELECTOR, "svg.uk-map"),
    #     "scotland - svg": Selector(By.ID, "scotland"),
    #     "northern ireland - svg": Selector(By.ID, "northern-ireland"),
    #     "north of england - svg": Selector(By.ID, "north-england"),
    #     "wales - svg": Selector(By.ID, "wales"),
    #     "midlands - svg": Selector(By.ID, "midlands"),
    #     "south of england - svg": Selector(By.ID, "south-england"),
    # },
    "the uk map": {
        "the uk map - svg": Selector(
            By.CSS_SELECTOR,
            "#content > div.atlas-hero__heading > div > div > div.atlas-grid__column.atlas-grid__column--5-12-m.atlas-grid__column--offset-1-m > div > svg",
        ),
        "scotland - svg": Selector(
            By.CSS_SELECTOR,
            "#atlas-map-scotland > g.atlas-map__shape > path:nth-child(8)",
        ),
        "northern ireland - svg": Selector(
            By.CSS_SELECTOR, "#atlas-map-northern-ireland > g.atlas-map__shape > path"
        ),
        "north of england - svg": Selector(
            By.XPATH, "//body/main/div[2]/div/div/div[2]/div/svg/g/a[2]/g/g[1]/path"
        ),
        "wales - svg": Selector(
            By.CSS_SELECTOR, "#atlas-map-wales > g.atlas-map__shape > path"
        ),
        "midlands - svg": Selector(
            By.CSS_SELECTOR, "#atlas-map-midlands > g.atlas-map__shape > path"
        ),
        "south of england - svg": Selector(
            By.CSS_SELECTOR,
            "#atlas-map-south-england > g.atlas-map__shape > path:nth-child(1)",
        ),
    },
    "contact us": {"get in touch": Selector(By.PARTIAL_LINK_TEXT, "Get in touch")},
}
SELECTORS.update(common_selectors.INTERNATIONAL_HEADER_WO_LANGUAGE_SELECTOR)
SELECTORS.update(common_selectors.INTERNATIONAL_HERO)
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
