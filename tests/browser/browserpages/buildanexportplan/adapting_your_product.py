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
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_ADAPTING_YOUR_PRODUCT.absolute
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
            By.XPATH, "//*[@id=\"changes-to-product\"]/div[2]/div/div[4]/div/div[1]/div/div/button/i"
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
            By.XPATH, "//*[@id=\"documents-for-target-market\"]/div/div/div[3]/div/div[1]/div/div/button"
            #"//body/main/div[2]/section[6]/div/div[2]/div/form/div[2]/div/div[3]/div/div[1]/div/div/button/span"
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
            By.XPATH, "//*[@id=\"documents-for-target-market\"]/div/div/button"
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
            By.XPATH, "//body/main/div[2]/section[1]/div/div/div[2]/span/a/span" #//*[@id=\"adapting-your-product-content\"]/section[1]/div/div/div[2]/a/span"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav marketing approach": Selector(
            By.XPATH, "//*[@id=\"collapseNav\"]/div/ul/li[5]/a"
        ),
        "search next button" : Selector(
            By.XPATH, "//body/div[9]/div/div/form/div[2]/div/span/div/section/div/div/button"
        ),
        "dashboard": Selector(
            By.XPATH, "//a[contains(text(),'Dashboard')]"
        ),
        "lesson": Selector(
            By.XPATH,
            "//*[@id=\"changes-to-product\"]/div[1]/div[1]/button"
        ),
        "adapting your product or service": Selector(
            By.XPATH,
            "//*[@id=\"changes-to-product\"]/div[1]/div[2]/a/div/h4"
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


# def delete_all_document_details(driver: WebDriver, position: str,del_button_position:str):
#     document_div_element_xpath = "/html/body/main/div[2]/section[6]/div/div/div/form/div/div/div[5]/div" + "[" + position + "]"
#     del_btn_ele_xpath = document_div_element_xpath + "/div[3]/button/i"
#     driver.find_element_by_xpath(del_btn_ele_xpath).click()
#     time.sleep(1)

def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()

def fill_out_country(driver: WebDriver, country: str):
    driver.implicitly_wait(1)

    country_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "add a target market")  # dashboard add country button
    )
    country_btn.click()

    # try:
    #     if driver.find_element_by_xpath("//button[contains(text(),'Got it')]").is_displayed():
    #         driver.find_element_by_xpath("//button[contains(text(),'Got it')]").click()
    # except:
    #     pass

    if 0 == len(country):
        # if country name is not provided from the test case, then select one of the random 5 countries listed on the browser
        path_random_country_element = "body > div:nth-child(13) > div > div > div > div > div > div.only-desktop > div.suggested-markets > ul > button:nth-child(" + str(
            random.randint(1, 5)) + ")"
        driver.find_element_by_css_selector(path_random_country_element).click()
    else:
        # search using the provide country name from the test case
        driver.find_element_by_css_selector("#search-input").clear()
        driver.find_element_by_css_selector("#search-input").send_keys(country)

        # look out for the list displayed after entering country name and select random/provided country
        ul_list_element = driver.find_element_by_xpath(
            "//body/div[11]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/ul")


        section_elements = ul_list_element.find_elements_by_tag_name("section")
        logging.debug("length of section elements " + str(len(section_elements)))
        # select random section element and within that select a country
        index_random_element_to_be_selected = random.randint(0, len(section_elements) - 1)
        logging.debug("Index of section elements " + str(index_random_element_to_be_selected))
        section_element_selected = section_elements[index_random_element_to_be_selected]
        logging.debug(section_element_selected)

        div_elements = section_element_selected.find_elements_by_tag_name("div")  # 2 has to be present
        logging.debug("length of div elements " + str(len(div_elements)))
        level_1_div_element = div_elements[
            1]  # section_element_selected.find_element_by_class_name("p-t-s expand-section open")
        level_2_div_element = level_1_div_element.find_element_by_tag_name("div")
        span_elements = level_2_div_element.find_elements_by_tag_name("span")
        logging.debug("length of span elements " + str(len(span_elements)))
        # select random span element and within that select a country
        index_random_element_to_be_selected = random.randint(0, len(span_elements) - 1)
        span_element_selected = span_elements[index_random_element_to_be_selected]
        li_element = span_element_selected.find_element_by_tag_name("li")
        # finally arrived at country name button(s)
        buttons_elements = li_element.find_elements_by_tag_name("button")
        logging.debug("length of country button elements " + str(len(buttons_elements)))
        country_name_found = False
        for button_element in buttons_elements:
            if str(button_element.text).lower() == country.lower():
                country_name_found = True
                button_element.click()
                time.sleep(2)
                break
        if country_name_found == False:
            raise Exception("Country name could not be found " + str(country))


def fill_out_product(driver: WebDriver, product_name: str):
    product_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "add a product")
    )
    product_btn.click()
    #search_again_top_bottom(driver)
    driver.implicitly_wait(1)
    driver.find_element_by_xpath("//body/div[9]/div/div/form/div[2]/div/div/div[2]/label/div/input").clear()
    driver.find_element_by_xpath("//body/div[9]/div/div/form/div[2]/div/div/div[2]/label/div/input").send_keys(
        product_name)
    driver.find_element_by_xpath("//body/div[9]/div/div/form/div[2]/div/div/div[2]/button/i").click()


# Inorder to copy this code, 3 elements to be copied
# as per the element path on the browser
# save_product_btn, parent_1_div_element, search next button
#def search_select_save_radio(driver: WebDriver):
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
                "//body/div[9]/div/div/form/div[2]/div/span/div/section[1]/div[2]/button")
            save_btn_found = True
        except Exception as ex:
            logging.debug("save button not found.Exception: " + str(ex))

        if save_btn_found == True:
            logging.debug("Save button found")
            save_product_btn.click()
            return
        # look for div's and radio buttons
        parent_1_div_element = driver.find_element_by_xpath(
            "//body/div[9]/div/div/form/div[2]/div/span/div/section[1]/div")  # ("interaction grid m-v-xs")
        child_1_div_element = parent_1_div_element.find_element_by_tag_name("div")  # ("c-fullwidth")
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
            driver, find_selector_by_name(SELECTORS, "search next button")
        )
        search_next_btn.click()

        counter += 1

def delete_all_document_details(driver: WebDriver, del_button_position:str):
    # 1,3,5,7,......

    # del_button_position: 5,4,3,2,1
    document_div_element_xpath = "//body/main/div[2]/section[6]/div/div[2]/div/form/div/div/div[5]/div" + "[" + del_button_position + "]"
    del_btn_ele_xpath = document_div_element_xpath + "/div[3]/button"
    driver.find_element_by_xpath(del_btn_ele_xpath).click()
    logging.debug("del_button_position " + str(del_button_position))

    driver.implicitly_wait(1)
    delete_msg_yes_index = int(12 + (int(del_button_position) - 1))
    delete_message_yes_element_xpath = "//body/div" + "[" + str(
        delete_msg_yes_index) + "]" + "/div/div/div/div[2]/div[2]/button[1]"
    logging.debug(delete_message_yes_element_xpath)
    delete_message_yes_element = driver.find_element_by_xpath(delete_message_yes_element_xpath)
    delete_message_yes_element.click()
