# -*- coding: utf-8 -*-
"""International - Industry"""
import logging
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import common_selectors
from browserpages.common_actions import (
    Selector,
    assertion_msg,
    check_for_sections,
    check_url,
    go_to_url,
)

NAME = "Industry"
NAMES = [
    "Clean agritech",
    "Carbon capture usage and storage",
    "Chemicals",
    "Civil nuclear"
    "Green finance",
    "Greener buildings",
    "Hydrogen",
    "Jet zero and green ships",
    "Scotland",
    "sustainable infrastructure",
    "Aerospace",
    "Agricultural technology",
    "Automotive",
    "Creative industries",
    "Cyber security",
    "Education",
    "Energy",
    "Engineering and manufacturing",
    "Financial and professional services",
    "Financial services",
    "Food and drink",
    "Health and Life Sciences",
    "Healthcare and Life Sciences",
    "Industry",
    "Legal services",
    "Maritime",
    "Nuclear energy",
    "Offshore Wind"
    "Real Estate",
    "Retail",
    "Space",
    "Sports economy",
    "Technology",
    "Zero emission vehicles"
]
SERVICE = Service.INTERNATIONAL
TYPE = PageType.INDUSTRY
URL = URLs.INTERNATIONAL_INDUSTRIES.absolute
PAGE_TITLE = "great.gov.uk International - "


SubURLs = {
    "industry": URL,
    "clean agritech": URLs.INTERNATIONAL_INDUSTRY_AGRI_TECH.absolute,
    "carbon capture usage and storage": URLs.INTERNATIONAL_INDUSTRY_CARBON_CAPTURE_USAGE_AND_STORAGE.absolute,
    "chemicals": URLs.INTERNATIONAL_INDUSTRY_CHEMICALS.absolute,
    "civil nuclear" : URLs.INTERNATIONAL_INDUSTRY_CIVIL_NUCLEAR.absolute,
    "green finance": URLs.INTERNATIONAL_INDUSTRY_GREEN_FINANCE.absolute,
    "greener buildings": URLs.INTERNATIONAL_INDUSTRY_GREENER_BUILDINGS.absolute,
    "hydrogen": URLs.INTERNATIONAL_INDUSTRY_HYDROGEN.absolute,
    "jet zero and green ships": URLs.INTERNATIONAL_INDUSTRY_JET_ZERO_AND_GREEN_SHIPS.absolute,
    "offshore wind" : URLs.INTERNATIONAL_INDUSTRY_OFFSHORE_WIND.absolute,
    # "scotland": URLs.INTERNATIONAL_INDUSTRY_SCOTLAND.absolute,
    "sustainable infrastructure": URLs.INTERNATIONAL_INDUSTRY_SUSTAINABLE_INFRASTRUCTURE.absolute,
    # "aerospace": URLs.INTERNATIONAL_INDUSTRY_AEROSPACE.absolute,
    # "agricultural technology": URLs.INTERNATIONAL_INDUSTRY_AGRICULTURAL_TECHNOLOGY.absolute,
    # "automotive": URLs.INTERNATIONAL_INDUSTRY_AUTOMOTIVE.absolute,
    # "creative industries": URLs.INTERNATIONAL_INDUSTRY_CREATIVE_INDUSTRIES.absolute,
    # "cyber security": URLs.INTERNATIONAL_INDUSTRY_CYBER_SECURITY.absolute,
    # "education": URLs.INTERNATIONAL_INDUSTRY_EDUCATION.absolute,
    # "energy": URLs.INTERNATIONAL_INDUSTRY_ENERGY.absolute,
    # "engineering and manufacturing": URLs.INTERNATIONAL_INDUSTRY_ENGINEERING_AND_MANUFACTURING.absolute,
    # "financial and professional services": URLs.INTERNATIONAL_INDUSTRY_FINANCIAL_AND_PROFESSIONAL_SERVICES.absolute,
    # "financial services": URLs.INTERNATIONAL_INDUSTRY_FINANCIAL_SERVICES.absolute,
    # "food and drink": URLs.INTERNATIONAL_INDUSTRY_FOOD_AND_DRINK.absolute,
    # "health and life sciences": URLs.INTERNATIONAL_INDUSTRY_HEALTH_AND_LIFE_SCIENCES.absolute,
    # "healthcare and life sciences": URLs.INTERNATIONAL_INDUSTRY_HEALTH_AND_LIFE_SCIENCES.absolute,
    # "legal services": URLs.INTERNATIONAL_INDUSTRY_LEGAL_SERVICES.absolute,
    # "maritime": URLs.INTERNATIONAL_INDUSTRY_MARITIME.absolute,
    # "nuclear energy": URLs.INTERNATIONAL_INDUSTRY_NUCLEAR_ENERGY.absolute,
    # "real estate": URLs.INTERNATIONAL_INDUSTRY_REAL_ESTATE.absolute,
    # "retail": URLs.INTERNATIONAL_INDUSTRY_RETAIL.absolute,
    # "space": URLs.INTERNATIONAL_INDUSTRY_SPACE.absolute,
    # "sports economy": URLs.INTERNATIONAL_INDUSTRY_SPORTS_ECONOMY.absolute,
    # "technology": URLs.INTERNATIONAL_INDUSTRY_TECHNOLOGY.absolute,
    "zero emission vehicles" : URLs.INTERNATIONAL_INDUSTRY_ZERO_EMISSION_VEHICLES.absolute,
}

