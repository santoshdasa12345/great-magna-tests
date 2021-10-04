# -*- coding: utf-8 -*-
"""Invest in Great - HPO Page Object."""
import logging
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Selector,
    assertion_msg,
    check_for_sections,
    check_if_element_is_not_visible,
    check_url,
    find_element,
    get_selectors,
    go_to_url,
    scroll_to,
)

NAME = "HPO"
NAMES = [
    "Aquaculture",
    "High productivity food production",
    "Lightweight",
    "Photonics",
    "Rail",
    "Space",
    "Sustainable packaging",
    "chemicals in the humber",
    "carbon fibre in tees valley",
    "circular economy",
    "compound semiconductors and application",
    "food processing automation",
    "fusion energy",
    "heat networks",
    "hydrogen",
    "immersive technology",
    "marine autonomy",
    "net zero transport",
    "plant based and alternative protein products",
    "precision farming",
    "smart and sustainable avaiation",
    "spalding battery energy storage system",
    "innovation in animal health",

]
SERVICE = Service.INVEST
TYPE = PageType.HPO
URL = URLs.INVEST_HPO.absolute
PAGE_TITLE = "high potential"


SubURLs = {
    "aquaculture": URLs.INVEST_HPO_AQUACULTURE.absolute,
    "high productivity food production": URLs.INVEST_HPO_HIGH_PRODUCTIVITY_FOOD.absolute,
    "lightweight": URLs.INVEST_HPO_LIGHTWEIGHT.absolute,
    "photonics": URLs.INVEST_HPO_PHOTONICS.absolute,
    "rail": URLs.INVEST_HPO_RAIL.absolute,
    "space": URLs.INVEST_HPO_SPACE.absolute,
    "sustainable packaging": URLs.INVEST_HPO_SUSTAINABLE_PACKAGING.absolute,
    "chemicals in the humber": URLs.INVEST_HPO_CHEMICALS_IN_THE_HUMBER.absolute,
    "carbon fibre in tees valley": URLs.INVEST_HPO_CARBON_FIBRE_IN_TEES_VALLEY.absolute,
    "circular economy": URLs.INVEST_HPO_CIRCULAR_ECONOMY_IN_TELFORD.absolute,
    "compound semiconductors and application": URLs.INVEST_HPO_COMPOUND_SEMICONDUCTORS.absolute,
    "food processing automation": URLs.INVEST_HPO_FOOD_PROCESSING_AUTOMATION.absolute,
    "fusion energy": URLs.INVEST_HPO_FUSION_ENERGY.absolute,
    "heat networks": URLs.INVEST_HPO_HEAT_NETWORKS.absolute,
    "hydrogen": URLs.INVEST_HPO_HYDROGEN.absolute,
    "immersive technology": URLs.INVEST_HPO_IMMERSIVE_TECHNOLOGY.absolute,
    "marine autonomy": URLs.INVEST_HPO_MARINE_AUTONOMY.absolute,
    "net zero transport": URLs.INVEST_HPO_NET_ZERO_TRANSPORT.absolute,
    "plant based and alternative protein products": URLs.INVEST_HPO_PLANT_BASED_PROTEIN_PRODUCTS.absolute,
    "precision farming": URLs.INVEST_HPO_PRECISION_FARMING.absolute,
    "smart and sustainable avaiation": URLs.INVEST_HPO_SMART_AND_SUSTAINABLE_AVIATION.absolute,
    "spalding battery energy storage system": URLs.INVEST_HPO_SPALDING_BATTERY_ENERGY_STORAGE_SYSTEM.absolute,
    "innovation in animal health": URLs.INVEST_HPO_INNOVATION_IN_ANIMAL_HEALTH.absolute,

}


