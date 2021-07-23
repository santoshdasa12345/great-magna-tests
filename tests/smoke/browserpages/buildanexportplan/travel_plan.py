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

NAME = "Travel Plan"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_TRAVEL_PLAN.absolute
PAGE_TITLE = "Travel Plan Page"

SELECTORS = {
    "travel plan": {
        "back": Selector(
            By.XPATH, "//body/div[7]/div/div/div/div[1]/a"
        ),
        "travel information": Selector(
            By.XPATH, "//textarea[@id='travel_information']", type=ElementType.INPUT
        ),
        "travel information eduactional": Selector(
            By.CSS_SELECTOR, "#culture-and-rules > div.tooltip.inline-block > div > button > i"
        ),
        "cultural information": Selector(
            By.XPATH, "//textarea[@id='cultural_information']", type=ElementType.INPUT
        ),
        "languages educational": Selector(
            By.XPATH, "//*[@id=\"stats-for-target-market\"]/div[1]/div/div/div/div/div/button/i"
        ),
        "open datasnapshot": Selector(
            By.XPATH, "//*[@id=\"stats-for-target-market\"]/div/button"
        ),
        "i dont need visa": Selector(
            By.XPATH, "//body/main/div[2]/section[5]/div/div[2]/div[2]/div/div[1]/label"
        ),
        "i need a visa": Selector(
            By.XPATH, "//body/main/div[2]/section[5]/div/div[2]/div[2]/div/div[2]/label"
        ),
        "planned travel educational": Selector(
            By.CSS_SELECTOR, "#planned-travel > div > div.learning__buttons.m-b-xs > div > div > button > i",
            type=ElementType.INPUT
        ),
        "add a trip": Selector(
            By.CSS_SELECTOR, "#planned-travel > button"
        ),
        "delete message": Selector(
            By.XPATH, "//body/div[12]/div/div/div/div[2]/div[2]/button[1]/i"
        ),
        "how and where": Selector(
            By.CSS_SELECTOR, "#how_where_visa"
        ),
        "how long": Selector(
            By.CSS_SELECTOR, "#how_long"
        ),
        "notes": Selector(
            By.CSS_SELECTOR, "#notes"
        ),
        "yes checkbox": Selector(
            By.XPATH, "//input[@id='checkbox_complete']"
        ),
        "Selling direct to your customer link": Selector(
            By.CSS_SELECTOR,
            "#marketing-approach-content > section.container.m-b-l > div > div.c-1-4.m-t-s > div > a > div > p"
        ),
        "how to manage exchange rates": Selector(
            By.XPATH, "//h4[contains(text(),'How to manage exchange rates')]"
        ),
        "lesson": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.bg-blue-deep-10.m-t-l.p-v-s > div > div > div.c-1-1.c-2-3-m.c-1-2-xl > button"
        ),
        "open navigation": Selector(
            By.XPATH, "//*[@id=\"collapseNav\"]/div/button/i"
        ),
        "nav business risk": Selector(
            By.CSS_SELECTOR, "#collapseNav > div > ul > li:nth-child(10) > button"
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


def enter_trip_details(driver: WebDriver, position: str, trip_name: str):
    # every call of this function, click on Add Goal
    find_and_click(driver, element_selector_name="Add a trip")
    time.sleep(2)
    document_div_element_xpath = "/html/body/main/div[2]/section[6]/div/div[2]/div/div[2]/table/tbody/tr" + "[" + position + "]"
    document_text_ele_xpath = document_div_element_xpath + "/td/div/textarea"
    driver.find_element_by_xpath(document_text_ele_xpath).send_keys(trip_name)
    time.sleep(2)


def delete_all_trip_details(driver: WebDriver, del_button_position: str):
    # 1,3,5,7,......
    trip_text_area_element_index = int(del_button_position) - 1
    trip_text_area_element_x_path = "/html/body/main/div[2]/section[6]/div/div[2]/div/div[2]/table/tbody/tr" \
                                    + "[" + str(trip_text_area_element_index) + "]" + "/td/div/textarea"
    trip_text_area_text_exists = True
    try:
        trip_text_area_text = driver.find_element_by_xpath(trip_text_area_element_x_path).text
        if trip_text_area_text == None or len(trip_text_area_text) <= 0:
            trip_text_area_text_exists = False
    except:
        trip_text_area_text_exists = False

    # del_button_position: 2,4,6,8,10,.....
    document_div_element_xpath = "/html/body/main/div[2]/section[6]/div/div[2]/div/div[2]/table/tbody/tr" + "[" + del_button_position + "]"
    del_btn_ele_xpath = document_div_element_xpath + "/td/button/i"
    driver.find_element_by_xpath(del_btn_ele_xpath).click()

    if trip_text_area_text_exists == True:
        driver.implicitly_wait(1)
        # 12,13,14,15.......
        # 12 + (2/2 - 1), 12 + (4/2 - 1), 12 + (6/2 - 1), 12 + (8/2 - 1),.........
        delete_msg_yes_index = int(12 + (int((int(del_button_position) / 2)) - 1))
        delete_message_yes_element_xpath = "//body/div" + "[" + str(
            delete_msg_yes_index) + "]" + "/div/div/div/div[2]/div[2]/button[1]"
        delete_message_yes_element = driver.find_element_by_xpath(delete_message_yes_element_xpath)
        delete_message_yes_element.click()
        time.sleep(1)


def select_radio_button(driver: WebDriver, element_name: str):
    # i dont need visa
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//body/main/div[2]/section[5]/div/div[2]/div[2]/div/h2")
    lower_case_element_name = element_name.lower()
    # find_and_click(driver, element_selector_name=element_name)
    # logging.debug(SELECTORS["travel plan"][lower_case_element_name])
    # logging.debug(SELECTORS["travel plan"][lower_case_element_name].value)
    radio_element_x_path = SELECTORS["travel plan"][lower_case_element_name].value
    radio_i_dont_need_visa_elem = driver.find_element_by_xpath(radio_element_x_path)
    radio_i_dont_need_visa_elem.click()


def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()
