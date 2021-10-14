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

NAME = "Export Plan Market"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_START_MARKET_MAKE_AN_EXPORT_PLAN.absolute
PAGE_TITLE = "Export Plan Market"

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
        "next button": Selector(
            By.XPATH, "//body/div[6]/div/div/form/div[2]/div/span/div/section[1]/div/fieldset/button"
        ),
        "start choose a product": Selector(
            By.XPATH, "//body/main/div/div[1]/div[2]/div[1]/div[2]/button"
        ),
        "choose market": Selector(
            By.XPATH, "//body/main/div/div[1]/div[2]/div/div[2]/button"
        ),


    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()

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

def find_and_select_random_item_list(driver: WebDriver, element_selector_name: str):
    #//body/main/div[2]/section[4]/div/div[2]/div/button
    find_and_click(driver, element_selector_name="Add route to market")
    drop_down_btn = driver.find_element_by_xpath(
        "//body/main/div[2]/section[4]/div/div[2]/div/div[1]/div[1]/div/div/div[2]/button"
        )
    drop_down_btn.click()
    # promote_your_product_btn = driver.find_element_by_xpath(
    #     "//body/main/div[2]/section[4]/div/div[2]/div/div/div[2]/div/div/div[3]/div[1]")
    # promote_your_product_btn.click()
    driver.implicitly_wait(5)
    # select__list body-l bg-white radius
    drop_down_element = driver.find_element_by_xpath(
        "//body/main/div[2]/section[4]/div/div[2]/div/div/div[1]/div/div/div[3]/ul")
    # promote_your_product_element = driver.find_element_by_xpath(
    #     "//body/main/div[2]/section[4]/div/div[2]/div/div/div[2]/div/div/div[3]/ul")
    li_elements = drop_down_element.find_elements_by_tag_name("li")
    # li_elements = promote_your_product_element.find_elements_by_tag_name("li")
    # logging.debug("list elements")
    # logging.debug(li_elements)
    random_number = 0
    if len(li_elements) > 2:
        random_number = random.randint(1, len(li_elements) - 1)
    random_li_element = li_elements[random_number]
    # logging.debug(random_number)
    # logging.debug(random_li_element.tag_name)
    # logging.debug(random_li_element)
    time.sleep(2)


def random_select_checkbox(driver: WebDriver, element_name: str):
    find_and_click(driver, element_selector_name="Select")

    random_age_group_element_xpath = "//body/main/div[2]/section[3]/div/div/div[2]/div/div[1]/form/ul/li" \
                                     + "[" + str(random.randint(0, 8)) + "]" + "/label"
    driver.implicitly_wait(1)
    driver.find_element_by_xpath(random_age_group_element_xpath).click()
    find_and_click(driver, element_selector_name="Confirm")


def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()


def fill_out_country(driver: WebDriver, country: str):
    driver.implicitly_wait(1)
    # parent div: //body/div[5]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]
    # parent ul: //body/div[5]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/ul

    # where to export : country search
    # //body/div[8]/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]
    # //body/div[8]/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]/ul

    # country
    country_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "choose market")  # dashboard add country button
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
            "//body/div[6]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/div/section[1]/div[2]/ol")
            #"//body/div[11]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/ul")

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
        driver, find_selector_by_name(SELECTORS, "start choose a product")
    )
    #/html/body/div[6]/div/div/form/div[2]/div/div/div[2]/label/div/input
    #/html/body/div[6]/div/div/form/div[2]/div/span/div/section[1]/div/fieldset
    #next-/html/body/div[6]/div/div/form/div[2]/div/span/div/section[1]/div/fieldset/button
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
            driver, find_selector_by_name(SELECTORS, "next button")
        )
        search_next_btn.click()

        counter += 1
    driver.find_element_by_xpath("//body/main/div/div[1]/div[2]/div[2]/a").click()