SELECTORS = {
    "industry breadcrumbs": {
        # "great.gov.uk international": Selector(
        #     By.CSS_SELECTOR, "#breadcrumb-section ol > li:nth-child(1) > a"
        # ),
        # "industries": Selector(
        #     By.CSS_SELECTOR, "#breadcrumb-section ol > li:nth-child(2) > a"
        # ),
    },
    "content": {
        "carbon capture usage and storage": Selector(By.CSS_SELECTOR, "#content > section.atlas-container > div:nth-child(2) > div:nth-child(1) > a"),
        "chemicals": Selector(By.CSS_SELECTOR, "#content > section.atlas-container > div:nth-child(2) > div:nth-child(2) > a"),
        "civil nuclear": Selector(By.CSS_SELECTOR, "#content > section.atlas-container > div:nth-child(2) > div:nth-child(3) > a"),
        "clean agritech": Selector(By.CSS_SELECTOR, "#content > section.atlas-container > div:nth-child(2) > div:nth-child(4) > a"),
        "green finance": Selector(By.CSS_SELECTOR, "#content > section.atlas-container > div:nth-child(2) > div:nth-child(5) > a"),
        "greener buildings": Selector(By.CSS_SELECTOR, "#content > section.atlas-container > div:nth-child(2) > div:nth-child(6) > a"),
        "hydrogen": Selector(By.CSS_SELECTOR, "#content > section.atlas-container > div:nth-child(2) > div:nth-child(7) > a"),
        "jet zero and green ships": Selector(By.CSS_SELECTOR, "#content > section.atlas-container > div:nth-child(2) > div:nth-child(8) > a"),
        "offshore wind": Selector(By.CSS_SELECTOR, "#content > section.atlas-container > div:nth-child(2) > div:nth-child(9) > a"),
        "sustainable infrastructure": Selector(By.CSS_SELECTOR, "#content > section.atlas-container > div:nth-child(2) > div:nth-child(10 > a)"),
        "zero emission vehicles": Selector(By.CSS_SELECTOR, "#content > section.atlas-container > div:nth-child(2) > div:nth-child(11) > a"),

    },

    "opportunity highlights": {
        "itself": Selector(By.CSS_SELECTOR, "#content > div.atlas-alternate-bg > section:nth-child(2)"),
        },
    "commercial maturity": {
        "itself": Selector(By.CSS_SELECTOR, "#content > div.atlas-alternate-bg > section:nth-child(3)"),
        },
    "key uk assets": {
        "itself": Selector(By.CSS_SELECTOR, "#content > div.atlas-alternate-bg > section:nth-child(4)"),
        },
    "r&d capability": {
        "itself": Selector(By.CSS_SELECTOR, "#content > div.atlas-alternate-bg > section:nth-child(5)"),
        },
    "business and government support": {
        "itself": Selector(By.CSS_SELECTOR, "#content > div.atlas-alternate-bg > section:nth-child(6)"),
        },
    "case studies": {
        "itself": Selector(By.CSS_SELECTOR, "#content > div.atlas-alternate-bg > section:nth-child(7)"),
        },
    "early potential opportunities": {
        "itself": Selector(By.CSS_SELECTOR, "#content > section"),
        },

}
SELECTORS.update(common_selectors.INTERNATIONAL_HEADER)
SELECTORS.update(common_selectors.INTERNATIONAL_HERO)
SELECTORS.update(common_selectors.BREADCRUMBS)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.INTERNATIONAL_FOOTER)


def visit(driver: WebDriver, *, page_name: str = None):
    url = SubURLs[page_name] if page_name else URL
    go_to_url(driver, url, page_name or NAME)


def should_be_here(driver: WebDriver, *, page_name: str):
    url = SubURLs[page_name.lower()] if page_name else URL
    check_url(driver, url, exact_match=False)
    logging.debug("All expected elements are visible on '%s' page", PAGE_TITLE)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def clean_name(name: str) -> str:
    return name.split(" - ")[1].strip()


def should_see_content_for(driver: WebDriver, industry_name: str):
    source = driver.page_source
    industry_name = clean_name(industry_name)
    logging.debug("Looking for: {}".format(industry_name))
    with assertion_msg(
        "Expected to find term '%s' in the source of the page %s",
        industry_name,
        driver.current_url,
    ):
        assert industry_name.lower() in source.lower()

def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)