SELECTORS = {
    "hero": {
        "self": Selector(By.ID, "#content > div.atlas-hero"),
        "heading": Selector(By.CSS_SELECTOR, "#hero h1"),
    },
    "contact us": {
        "self": Selector(By.ID, "contact-section"),
        "heading": Selector(By.CSS_SELECTOR, "#contact-section h2"),
        "get in touch": Selector(By.CSS_SELECTOR, "#contact-section a"),
    },
    "proposition one": {
        "self": Selector(By.ID, "proposition-one"),
        "heading": Selector(By.CSS_SELECTOR, "#proposition-one h2"),
        # "view video transcript": Selector(
        #     By.CSS_SELECTOR, "#proposition-one details summary", type=ElementType.BUTTON
        # ),
        # "video transcript": Selector(By.CSS_SELECTOR, "#proposition-one details p"),
    },
    "opportunity list": {"self": Selector(By.ID, "opportunity-list")},
    "proposition two": {
        "self": Selector(By.ID, "proposition-two"),
        "heading": Selector(By.CSS_SELECTOR, "#proposition-two div:nth-child(1) h2"),
        "list of propositions": Selector(By.CSS_SELECTOR, "#proposition-two ul"),
    },
    "competitive advantages": {
        "self": Selector(By.ID, "competitive-advantages"),
        "first - icon": Selector(
            By.CSS_SELECTOR, "#competitive-advantages li:nth-child(1) img"
        ),
        "first - heading": Selector(
            By.CSS_SELECTOR, "#competitive-advantages li:nth-child(1) div ~ div > h3"
        ),
        "first - list": Selector(
            By.CSS_SELECTOR, "#competitive-advantages li:nth-child(1) div ~ div > ul"
        ),
        "second - icon": Selector(
            By.CSS_SELECTOR, "#competitive-advantages li:nth-child(2) img"
        ),
        "second - heading": Selector(
            By.CSS_SELECTOR, "#competitive-advantages li:nth-child(2) div ~ div > h3"
        ),
        "second - list": Selector(
            By.CSS_SELECTOR, "#competitive-advantages li:nth-child(2) div ~ div > ul"
        ),
        "third - icon": Selector(
            By.CSS_SELECTOR, "#competitive-advantages li:nth-child(3) img"
        ),
        "third - heading": Selector(
            By.CSS_SELECTOR, "#competitive-advantages li:nth-child(3) div ~ div > h3"
        ),
        "third - list": Selector(
            By.CSS_SELECTOR, "#competitive-advantages li:nth-child(3) div ~ div > ul"
        ),
    },
    "testimonial": {
        "self": Selector(By.ID, "testimonial"),
        "quote": Selector(By.CSS_SELECTOR, "#testimonial p"),
    },
    "company list": {
        "self": Selector(By.ID, "company-list"),
        "heading": Selector(By.CSS_SELECTOR, "#company-list p"),
        "list": Selector(By.CSS_SELECTOR, "#company-list ul"),
        "images": Selector(By.CSS_SELECTOR, "#company-list ul img"),
    },
    "case studies": {
        "self": Selector(By.ID, "case-studies"),
        "heading": Selector(By.CSS_SELECTOR, "#case-studies h2"),
        # "first case study": Selector(
        #     By.CSS_SELECTOR,
        #     "#case-studies details:nth-child(1)",
        #     type=ElementType.BUTTON,
        # ),
        "first - heading": Selector(
            By.CSS_SELECTOR, "#case-studies details:nth-child(1) h3"
        ),
        "first - text": Selector(
            By.CSS_SELECTOR, "#case-studies details:nth-child(1) p"
        ),
        # "second case study": Selector(
        #     By.CSS_SELECTOR,
        #     "#case-studies details:nth-child(2)",
        #     type=ElementType.BUTTON,
        # ),
        "second - heading": Selector(
            By.CSS_SELECTOR, "#case-studies details:nth-child(2) h3"
        ),
        "second - text": Selector(
            By.CSS_SELECTOR, "#case-studies details:nth-child(2) p"
        ),
        # "third case study": Selector(
        #     By.CSS_SELECTOR,
        #     "#case-studies details:nth-child(3)",
        #     type=ElementType.BUTTON,
        # ),
        "third - heading": Selector(
            By.CSS_SELECTOR, "#case-studies details:nth-child(3) h3"
        ),
        "third - text": Selector(
            By.CSS_SELECTOR, "#case-studies details:nth-child(3) p"
        ),
    },
    "other opportunities": {
        "self": Selector(By.ID, "other-opportunities"),
        "first opportunity": Selector(
            By.CSS_SELECTOR, "#content > section.atlas-bg.atlas-bg--grey-light > div > div > div:nth-child(1) > a"
        ),
        "second opportunity": Selector(
            By.CSS_SELECTOR, "#content > section.atlas-bg.atlas-bg--grey-light > div > div > div:nth-child(2) > a"
        ),
        "third opportunity": Selector(
            By.CSS_SELECTOR, "#content > section.atlas-bg.atlas-bg--grey-light > div > div > div:nth-child(3) > a"
        ),
        "fourth opportunity": Selector(
            By.CSS_SELECTOR, "#content > section.atlas-bg.atlas-bg--grey-light > div > div > div:nth-child(4) > a > div"
        ),
        "fifth opportunity": Selector(
            By.CSS_SELECTOR, "#content > section.atlas-bg.atlas-bg--grey-light > div > div > div:nth-child(5) > a > div"
        ),

    },
}
SELECTORS.update(common_selectors.INTERNATIONAL_HEADER_WO_LANGUAGE_SELECTOR)
SELECTORS.update(common_selectors.BETA_BAR)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.INTERNATIONAL_FOOTER)


UNEXPECTED_ELEMENTS = {
    "breadcrumbs": {"itself": Selector(By.CSS_SELECTOR, "div.breadcrumbs")}
}


def visit(driver: WebDriver, *, page_name: str = None):
    url = SubURLs[page_name] if page_name else URL
    go_to_url(driver, url, page_name or NAME)


def should_be_here(driver: WebDriver, *, page_name: str):
    url = SubURLs[page_name] if page_name else URL
    check_url(driver, url)
    logging.debug("All expected elements are visible on '%s' page", PAGE_TITLE)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def clean_name(name: str) -> str:
    return name.split(" - ")[1].strip()


def should_see_content_for(driver: WebDriver, hpo_name: str):
    source = driver.page_source
    hpo_name = clean_name(hpo_name)
    logging.debug("Looking for: {}".format(hpo_name))
    with assertion_msg(
        "Expected to find term '%s' in the source of the page %s",
        hpo_name,
        driver.current_url,
    ):
        assert hpo_name.lower() in source.lower()


def should_not_see_section(driver: WebDriver, name: str):
    section = UNEXPECTED_ELEMENTS[name.lower()]
    for key, selector in section.items():
        check_if_element_is_not_visible(
            driver, selector, element_name=key, wait_for_it=False
        )


def unfold_elements_in_section(driver: WebDriver, section_name: str):
    section_selectors = SELECTORS[section_name]
    folded_elements = get_selectors(section_selectors, ElementType.BUTTON)
    logging.debug(f"Found {len(folded_elements)} selectors for elements to unfold")
    for name, selector in folded_elements.items():
        element = find_element(driver, selector, element_name=name)
        scroll_to(driver, element)
        if element.get_attribute("open"):
            logging.debug(f"Element: '{name}' is already unfolded")
        else:
            logging.debug(f"Unfolding closed element: {name}")
            element.click()

def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)
