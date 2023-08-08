import logging
import random
import time
from types import ModuleType
from typing import List, Union

from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Actor,
    Selector,
    assertion_msg,
    check_for_sections,
    check_if_element_is_not_present,
    check_if_element_is_visible,
    check_random_radio,
    check_url,
    fill_out_email_address,
    fill_out_input_fields,
    find_element,
    find_elements,
    find_selector_by_name,
    go_to_url,
    is_element_present,
    pick_option,
    submit_form,
    take_screenshot,
    wait_for_page_load_after_action,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from great_magna_tests_shared.utils import check_url_path_matches_template

NAME = "Regulations licensing and logistics"
SERVICE = Service.LEARNTOEXPORT
TYPE = PageType.LESSON
URL = URLs.GREAT_MAGNA_LESSONS_REGULATIONS_LICENSING_AND_LOGISTICS.absolute
PAGE_TITLE = "Regulations licensing and logistics page"

SELECTORS = {
    "Regulations licensing and logistics": {
        "how to adapt your labelling and packaging": Selector(
            By.XPATH,
            "//span[contains(text(),'How to adapt your labelling and packaging')]",
        ),
        "understand duties and taxes": Selector(
            By.XPATH, "//span[contains(text(),'Understand duties and taxes')]"
        ),
        "understand local market regulations for products": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[1]/div/ul/li[3]/a"
        ),
        "using harmonised system or commodity codes": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[1]/div/ul/li[4]/a"
        ),
        "applying rules sof orgin to your product": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[1]/div/ul/li[5]/a"
        ),
        "choose which incoterms are right for you": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[2]/div/ul/li[1]/a"
        ),
        "using freight forwarders": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[2]/div/ul/li[2]/a"
        ),
        "regulations around ecommerce": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[3]/div/ul/li[1]/a"
        ),
        "regulations around supplying a service": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[3]/div/ul/li[2]/a"
        ),
        "understand data regulations and data protection": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[3]/div/ul/li[3]/a"
        ),
        "how to make uk customs declaration": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[4]/div/ul/li[1]/a"
        ),
        "understand export licensing": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[4]/div/ul/li[2]/a"
        ),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)
