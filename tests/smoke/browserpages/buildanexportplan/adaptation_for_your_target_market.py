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

NAME = "Adapting Your Product"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_ADAPTING_YOUR_PRODUCT.absolute
PAGE_TITLE = "Adapting Your Product Page"

SELECTORS = {
    "Adapting Your Product": {
        "open data snapshot": Selector(
            By.CSS_SELECTOR, "#stats-for-target-market > div > button"
        ),
        "hide data snapshot": Selector(
            By.CSS_SELECTOR, "#stats-for-target-market > div.m-t-s > button"
        ),
        "labelling educational": Selector(
            By.XPATH, "//*[@id=\"adapt-to-target-market\"]/div/div/div[1]/div/div/div/button/i"
        ),
        "labelling": Selector(
            By.XPATH, "//*[@id=\"labelling\"]", type=ElementType.INPUT
        ),
        "packaging educational": Selector(
            By.XPATH, "//*[@id=\"adapt-to-target-market\"]/div/div/div[2]/div/div/div/button/i"
        ),
        "packaging": Selector(
            By.XPATH, "//*[@id=\"packaging\"]", type=ElementType.INPUT
        ),
        "size educational": Selector(
            By.XPATH, "//*[@id=\"adapt-to-target-market\"]/div/div/div[3]/div/div/div/button/i"
        ),
        "size": Selector(
            By.XPATH, "//*[@id=\"size\"]", type=ElementType.INPUT
        ),
        "product changes to comply educational": Selector(
            By.XPATH, "//*[@id=\"adapt-to-target-market\"]/div/div/div[4]/div/div/div/button/i"
        ),
        "product changes to comply": Selector(
            By.XPATH, "//*[@id=\"standards\"]", type=ElementType.INPUT
        ),
        "translations educational": Selector(
            By.XPATH, "//*[@id=\"adapt-to-target-market\"]/div/div/div[5]/div/div/div/button/i"
        ),
        "translations": Selector(
            By.XPATH, "//*[@id=\"translations\"]", type=ElementType.INPUT
        ),
        "other changes": Selector(
            By.XPATH, "//*[@id=\"other_changes\"]", type=ElementType.INPUT
        ),
        "certificate of origin educational": Selector(
            By.XPATH, "//body/main/div[2]/section[6]/div/div/div/form/div/div/div[1]/textarea"
            # "//*[@id=\"documents-for-target-market\"]/div/div/div[1]/div/div/div/button/i"
        ),
        "certificate of origin": Selector(
            By.XPATH, "//*[@id=\"certificate_of_origin\"]", type=ElementType.INPUT
        ),
        "insurance certificate educational": Selector(
            By.XPATH, "//*[@id=\"documents-for-target-market\"]/div/div/div[2]/div/div/div/button/i"
        ),
        "insurance certificate": Selector(
            By.XPATH, "//*[@id=\"insurance_certificate\"]", type=ElementType.INPUT
        ),
        "commercial invoice educational": Selector(
            By.XPATH, "//*[@id=\"documents-for-target-market\"]/div/div/div[3]/div/div/div/button/i"
        ),
        "commercial invoice": Selector(
            By.XPATH, "//*[@id=\"commercial_invoice\"]", type=ElementType.INPUT
        ),
        "uk customs declaration educational": Selector(
            By.XPATH, "//*[@id=\"documents-for-target-market\"]/div/div/div[4]/div/div/div/button/i"
        ),
        "uk customs declaration": Selector(
            By.XPATH, "//*[@id=\"uk_customs_declaration\"]", type=ElementType.INPUT
        ),
        "delete": Selector(
            By.CSS_SELECTOR,
            "#documents-for-target-market > div > div > div.target-market-documents-form > div > div.form-delete.m-b-xs > button > i"
        ),
        "add another document": Selector(
            By.XPATH, "//span[contains(text(),'Add another document')]"
        ),
        "yes checkbox": Selector(
            By.CSS_SELECTOR, "#section-complete > div > label"
        ),
        "marketing approach": Selector(
            By.XPATH, "//*[@id=\"adaptation-for-your-target-market-content\"]/section[7]/div/div/div[2]/a/span"
        ),
        "export plan home": Selector(
            By.XPATH, "//*[@id=\"adaptation-for-your-target-market-content\"]/section[7]/div/div/div[2]/div/a"
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
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav marketing approach": Selector(
            By.XPATH, "//a[contains(text(),'Marketing approach')]"
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


def enter_document_details(driver: WebDriver, position: str, document_name: str, notes: str):
    # every call of this function, click on Add Goal
    find_and_click(driver, element_selector_name="Add another document")
    time.sleep(2)
    document_div_element_xpath = "/html/body/main/div[2]/section[6]/div/div/div/form/div/div/div[5]/div" + "[" + position + "]"
    document_text_ele_xpath = document_div_element_xpath + "/div[1]/div[2]/input"
    notes_ele_xpath = document_div_element_xpath + "/div[2]/textarea"

    driver.find_element_by_xpath(document_text_ele_xpath).send_keys(document_name)
    driver.find_element_by_xpath(notes_ele_xpath).send_keys(notes)
    time.sleep(2)


def delete_all_document_details(driver: WebDriver, position: str,del_button_position:str):
    document_div_element_xpath = "/html/body/main/div[2]/section[6]/div/div/div/form/div/div/div[5]/div" + "[" + position + "]"
    del_btn_ele_xpath = document_div_element_xpath + "/div[3]/button/i"
    driver.find_element_by_xpath(del_btn_ele_xpath).click()
    time.sleep(1)

