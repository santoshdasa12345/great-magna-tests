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

NAME = "Setting up a business abroad"
SERVICE = Service.LEARNTOEXPORT
TYPE = PageType.LESSON
URL = URLs.GREAT_MAGNA_LESSONS_SETTING_UP_A_BUSINESS_ABROAD.absolute
PAGE_TITLE = "Setting up a business abroad"
PROMO_VIDEO = Selector(By.CSS_SELECTOR,
                       "#content > div > div:nth-child(2) > div > div > div > div.c-1-2 > div.lesson-hero.media-section > video")
CLOSE_VIDEO = Selector(By.ID, "campaign-section-videoplayer-close")
SELECTORS = {
    "setting up a business abroad": {
        "lesson yes checkbox": Selector(
            By.XPATH, "//label[contains(text(),'Yes')]"
        ),
        "continue learning": Selector(
            By.XPATH, "//a[contains(text(),'Continue learning')]"
        ),
        "bottom back": Selector(
            By.XPATH, "//body/main/div/div[2]/span/a"
        ),
        "top back": Selector(
            By.XPATH, "//body/main/div/div[1]/div/div[1]/a"
        ),
        "open case study" :Selector(
            By.XPATH, "//body/main/div/div[1]/div/div[2]/div[2]/div[3]/div[5]/div/div/div/div/button"
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

def open(driver: WebDriver, group: str, element: str):
    selector = SELECTORS[group.lower()][element.lower()]
    link = find_element(driver, selector, element_name=element, wait_for_it=True)
    check_if_element_is_visible(link, element_name=element)
    link.click()
    take_screenshot(driver, NAME + " after clicking on: %s link".format(element))


def play_video(driver: WebDriver, *, play_time: int = 5):
    # open(driver, group="what's new", element="watch video")
    video_load_delay = 2
    play_js = f'document.querySelector("{PROMO_VIDEO.value}").play()'
    pause = f'document.querySelector("{PROMO_VIDEO.value}").pause()'
    driver.execute_script(play_js)
    if play_time:
        time.sleep(play_time + video_load_delay)
        driver.execute_script(pause)


def get_video_watch_time(driver: WebDriver) -> int:
    watch_time_js = f'return document.querySelector("{PROMO_VIDEO.value}").currentTime'
    duration_js = f'return document.querySelector("{PROMO_VIDEO.value}").duration'
    watch_time = driver.execute_script(watch_time_js)
    duration = driver.execute_script(duration_js)
    logging.debug(f"Video watch time: {watch_time}")
    logging.debug(f"Video duration : {duration}")
    return int(watch_time)


def close_video(driver: WebDriver):
    take_screenshot(driver, NAME + " before closing video modal window")
    close_button = find_element(driver, CLOSE_VIDEO)
    close_button.click()
