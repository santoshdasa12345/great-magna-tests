# -*- coding: utf-8 -*-
"""Events Event Page Object."""
from browserpages.common_actions import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from great_magna_tests_shared.utils import check_url_path_matches_template

NAME = "Event"
SERVICE = Service.EVENTS
TYPE = PageType.EVENT
URL = URLs.EVENTS_EVENT.absolute_template
GREAT_LOGO = Selector(By.CSS_SELECTOR, "div.event-logo")
SELECTORS = {
    "general": {"great.gov.uk logo": GREAT_LOGO},
    "breadcrumbs": Selector(By.CSS_SELECTOR, ".breadcrumbs div>a"),
}


def should_be_here(driver: WebDriver):
    check_url_path_matches_template(URL, driver.current_url)
