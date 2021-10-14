# -*- coding: utf-8 -*-
"""Find a Supplier - ISD Search Results Page Object."""
import logging
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import common_selectors
from browserpages.common_actions import Selector, check_for_sections, check_url

NAME = "Search results"
SERVICE = Service.ISD
TYPE = PageType.SEARCH_RESULTS
URL = URLs.ISD_SEARCH.absolute
PAGE_TITLE = "Find a UK specialist"

SELECTORS = {
    "results summary": {
        "number of results": Selector(By.CSS_SELECTOR, "#hero-container h2")
    },
    "search form": {
        "itself": Selector(By.ID, "#id_q-container"),
        "search box label": Selector(By.CSS_SELECTOR, "label[for=id_q]"),
        "search box": Selector(By.CSS_SELECTOR, "#id_q"),
        # "search button": Selector(By.CSS_SELECTOR, ""),
    },
    "filters": {
        "itself": Selector(By.CSS_SELECTOR, "#filter-column"),
        "title": Selector(By.CSS_SELECTOR, "#filter-column span"),
        "filter by expertise": Selector(
            By.CSS_SELECTOR, "#filter-column > fieldset:nth-child(2)"
        ),
        "regional expertise": Selector(By.CSS_SELECTOR, "#toggle_id_expertise_regions"),
        "industry expertise": Selector(By.CSS_SELECTOR, "#toggle_id_expertise_industries"),
        "language expertise": Selector(By.CSS_SELECTOR, "#toggle_id_expertise_languages"),
        "international expertise": Selector(By.CSS_SELECTOR, "#toggle_id_expertise_countries"),
        "filter by services": Selector(
            By.CSS_SELECTOR, "#filter-column > fieldset:nth-child(3)"
        ),
        "financial": Selector(By.CSS_SELECTOR, "#toggle_id_expertise_products_services_financial"),
        "management consulting": Selector(
            By.CSS_SELECTOR, "#toggle_id_expertise_products_services_management"
        ),
        "human resources and recruitment": Selector(
            By.CSS_SELECTOR, "#toggle_id_expertise_products_services_human_resources"
        ),
        "publicity and communications": Selector(
            By.CSS_SELECTOR, "#toggle_id_expertise_products_services_publicity"
        ),
        "legal": Selector(By.CSS_SELECTOR, "#toggle_id_expertise_products_services_legal"),
        "business support": Selector(
            By.CSS_SELECTOR, "#toggle_id_expertise_products_services_business_support"
        ),
    },
    "search results": {
        "itself": Selector(By.CSS_SELECTOR, "#companies-column"),
        "result links": Selector(By.CSS_SELECTOR, "#companies-column ul li a"),
    },
}
SELECTORS.update(common_selectors.INTERNATIONAL_HEADER_WO_LANGUAGE_SELECTOR)
SELECTORS.update(common_selectors.BREADCRUMBS)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.INTERNATIONAL_FOOTER)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)
    logging.debug("All expected elements are visible on '%s' page", NAME)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)

def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)
