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

NAME = "Adapting your Product"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_ADAPTING_YOUR_PRODUCT.absolute_template
PAGE_TITLE = "Adapting your Product"

SELECTORS = {
    "adapting your Product": {
        "open data snapshot": Selector(
            By.CSS_SELECTOR, "#stats-for-target-market > div > button"
        ),
        "hide data snapshot": Selector(
            By.CSS_SELECTOR, "#stats-for-target-market > div.m-t-s > button"
        ),
        "labelling educational": Selector(
            By.XPATH, "//*[@id=\"changes-to-product\"]/div[2]/div/div[1]/div/div[1]/div/div/button/i"
        ),
        "labelling": Selector(
            By.XPATH, "//*[@id=\"labelling\"]", type=ElementType.INPUT
        ),
        "packaging educational": Selector(
            By.XPATH, "//*[@id=\"changes-to-product\"]/div[2]/div/div[2]/div/div[1]/div/div/button/i"
        ),
        "packaging": Selector(
            By.XPATH, "//*[@id=\"packaging\"]", type=ElementType.INPUT
        ),
        "size educational": Selector(
            By.XPATH, "//*[@id=\"changes-to-product\"]/div[2]/div/div[3]/div/div[1]/div/div/button/i"
        ),
        "size": Selector(
            By.XPATH, "//*[@id=\"size\"]", type=ElementType.INPUT
        ),
        "product changes to comply educational": Selector(
            By.XPATH,
            "//body/main/div[2]/section[5]/div/div[2]/div/div[2]/div/div[4]/div/div[1]/div/div/button/span"
        ),
        "product changes to comply": Selector(
            By.XPATH, "//*[@id=\"standards\"]", type=ElementType.INPUT
        ),
        "translations educational": Selector(
            By.XPATH, "//*[@id=\"changes-to-product\"]/div[2]/div/div[5]/div/div[1]/div/div/button/i"
        ),
        "translations": Selector(
            By.XPATH, "//*[@id=\"translations\"]", type=ElementType.INPUT
        ),
        "other changes": Selector(
            By.XPATH, "//*[@id=\"other_changes\"]", type=ElementType.INPUT
        ),
        "certificate of origin educational": Selector(
            By.XPATH, "//*[@id=\"documents-for-target-market\"]/div/div/div[1]/div/div[1]/div/div/button/i"
            # "//*[@id=\"documents-for-target-market\"]/div/div/div[1]/div/div/div/button/i"
        ),
        "certificate of origin": Selector(
            By.XPATH, "//*[@id=\"certificate_of_origin\"]", type=ElementType.INPUT
        ),
        "insurance certificate educational": Selector(
            By.XPATH, "//*[@id=\"documents-for-target-market\"]/div/div/div[2]/div/div[1]/div/div/button/i"
        ),
        "insurance certificate": Selector(
            By.XPATH, "//*[@id=\"insurance_certificate\"]", type=ElementType.INPUT
        ),
        "commercial invoice educational": Selector(
            By.CSS_SELECTOR,
            "//body/main/div[2]/section[6]/div/div[2]/div/form/div[2]/div/div[3]/div/div[1]/div/div/button"
        ),
        "commercial invoice": Selector(
            By.XPATH, "//*[@id=\"commercial_invoice\"]", type=ElementType.INPUT
        ),
        "uk customs declaration educational": Selector(
            By.XPATH, "//*[@id=\"documents-for-target-market\"]/div/div/div[4]/div/div[1]/div/div/button/i"
        ),
        "uk customs declaration": Selector(
            By.XPATH, "//*[@id=\"uk_customs_declaration\"]", type=ElementType.INPUT
        ),
        # "delete": Selector(
        #     By.CSS_SELECTOR,
        #     "#documents-for-target-market > div > div > div.target-market-documents-form > div > div.form-delete.m-b-xs > button > i"
        # ),
        "add another document": Selector(
            By.XPATH, "//body/main/div[2]/section[6]/div/div[2]/div/div[2]/div/button"
        ),
        "yes checkbox": Selector(
            By.CSS_SELECTOR, "#section-complete > div > label"
        ),
        "marketing approach": Selector(
            By.XPATH, "//*[@id=\"adapting-your-product-content\"]/section[7]/div/div/div[2]/a/span"
        ),
        "export plan home": Selector(
            By.XPATH, "//*[@id=\"adapting-your-product-content\"]/section[7]/div/div/div[2]/div[2]/a/span"
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
            By.XPATH, "//body/main/div[2]/section[1]/div/div/div[2]/span/a/span"
            # //*[@id=\"adapting-your-product-content\"]/section[1]/div/div/div[2]/a/span"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav marketing approach": Selector(
            By.XPATH, "//*[@id=\"collapseNav\"]/div/ul/li[5]/a"
        ),
        "search next button": Selector(
            By.XPATH, "//body/div[9]/div/div/form/div[2]/div/span/div/section/div/div/button"
        ),
        "dashboard": Selector(
            By.XPATH, "//a[contains(text(),'Dashboard')]"
        ),
        "adapting lesson": Selector(
            By.XPATH,"//body/main/div[2]/section[5]/div/div[2]/div/div[1]/div[1]/button"
        ),
        "adapting your product or service": Selector(
            By.XPATH,"//body/main/div[2]/section[5]/div/div[2]/div/div[1]/div[2]/a"
        ),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url_path_matches_template(URL, driver.current_url)


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
    document_div_element_xpath = "/html/body/main/div[2]/section[6]/div/div[2]/div/div[2]/div/div[5]/div" + "[" + position + "]"
    document_text_ele_xpath = document_div_element_xpath + "/div[1]/div[2]/input"
    notes_ele_xpath = document_div_element_xpath + "/div[2]/textarea"

    driver.find_element_by_xpath(document_text_ele_xpath).send_keys(document_name)
    driver.find_element_by_xpath(notes_ele_xpath).send_keys(notes)
    time.sleep(2)


def delete_all_document_details(driver: WebDriver, position: str,del_button_position:str):
    # /html/body/main/div[2]/section[6]/div/div[2]/div/div[2]/div/div[5]/div[5]/
    document_div_element_xpath = "/html/body/main/div[2]/section[6]/div/div[2]/div/div[2]/div/div[5]/div" + "[" + position + "]"
    # del_btn_ele_xpath = document_div_element_xpath + "/div[3]/button/i"
    # driver.find_element_by_xpath(del_btn_ele_xpath).click()
    time.sleep(1)
    document_div_element_xpath_text_exists == True
    try:
        document_div_element_xpath_text = driver.find_element_by_xpath(document_div_element_xpath).text
        if document_div_element_xpath_text == None or len(document_div_element_xpath_text) <= 0:
            document_div_element_xpath_text_exists = False
    except Exception as e:
        logging.error(e)
        document_div_element_xpath_text_exists = False
    # /html/body/main/div[2]/section[4]/div/div[2]/div/
    if document_div_element_xpath_text_exists == True:
        driver.implicitly_wait(1)
        # 12,13,14,15.......
        # 12 + (1 - 1), 12 + (2 - 1), 12 + (3 - 1), 12 + (4 - 1),.........
        # /html/body/div[16]/div/div/div/div[2]/div[2]/button[1]/i
        # /html/body/div[13]/div/div/div/div[2]/div[2]/button[1]
        delete_msg_yes_index = int(12 + (int(del_button_position) - 1))
        delete_message_yes_element_xpath = "//body/div" + "[" + str(
            delete_msg_yes_index) + "]" + "/div/div/div/div[2]/div[2]/button[1]"
        logging.debug(delete_message_yes_element_xpath)
        delete_message_yes_element = driver.find_element_by_xpath(delete_message_yes_element_xpath)
        delete_message_yes_element.click()
        # time.sleep(1)
    else:
        logging.debug(
            "document_div_element_xpath_text_exists is False for del_button_position " + str(del_button_position))


def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()

def delete_all_document_details(driver: WebDriver, del_button_position: str):
    # 1,3,5,7,......
    # //body/main/div[2]/section[6]/div/div[2]/div/form/div[2]/div/div[5]/div[5]
    # del_button_position: 5,4,3,2,1
    document_div_element_xpath = "//body/main/div[2]/section[6]/div/div[2]/div/form/div[2]/div/div[5]/div" + "[" + del_button_position + "]"
    del_btn_ele_xpath = document_div_element_xpath + "/div[3]/button"
    driver.find_element_by_xpath(del_btn_ele_xpath).click()
    logging.debug("del_button_position " + str(del_button_position))

    # //body/div[12]/div/div/div/div[2]/div[2]/button[1]
    driver.implicitly_wait(1)
    delete_msg_yes_index = int(12 + (int(del_button_position) - 1))
    delete_message_yes_element_xpath = "//body/div" + "[" + str(
        delete_msg_yes_index) + "]" + "/div/div/div/div[2]/div[2]/button[1]"
    logging.debug(delete_message_yes_element_xpath)
    delete_message_yes_element = driver.find_element_by_xpath(delete_message_yes_element_xpath)
    delete_message_yes_element.click()
