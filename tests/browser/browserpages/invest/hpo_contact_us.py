# -*- coding: utf-8 -*-
"""Invest in Great - Contact us Page Object."""
import logging
from types import ModuleType
from typing import List, Union
from uuid import uuid4

from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Actor,
    Selector,
    check_for_sections,
    check_radio,
    check_random_radio,
    check_url,
    fill_out_input_fields,
    fill_out_textarea_fields,
    find_element,
    find_selector_by_name,
    go_to_url,
    pick_option,
    submit_form,
    tick_captcha_checkbox,
    tick_checkboxes,
)
from browserpages.common_autocomplete_callbacks import js_country_select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service

NAME = "HPO Contact us"
NAMES = [
    "High productivity food production",
    "Lightweight",
    "Rail",
]
SERVICE = Service.INVEST
TYPE = PageType.CONTACT_US
URL = URLs.INVEST_HPO_CONTACT.absolute
SubURLs = {
    "high productivity food production": URL,
    "lightweight": URL,
    "rail": URL,
}
PAGE_TITLE = ""

SELECTORS = {
    "form": {
        "itself": Selector(By.CSS_SELECTOR, "#content form"),
        "given name": Selector(
            By.CSS_SELECTOR, "#id_given_name", type=ElementType.INPUT
        ),
        "family name": Selector(
            By.CSS_SELECTOR, "#id_family_name", type=ElementType.INPUT
        ),
        "job title": Selector(By.CSS_SELECTOR, "#id_job_title", type=ElementType.INPUT),
        "work email": Selector(
            By.CSS_SELECTOR, "#id_email_address", type=ElementType.INPUT
        ),
        "phone": Selector(By.CSS_SELECTOR, "#id_phone_number", type=ElementType.INPUT),
        "company name": Selector(
            By.CSS_SELECTOR, "#id_company_name", type=ElementType.INPUT
        ),
        "company website": Selector(
            By.CSS_SELECTOR, "#id_website_url", type=ElementType.INPUT
        ),
        "company address": Selector(
            By.CSS_SELECTOR, "#id_company_address", type=ElementType.INPUT
        ),
        "country": Selector(
            By.CSS_SELECTOR,
            "#js-country-select",
            type=ElementType.INPUT,
            is_visible=False,
            autocomplete_callback=js_country_select,
        ),
        # "organisation size": Selector(
        #     By.ID, "id_company_size", type=ElementType.SELECT
        # ),
        # "cam modelling": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-cam-modelling-and-simulation-in-oxfordshire-and-the-midlands-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "carbon fibre in tees valley": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-carbon-fibre-in-tees-valley-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        "chemicals in the humber": Selector(
            By.CSS_SELECTOR,
            "#checkbox-multiple-chemicals-in-the-humber-label",
            type=ElementType.CHECKBOX,
            is_visible=False,
            alternative_visibility_check=True,
        ),
        # "circular economy": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-circular-economy-in-telford-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "compund semiconductors": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-compound-semiconductors-and-applications-in-south-wales-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "controlled environment agriculture": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-controlled-environment-agriculture-in-north-and-west-yorkshire-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "food processing automation": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-food-processing-automation-in-greater-lincolnshire-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "heat networks": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-heat-networks-in-the-north-east-and-tees-valley-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "hydrogen": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-hydrogen-in-north-east-scotland-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "immersive technology": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-immersive-technology-in-the-north-east",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "innovation in animal health": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-innovation-in-animal-health-in-surrey-and-hampshire-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "lightweight": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-lightweight-structures-in-greater-manchester-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "marine autonomy": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-marine-autonomy-in-the-south-west-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "mining": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-mining-in-cornwall-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "offshore wind floating": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-offshore-wind-floating-substructures-in-scotland-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "photonics": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-photonics-in-the-south-west-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "plant based protein products": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-plant-based-and-alternative-protein-products-in-the-north-east-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "precision farming": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-precision-farming-in-telford-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "rail": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-rail-in-doncaster-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        # "aquaculture": Selector(
        #     By.CSS_SELECTOR,
        #     "#checkbox-multiple-sustainable-aquaculture-in-dorset-label",
        #     type=ElementType.CHECKBOX,
        #     is_visible=False,
        #     alternative_visibility_check=True,
        # ),
        "terms and conditions": Selector(
            By.ID,
            "id_terms_agreed",
            type=ElementType.CHECKBOX,
            is_visible=False,
            alternative_visibility_check=True,
        ),
        "how can we help": Selector(
            By.CSS_SELECTOR,
            "#id_how_can_we_help_1",
            type=ElementType.RADIO,
            is_visible=False,
            # alternative_visibility_check=True,
        ),
        "information email": Selector(
            By.CSS_SELECTOR,
            "#id_email_contact_consent-label",
            type=ElementType.CHECKBOX,
            is_visible=False,
            alternative_visibility_check=True,
        ),
        "industry": Selector(By.CSS_SELECTOR, "#id_industry", type=ElementType.SELECT),
        "tell us about your plans": Selector(
            By.CSS_SELECTOR, "#id_your_plans", type=ElementType.TEXTAREA
        ),
        # "comment": Selector(By.ID, "id_comment", type=ElementType.TEXTAREA),
        # "terms and conditions link": Selector(
        #     By.CSS_SELECTOR, "#id_terms_agreed-label a"
        # ),
        "how did you hear about us": Selector(
            By.CSS_SELECTOR, "#id_how_did_you_hear", type=ElementType.SELECT
        ),
        "i would like to receive additional information by email": Selector(
            By.CSS_SELECTOR,
            "#id_email_contact_consent-label",
            type=ElementType.CHECKBOX,
            is_visible=False,
            alternative_visibility_check=True,
        ),
        "captcha": Selector(
            By.CSS_SELECTOR, "#form-container iframe", type=ElementType.IFRAME
        ),
        "submit": Selector(
            By.CSS_SELECTOR, "#form-container > form > button", type=ElementType.SUBMIT
        ),
    },
}
SELECTORS.update(common_selectors.INVEST_HEADER)
SELECTORS.update(common_selectors.BETA_BAR)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.INVEST_FOOTER)


