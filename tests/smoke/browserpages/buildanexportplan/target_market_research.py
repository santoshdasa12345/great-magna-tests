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

NAME = "Target Markets Research"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_TARGET_MARKET_RESEARCH.absolute
PAGE_TITLE = "Target Markets Research Page"

SELECTORS = {
    "target markets research": {
        "target markets research": Selector(
            By.XPATH, "//*[@id=\"export-plan-dashboard\"]/div[3]/div/a/div[2]/h3"
        ),
        "data snapshot": Selector(
            By.XPATH, "//*[@id=\"target-age-groups\"]/div/button"
        ),
        "select": Selector(
            By.XPATH, "//*[@id=\"target-age-groups\"]/div[1]/div[3]/div/button"
        ),
        "close": Selector(
            By.XPATH, "//span[contains(text(),'close')]"
        ),
        "confirm": Selector(
            By.XPATH, "//button[contains(text(),'Confirm')]"
        ),
        "describe the consumer demand example": Selector(
            By.CSS_SELECTOR, "#target-markets-research > div:nth-child(1) > div.learning > div.learning__buttons.m-b-xs > button.button-example.button.button--small.button--tertiary.m-r-xxs"
        ),
        "describe the consumer demand": Selector(
            By.CSS_SELECTOR, "#demand"
        ),
        "Who are your competitors example": Selector(
            By.CSS_SELECTOR, "#target-markets-research > div:nth-child(2) > div.learning > div.learning__buttons.m-b-xs > button"
        ),
        "Who are your competitors": Selector(
            By.CSS_SELECTOR, "#competitors"
        ),
        "What are the product trends example": Selector(
            By.CSS_SELECTOR, "#target-markets-research > div:nth-child(3) > div.learning > div.learning__buttons.m-b-xs > button"
        ),
        "What are the product trends": Selector(
            By.CSS_SELECTOR, "#trend"
        ),
        "marketing resources example": Selector(
            By.CSS_SELECTOR, "#resources > div > div.m-b-xs > button"
        ),
        "What’s your unique selling proposition example": Selector(
            By.CSS_SELECTOR, "#target-markets-research > div:nth-child(4) > div.learning > div.learning__buttons.m-b-xs > button"
        ),
        "What’s your unique selling proposition": Selector(
            By.CSS_SELECTOR, "#unqiue_selling_proposition"
        ),
        "Adapting Your Product": Selector(
            By.XPATH, "//span[contains(text(),'Adapting Your Product')]"
        ),
        "export plan home": Selector(
            By.CSS_SELECTOR,
            "#target-markets-research-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > div.m-t-l > a"
        ),
        "what’s the average price for your product": Selector(
            By.CSS_SELECTOR, "#average_price", type=ElementType.INPUT
        ),
        "using what you know": Selector(
            By.XPATH, "//h4[contains(text(),'Using what you know to help inform your positionin')]"
        ),
        "work out customer demand": Selector(
            By.CSS_SELECTOR, "#target-markets-research > div:nth-child(1) > div.learning > div.learning__content > a > div > h4"
        ),
        "understand market trends": Selector(
            By.XPATH, "//h4[contains(text(),'Understand market trends')]"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav Adapting Your Product": Selector(
            By.XPATH, "//a[contains(text(),'Adapting Your Product')]"
        ),
        "yes checkbox": Selector(
            By.XPATH, "//body/main/div/div[2]/div[2]/div/div/div[2]/fieldset/div/div"
        ),
        "lesson": Selector(
            By.CSS_SELECTOR,
            "#target-markets-research > div:nth-child(1) > div.m-b-xs > button.button-lesson.button.button--small.button--tertiary.m-r-xxs"
        ),
        "add a product": Selector(
            By.XPATH, "//button[contains(text(),'Add a product')]", type=ElementType.INPUT
        ),
        "back": Selector(
            By.XPATH, "//body/div[8]/div/div/div/div[1]/a"
        ),
        "add a target market": Selector(
            By.XPATH, "//button[contains(text(),'Add a target market')]"
        ),
        "search": Selector(
            By.CSS_SELECTOR, "#search-input", type=ElementType.INPUT
        ),
        "top export plan home": Selector(
            By.XPATH, "//*[@id=\"business-risk-content\"]/section[1]/div/div/div[2]/a/span"
        ),

    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def fill_out_products(driver: WebDriver, products: str):
    fill_out_input_fields(driver, products)


def enter_text(driver: WebDriver, element_name: str):
    text_element = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    text_element.clear()
    text_element.send_keys("Automated tests")


def validate_entered_text(driver: WebDriver, element_name: str):
    text_element = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    if "Automated tests" in text_element.text:
        return True
    return False


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()


def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def random_select_checkbox(driver: WebDriver, element_name: str):
    find_and_click(driver, element_selector_name="Select")

    random_age_group_element_xpath = "//body/main/div[2]/section[3]/div/div/div[2]/div/div[1]/form/ul/li" \
                                     + "["+ str(random.randint(0, 8)) + "]"+ "/label"
    driver.implicitly_wait(1)
    driver.find_element_by_xpath(random_age_group_element_xpath).click()
    find_and_click(driver, element_selector_name="Confirm")

def enter_value(driver: WebDriver, element_name: str):
    value_element = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    value_element.clear()
    value_element.send_keys("20")
