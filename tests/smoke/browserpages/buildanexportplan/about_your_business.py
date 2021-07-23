import logging
import random
import time
from types import ModuleType
from typing import List, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

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

NAME = "About Your business"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_ABOUT_YOUR_BUSINESS.absolute
PAGE_TITLE = "About Your business Page"

SELECTORS = {
    "about your business": {
        "about your business": Selector(
            By.XPATH, "//*[@id=\"export-plan-dashboard\"]/div[1]/div/a/div[2]/h3"
        ),
        "how you started example": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div:nth-child(1) > div > div.learning__buttons.m-b-xs > button"
        ),
        "how you started educational": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div:nth-child(1) > div > div.learning__buttons.m-b-xs > div > div > button > i"
        ),
        "how you started": Selector(
            By.XPATH, "//*[@id=\"story\"]", type=ElementType.INPUT
        ),
        "where you're based example": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div:nth-child(2) > div > div.learning__buttons.m-b-xs > button"
        ),
        "where you're based": Selector(
            By.XPATH, "//*[@id=\"location\"]", type=ElementType.INPUT
        ),
        "how you make your products example": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div:nth-child(3) > div > div.learning__buttons.m-b-xs > button"
        ),
        "how you make your products": Selector(
            By.XPATH, "//*[@id=\"processes\"]", type=ElementType.INPUT
        ),
        "your product packaging example": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div:nth-child(4) > div > div.learning__buttons.m-b-xs > button"
        ),
        "your product packaging": Selector(
            By.XPATH, "//*[@id=\"packaging\"]", type=ElementType.INPUT
        ),
        "business performance drop down": Selector(
            By.XPATH, "//*[@id=\"about-your-business-form\"]/div[5]/button"
        ),
        "business objectives": Selector(
            By.CSS_SELECTOR, "#about-your-business-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > a > span"
        ),
        "export plan home": Selector(
            By.CSS_SELECTOR, "#about-your-business-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > div.m-t-l > a"
        ),
        "move from accidental exporting to strategic exporting": Selector(
            By.XPATH, "//*[@id=\"about-your-business-content\"]/section[3]/div/div[1]/div/a/div/p"
        ),
        "your business performance label": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div.select.m-b-l > div > label"
        ),
        "your business performance dropdown": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div.select.m-b-l > button"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav business objectives": Selector(
            By.CSS_SELECTOR, "#collapseNav > div > ul > li:nth-child(2) > a"
        ),
        "yes checkbox": Selector(
            By.CSS_SELECTOR, "#section-complete > div > label"
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
    # about-your-business-form > div.select.m-b-l > button
    drop_down_btn = driver.find_element_by_css_selector(
        "#about-your-business-form > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius")
    drop_down_btn.click()
    driver.implicitly_wait(5)
    # select__list body-l bg-white radius
    # about-your-business-form > div.select.m-b-l > ul
    drop_down_element = driver.find_element_by_xpath("//body/main/div[2]/section[3]/div/div[2]/form/div[5]/div/div[4]/ul")
    li_elements = drop_down_element.find_elements_by_tag_name("li")
    logging.debug("list elements")
    logging.debug(li_elements)
    random_number = 0
    if len(li_elements) > 2:
        random_number = random.randint(1, len(li_elements) - 1)
    random_li_element = li_elements[random_number]
    logging.debug(random_number)
    logging.debug(random_li_element.tag_name)
    logging.debug(random_li_element)
    time.sleep(2)
    # random_li_element.click()

    # select = Select(random_li_element)
    # select.select_by_index(0)

    # £500,000 up to £1,999,999


def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()
