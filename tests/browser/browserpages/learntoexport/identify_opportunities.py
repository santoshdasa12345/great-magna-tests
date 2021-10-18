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

NAME = "Identify Opportunities"
SERVICE = Service.LEARNTOEXPORT
TYPE = PageType.LESSON
URL = URLs.GREAT_MAGNA_LESSONS_IDENTIFY_OPPORTUNITIES_AND_RESEARCH_THE_MARKET.absolute
PAGE_TITLE = "Identify Opportunities Page "

SELECTORS = {
    "identify opportunities": {
        "identify opportunities": Selector(
            By.XPATH, "//body/main[@id='content']/section[@id='learn-root']/section[1]/a[2]/article[1]"
        ),
        "choosing the right export opportunities": Selector(
            By.XPATH, "//span[contains(text(),'Choosing the right export opportunities')]"
        ),
        "move from accidental exporting to strategic exporting": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[1]/div/ul/li[2]/a"
        ),
        "in market research": Selector(
            By.XPATH, "//span[contains(text(),'In-market research')]"
        ),
        "online research": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[2]/div/ul/li[2]/a"
        ),
        "Work out customer demand": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[3]/div/ul/li[1]/a"
        ),
        "understand your market size and its segments": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[3]/div/ul/li[2]/a"
        ),
        "understanding the competition": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[4]/div/ul/li/a"
        ),
        "module_progress": Selector(
            By.CSS_SELECTOR, "#learn-root > section.learn__single-category-header > div > div > div:nth-child(1) > div.learn__single-category-header-content > div.learn__category-progress-container"
        ),
        "lessons_progress_bar": Selector(
            By.XPATH, "//*[@id=\"55\"]/div/p"
        ),
        "lesson_categories_progress": Selector(
            By.CSS_SELECTOR, "#learn-root > section > a:nth-child(3) > article > div > div.learn__category-content.learn__category-content--progress-bar > div.learn__category-progress-container > div"
        ),
        "bottom back": Selector(
            By.CSS_SELECTOR, "#content > div > div.bg-blue-deep-80 > a > i"
        ),
        "top back": Selector(
            By.CSS_SELECTOR, "#learn-root > span > a"
        ),
        "research current market conditions": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[5]/div/ul/li[1]/a"
        ),
        "ease of entry into a new market": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[5]/div/ul/li[2]/a"
        ),
        "research local infrastructure": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[5]/div/ul/li[3]/a"
        ),
        "adapting your product or service": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[5]/div/ul/li[4]/a"
        ),
        "information you need to choose a target country": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[5]/div/ul/li[5]/a"
        ),
        "customer demand vs ease of entry": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[5]/div/ul/li[6]/a"
        ),
        "research free trade agreements": Selector(
            By.XPATH, "//body/main/div/section[2]/ol/li[5]/div/ul/li[7]/a"
        ),
        "placeholder lesson": Selector(
            By.XPATH, "//*[@id=\"64\"]/ul/li[2]/a"
        ),
        "back" : Selector(
            By.XPATH, "//body/div[7]/div/div/div/div[1]/a"
        ),
        "ok button": Selector(
            By.XPATH, "//button[contains(text(),'Ok')]"
        ),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)

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

def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()
