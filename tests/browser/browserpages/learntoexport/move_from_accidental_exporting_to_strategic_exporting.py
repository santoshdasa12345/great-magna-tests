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

NAME = "Move from accidental exporting to strategic exporting"
SERVICE = Service.LEARNTOEXPORT
TYPE = PageType.LESSON
URL = URLs.GREAT_MAGNA_LESSONS_MOVE_FROM_ACCIDENTAL_EXPORTING_TO_STRATEGIC_EXPORTING.absolute
PAGE_TITLE = "Move from accidental exporting to strategic exporting"

SELECTORS = {
    "move from accidental exporting to strategic exporting": {
        "continue learning": Selector(
            By.XPATH, "//a[contains(text(),'Continue learning')]"
        ),
        "bottom back": Selector(
            By.XPATH, "//body/main/div/div[2]/div[3]/a"
        ),
        "top back": Selector(
            By.XPATH, "//body/main/div/div[1]/div/div[1]/a"
        ),
        "lesson yes checkbox": Selector(
            By.CSS_SELECTOR, "#mark_as_complete > div > div"
        ),
        "open case study": Selector(
            By.CSS_SELECTOR, "#case_study > div > button"
        ),
        "close case study": Selector(
            By.XPATH, "//body/main/div/div[1]/div/div[2]/div[2]/div[3]/div[5]/div/div/div/div/button"
        ),
        "view all lessons": Selector(
            By.XPATH, "//a[contains(text(),'View all lessons')]"
        ),
        "view transcript": Selector(
            By.XPATH, "//span[contains(text(),'View transcript')]"
        ),
        "about your business": Selector(
            By.XPATH, "//span[contains(text(),'About your business')]"
        ),
        "business objectives": Selector(
            By.XPATH, "//span[contains(text(),'Business objectives')]"
        ),
    },
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def check_lesson_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()

def find_progress_bar(driver: WebDriver, element_name : str):
    # search for parent progress bar div class
    parent_div_element = driver.find_element_by_class_name("learn__category-progress-container")
    #child_radio_div_elements = parent_div_radio_element.find_elements_by_tag_name("div")
    p_tag = parent_div_element.find_element_by_tag_name("p")
    logging.debug(p_tag.text)
    # get the child elements if any
    # check if progress bar exists
    # read the text from the progress bar

    #
    # find_and_click = find_element(
    #     driver, find_selector_by_name(SELECTORS, element_name)
    # )
    # find_and_click.click()
