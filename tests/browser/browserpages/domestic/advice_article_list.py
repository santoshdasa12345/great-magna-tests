# -*- coding: utf-8 -*-
"""Domestic Common Advice Page Object."""
import logging
import random
from typing import List
from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from great_magna_tests_shared.utils import extract_attributes_by_css
from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Selector,
    check_for_sections,
    check_url,
    go_to_url,
    wait_for_page_load_after_action,
)
from browserpages.domestic import actions as domestic_actions

NAME = "Advice article list"
SERVICE = Service.DOMESTIC
TYPE = PageType.ARTICLE_LIST
URL = URLs.DOMESTIC_ADVICE.absolute
PAGE_TITLE = "Welcome to great.gov.uk"
NAMES = [
    "Create an export plan",
    "Find an export market",
    "Choose a route to market",
    "Get export finance",
    "Manage payment for export orders",
    "Prepare to do business in a foreign country",
    "Prepare for export procedures and logistics",
    "Sell services overseas",
    "Manage risk of bribery and corruption",
    # "Upskill now",
]
SubURLs = {
    "create an export plan": urljoin(URL, "create-an-export-plan"),
    "find an export market": urljoin(URL, "find-an-export-market/"),
    "choose a route to market": urljoin(URL, "choose-route-market/"),
    "get export finance": urljoin(URL, "get-export-finance-and-funding/"),
    "manage payment for export orders": urljoin(
        URL, "manage-payment-export-orders/"
    ),
    "prepare to do business in a foreign country": urljoin(
        URL, "prepare-to-do-business-in-a-foreign-country/"
    ),
    "prepare for export procedures and logistics": urljoin(
        URL, "prepare-for-export-procedures-and-logistics/"
    ),
    "sell services overseas": urljoin(
        URL, "sell-services-overseas/"
    ),
    "manage risk of bribery and corruption": urljoin(
        URL, "manage-risk-bribery-and-corruption/"
    ),
    # "upskill now": urljoin(
    #     URL, "signup/?next=/learn/categories/"
    # ),
}

ARTICLE_LINKS = Selector(
    By.CSS_SELECTOR, "#article-list-page li.article a", type=ElementType.LINK
)
SELECTORS = {
    "breadcrumbs": {
        "itself": Selector(By.CSS_SELECTOR, "nav.breadcrumbs"),
        "links": Selector(By.CSS_SELECTOR, "nav.breadcrumbs a"),
    },
    "list of articles": {
        "itself": Selector(By.ID, "article-list-page"),
        "articles": ARTICLE_LINKS,
    },
    "error reporting": {
        "itself": Selector(By.CSS_SELECTOR, "section.error-reporting"),
        "link": Selector(By.ID, "error-reporting-section-contact-us"),
    },
    # "upskill now": {
    #     "itself": Selector(By.CSS_SELECTOR, "#article-list-page > div:nth-child(2) > div > div.cta-container > a"),
    # },
}
SELECTORS.update(common_selectors.DOMESTIC_HEADER)
SELECTORS.update(common_selectors.DOMESTIC_HERO_WO_LINK)
SELECTORS.update(common_selectors.DOMESTIC_FOOTER)


def clean_name(name: str) -> str:
    return name.split(" - ")[1].strip()


def visit(driver: WebDriver, *, page_name: str = None):
    url = SubURLs[page_name] if page_name else URL
    go_to_url(driver, url, page_name or NAME)


def should_be_here(driver: WebDriver, *, page_name: str):
    check_url(driver, URL, exact_match=False)
    logging.debug("All expected elements are visible on '%s' page", PAGE_TITLE)


def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def open_any_article(driver: WebDriver) -> str:
    article_links = extract_attributes_by_css(
        driver.page_source, ARTICLE_LINKS.value, attrs=["href"]
    )
    article_link = random.choice(article_links)

    link = driver.find_element_by_css_selector(f"a[href='{article_link['href']}']")
    with wait_for_page_load_after_action(driver):
        link.click()
    return article_link["text"]


def search(driver: WebDriver, phrase: str):
    domestic_actions.search(driver, phrase)
