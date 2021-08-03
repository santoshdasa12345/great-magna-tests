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

NAME = "Marketing Approach"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_MARKETING_APPROACH.absolute
PAGE_TITLE = "Marketing Approach Page"

SELECTORS = {
    "marketing approach": {
        "open": Selector(
            By.XPATH, "//span[contains(text(),'open')]"
        ),
        "close": Selector(
            By.XPATH, "//span[contains(text(),'close')]"
        ),
        "check box": Selector(
            By.CSS_SELECTOR, "#target-age-groups > form > ul > li:nth-child(1) > label"
        ),
        "0-14 year olds": Selector(
            By.CSS_SELECTOR, "#target-age-groups > form > ul > li:nth-child(1) > label"
        ),
        "15-19": Selector(
            By.XPATH, "//label[contains(text(),'15-19 year olds')]"
        ),
        "20-24": Selector(
            By.CSS_SELECTOR, "//input[@id='20-24']"
        ),
        "25-34": Selector(
            By.XPATH, "//label[contains(text(),'25-34 year olds')]"
        ),
        "35-44": Selector(
            By.XPATH, "//label[contains(text(),'35-44 year olds')]"
        ),
        "45-54": Selector(
            By.CSS_SELECTOR, "//label[contains(text(),'45-54 year olds')]"
        ),
        "55-64": Selector(
            By.XPATH, "//label[contains(text(),'55-64 year olds')]"
        ),
        "65": Selector(
            By.CSS_SELECTOR, "//label[contains(text(),'65 years old and over')]"
        ),
        "confirm": Selector(
            By.XPATH, "//button[contains(text(),'Confirm')]"
        ),
        "educational moment": Selector(
            By.CSS_SELECTOR,
            "#target-age-groups > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > button > i"
        ),
        "add route to market": Selector(
            By.CSS_SELECTOR, "#route-to-market > button"
        ),
        "how will we promote to product drop down": Selector(
            By.CSS_SELECTOR, "#route-to-market > div > div:nth-child(2) > div > button"
        ),
        "example": Selector(
            By.CSS_SELECTOR, "#route-to-market > div:nth-child(1) > div.form-group > div > button"
        ),
        "route to market text": Selector(
            By.CSS_SELECTOR, "#target-age-groups > button > span"
        ),
        "delete icon": Selector(
            By.CSS_SELECTOR, "#route-to-market > div:nth-child(1) > div.text-center > button > i"
        ),
        "marketing resources example": Selector(
            By.CSS_SELECTOR, "#resources > div > div.learning > div.learning__buttons.m-b-xs > button.button-example.button.button--small.button--tertiary.m-r-xxs"
        ),
        "marketing resources text": Selector(
            By.XPATH, "//textarea[@id='resources']"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "section complete": Selector(
            By.XPATH, "//label[contains(text(),'Yes')]"
        ),
        "costs and pricing": Selector(
            By.XPATH, "//span[contains(text(),'Costs and pricing')]"
        ),
        "export plan home": Selector(
            By.CSS_SELECTOR,
            "#marketing-approach-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > div > a"
        ),
        "selling direct to your customer": Selector(
            By.XPATH, "//h4[contains(text(),'Selling direct to your customer')]"
        ),
        "what marketing resources example": Selector(
            By.CSS_SELECTOR, "#resources > div > div.learning > div.learning__buttons.m-b-xs > button.button-example.button.button--small.button--tertiary.m-r-xxs"
        ),
        "lesson": Selector(
            By.CSS_SELECTOR,
            "#resources > div > div.m-b-xs > button.button-lesson.button.button--small.button--tertiary.m-r-xxs"
        ),
        "nav funding and credit": Selector(
            By.CSS_SELECTOR, "#collapseNav > div > ul > li:nth-child(7) > a"
        ),
        "back": Selector(
            By.XPATH, "//body/div[10]/div/div/div/div[1]/a"
        ),
        "add a product": Selector(
            By.XPATH, "//button[contains(text(),'Add a product')]"
        ),
        "add a target market": Selector(
            By.XPATH, "//button[contains(text(),'Add a target market')]"
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

def find_and_select_random_item_list(driver: WebDriver, element_selector_name: str):
    find_and_click(driver, element_selector_name="Add route to market")
    drop_down_btn = driver.find_element_by_xpath("//body/main/div[2]/section[4]/div/div[2]/div/div/div[1]/div/div/div[3]/div[1]")
    drop_down_btn.click()
    driver.implicitly_wait(5)
    #select__list body-l bg-white radius
    drop_down_element = driver.find_element_by_xpath("//body/main/div[2]/section[4]/div/div[2]/div/div/div[1]/div/div/div[3]/ul")
    li_elements = drop_down_element.find_elements_by_tag_name("li")
    logging.debug("list elements")
    logging.debug(li_elements)
    random_number = 0
    if len(li_elements) > 2:
        random_number = random.randint(1, len(li_elements)-1)
    random_li_element = li_elements[random_number]
    logging.debug(random_number)
    logging.debug(random_li_element.tag_name)
    logging.debug(random_li_element)
    time.sleep(2)

def random_select_checkbox(driver: WebDriver, element_name: str):
    find_and_click(driver, element_selector_name="Select")

    random_age_group_element_xpath = "//body/main/div[2]/section[3]/div/div/div[2]/div/div[1]/form/ul/li" \
                                     + "["+ str(random.randint(0, 8)) + "]"+ "/label"
    driver.implicitly_wait(1)
    driver.find_element_by_xpath(random_age_group_element_xpath).click()
    find_and_click(driver, element_selector_name="Confirm")
