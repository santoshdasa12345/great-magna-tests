import logging
import random
import time
from types import ModuleType
from typing import List, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from browserpages import ElementType, common_selectors
from great_magna_tests_shared.utils import check_url_path_matches_template
from browserpages.common_actions import (
    Actor,
    Selector,
    assertion_msg,
    check_for_sections,
    check_if_element_is_not_present,
    check_if_element_is_visible,
    check_url,
    find_element,
    find_selector_by_name,
    find_elements,
    go_to_url,
    pick_option,
    is_element_present,
    submit_form,
    check_random_radio,
    take_screenshot,
    wait_for_page_load_after_action,
    fill_out_input_fields,
    fill_out_email_address

)

NAME = "Funding finance and getting paid"
SERVICE = Service.LEARNTOEXPORT
TYPE = PageType.LESSON
URL = URLs.GREAT_MAGNA_LESSONS_FUNDING_FINANCE_AND_GETTING_PAID.absolute
PAGE_TITLE = "Funding finance and getting paid page"

SELECTORS = {
    "Funding finance and getting paid": {
        "choose the right funding": Selector(
            By.XPATH, "//span[contains(text(),'Choose the right funding and credit options')]"
        ),
        "avoid cashflow challenges when exporting": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[1]/div/ul/li[2]/a"
        ),
        "insure against non payment": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[2]/div/ul/li[1]/a"
        ),
        "create an export invoice": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[2]/div/ul/li[2]/a"
        ),
        "decide when to get paid": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[2]/div/ul/li[3]/a"
        ),
        "choose the right payment method": Selector(
            By.XPATH, "//span[contains(text(),'Choose the right payment method')]"
        ),
        "adapting ecommerce payment methods for lcoal markets": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[2]/div/ul/li[5]/a"
        ),
        "manage exchange rates": Selector(
            By.XPATH, "//span[contains(text(),'Manage exchange rates')]"
        ),
        "top back": Selector(
            By.CSS_SELECTOR, "#learn-root > span > a"
        )
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)
