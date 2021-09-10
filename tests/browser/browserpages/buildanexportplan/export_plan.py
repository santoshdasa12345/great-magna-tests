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

NAME = "Export Plan"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_START_PRODUCT_MAKE_AN_EXPORT_PLAN.absolute
PAGE_TITLE = "Export Plan"
# NAMES = [NAME, "new-lesson-added"]
SubURLs = {
    # "export plan":URLs.GREAT_MAGNA_EXPORT_PLAN_DASHBOARD.absolute,
    "export plan": URLs.GREAT_MAGNA_START_PRODUCT_MAKE_AN_EXPORT_PLAN.absolute,
    "export plan market": URLs.GREAT_MAGNA_START_MARKET_MAKE_AN_EXPORT_PLAN.absolute_template,
    "export plan dashboard" : URLs.GREAT_MAGNA_NEW_EXPORT_PLAN.absolute_template,
}

SELECTORS = {
    "Export Plan Dashboard": {
        "top create a new plan": Selector(
            By.CSS_SELECTOR, "#content > div.bg-blue-deep-80.hero-image-container > div > div > div.c-1-2.p-v-xl.lh > a"
        ),
        "bottom create an export plan": Selector(
            By.CSS_SELECTOR, "#content > div:nth-child(3) > div > div > div > div:nth-child(2) > div:nth-child(1) > a"
        ),
        "continue": Selector(
            By.XPATH, "//body/main/div/div[1]/div[2]/div[2]/a"
        ),
        "choose a product": Selector(
            By.XPATH, "//body/main/div/div[1]/div[2]/div[1]/div[3]/button"
        ),
        "something else": Selector(
            By.XPATH, "//body/main/div/div[1]/div[2]/div[1]/div[2]/div/div[7]/label"
        ),
        "next": Selector(
            By.XPATH, "//body/div[6]/div/div/form/div[2]/div/span/div/section[1]/div/fieldset/button"
        ),


    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    url = SubURLs[page_name] if page_name else URL
    go_to_url(driver, url, page_name or NAME)

def should_be_here(driver: WebDriver, *, page_name: str = None):
    if page_name:
        url = SubURLs[page_name]
        logging.debug(f"visit url info -> {url} {page_name}")
        check_url_path_matches_template(url, driver.current_url)
    else:
        check_url(driver, URL, exact_match=False)


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()

def choose_a_product(driver: WebDriver, product_name: str):
    product_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "choose a product")
    )
    product_btn.click()
    # search_again_top_bottom(driver)
    driver.implicitly_wait(1)
    driver.find_element_by_xpath("//body/div[6]/div/div/form/div[2]/div/div/div[2]/label/div/input").clear()
    driver.find_element_by_xpath("//body/div[6]/div/div/form/div[2]/div/div/div[2]/label/div/input").send_keys(
        product_name)
    driver.find_element_by_xpath("//body/div[6]/div/div/form/div[2]/div/div/div[2]/button/i").click()

    # Inorder to copy this code, 3 elements to be copied
    # as per the element path on the browser
    # save_product_btn, parent_1_div_element, search next button
    # def search_select_save_radio(driver: WebDriver):
    counter = 0
    while True:

        if counter >= 50:
            break
        # logging.debug("Counter: " + str(counter))

        driver.implicitly_wait(1)

        # check for save button
        save_btn_found = False
        try:
            save_product_btn = driver.find_element_by_xpath(
                "//body/div[6]/div/div/form/div[2]/div/span/div/section[1]/button")
            save_btn_found = True
        except Exception as ex:
            logging.debug("save button not found.Exception: " + str(ex))

        if save_btn_found == True:
            logging.debug("Save button found")
            save_product_btn.click()
            return
        # look for div's and radio buttons
        parent_1_div_element = driver.find_element_by_xpath(
            "//body/div[6]/div/div/form/div[2]/div/span/div/section[1]/div")  # ("interaction grid m-v-xs")
        child_1_div_element = parent_1_div_element.find_element_by_tag_name("fieldset")  # ("c-fullwidth")
        main_div_element = child_1_div_element.find_element_by_tag_name("div")  # "m-b-xs"
        # radio button labels
        label_elements = main_div_element.find_elements_by_tag_name("label")
        radio_elements = []
        for label_element in label_elements:
            radio_ele = None
            try:
                radio_ele = label_element.find_element_by_tag_name("input")
            except Exception as e:
                continue
            radio_elements.append(radio_ele)
        # logging.debug('number of labels - ' + str(len(radio_elements)))
        random_label_index = random.randint(0, len(radio_elements) - 1)
        # logging.debug('Index of radio buttons to be selected -> ' + str(random_label_index))

        radio_btn_selected = radio_elements[random_label_index]
        radio_btn_selected.click()

        driver.implicitly_wait(1)
        search_next_btn = find_element(
            driver, find_selector_by_name(SELECTORS, "next")
        )
        search_next_btn.click()

        counter += 1
