# -*- coding: utf-8 -*-
"""Domestic - Services page"""
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType, common_selectors
from browserpages.common_actions import Selector, check_for_sections, check_url, go_to_url
from browserpages.domestic import actions as domestic_actions

NAME = "Services"
SERVICE = Service.DOMESTIC
TYPE = PageType.LISTING
URL = URLs.DOMESTIC_SERVICES.absolute

SELECTORS = {
    "services": {
        "service cards": Selector(By.CSS_SELECTOR, "div.card"),
        "create a business profile": Selector(
            By.CSS_SELECTOR, "#services-list-section > div > div > div:nth-child(1) > div > div > a.card__link.card__link--focused > div",
            type=ElementType.LINK
        ),
        "find online marketplaces": Selector(
            By.CSS_SELECTOR, "#services-list-section > div > div > div:nth-child(2) > div > div > a.card__link.card__link--focused > div",
            type=ElementType.LINK
        ),
        "find export opportunities": Selector(
            By.CSS_SELECTOR, "#services-list-section > div > div > div:nth-child(3) > div > div > a.card__link.card__link--focused > div",
            type=ElementType.LINK
        ),
        "uk export finance": Selector(
            By.CSS_SELECTOR, "#services-list-section > div > div > div:nth-child(4) > div > div > a.card__link.card__link--focused > div",
            type=ElementType.LINK
        ),
        "find events and visits": Selector(
            By.CSS_SELECTOR, "#services-list-section > div > div > div:nth-child(5) > div > div > a.card__link.card__link--focused > div",
            type=ElementType.LINK
        ),
        "get an eori number": Selector(
            By.CSS_SELECTOR, "#services-list-section > div > div > div:nth-child(6) > div > div > a.card__link.card__link--focused > div",
            type=ElementType.LINK
        ),
        "report a trade barrier": Selector(
            By.CSS_SELECTOR, "#services-list-section > div > div > div:nth-child(7) > div > div > a.card__link.card__link--focused > div",
            type=ElementType.LINK
        ),
    }

}
SELECTORS.update(common_selectors.DOMESTIC_HEADER)
SELECTORS.update(common_selectors.SSO_LOGGED_OUT)
SELECTORS.update(common_selectors.BREADCRUMBS)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.DOMESTIC_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL)


def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def search(driver: WebDriver, phrase: str):
    domestic_actions.search(driver, phrase)