def visit(driver: WebDriver, *, page_name: str = None):
    url = SubURLs[page_name] if page_name else URL
    go_to_url(driver, url, page_name or NAME)


def should_be_here(driver: WebDriver, *, page_name: str):
    check_url(driver, URL, exact_match=False)
    logging.debug("All expected elements are visible on '%s' page", NAME)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def check_state_of_form_element(
    driver: WebDriver, element_name: str, expected_state: str
):
    element_selector = find_selector_by_name(SELECTORS, element_name)
    element = find_element(driver, element_selector, wait_for_it=False)
    if expected_state == "selected":
        assert element.get_property("checked")


def generate_form_details(actor: Actor, *, custom_details: dict = None) -> dict:
    details = {
        "given name": str(uuid4()),
        "family name": str(uuid4()),
        "job title": "QA @ DIT",
        "work email": actor.email,
        "phone": "0123456789",
        "company name": actor.company_name or "Automated test - company name",
        "company website": "https://browser.tests.com",
        "company address": "Test whitehall place",
        "country": True,
        # "organisation size": None,
        "comment": "This form was submitted by Automated test",
        # "aquaculture": True,
        # "advanced food production": True,
        # "lightweight": True,
        # "rail": True,
        # "photonics": True,
        # "space": True,
        "chemicals in the humber": True,
        # "sustainable packaging": True,
        "industry": None,
        "how can we help": True,
        "tell us about your plans": "Automated tests",
        "how did you hear about us": None,
        "i would like to receive additional information by email": True,
        # "terms and conditions": True,
    }
    if custom_details:
        details.update(custom_details)
    logging.debug(f"Form details: {details}")
    return details


def fill_out(driver: WebDriver, details: dict):
    form_selectors = SELECTORS["form"]
    fill_out_input_fields(driver, form_selectors, details)
    fill_out_textarea_fields(driver, form_selectors, details)
    pick_option(driver, form_selectors, details)
    tick_checkboxes(driver, form_selectors, details)
    check_radio(driver, form_selectors, details)
    # tick_captcha_checkbox(driver)


def submit(driver: WebDriver) -> Union[ModuleType, None]:
    return submit_form(driver, SELECTORS["form"])
