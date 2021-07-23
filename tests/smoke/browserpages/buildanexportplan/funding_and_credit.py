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
    fill_out_email_address,
    fill_out_textarea_fields,
)

NAME = "Funding and credit"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_FUNDING_AND_CREDIT.absolute
PAGE_TITLE = "Funding and credit Page"

SELECTORS = {
    "funding and credit": {
        "estimate": Selector(
            By.CSS_SELECTOR, "#finance-total-export-cost > div > div.m-b-xs > button"
        ),
        "estimate input": Selector(
            By.XPATH, "//input[@id='override_estimated_total_cost']", type=ElementType.INPUT
        ),
        "how much funding": Selector(
            By.XPATH, "//input[@id='funding_amount_required']", type=ElementType.INPUT
        ),
        "Add a funding option": Selector(
            By.XPATH, "//span[contains(text(),'Add a funding option')]"
        ),
        "select option": Selector(
            By.XPATH, "//tbody/tr[1]/td[1]/div[1]/button[1]"
        ),
        "credit option": Selector(
            By.XPATH, "//input[@id='21']", type=ElementType.INPUT
        ),
        "delete": Selector(
            By.XPATH, "//tbody/tr[2]/td[1]/button[1]/i[1]"
        ),
        "section complete": Selector(
            By.XPATH, "//label[contains(text(),'Yes')]"
        ),
        "getting paid": Selector(
            By.XPATH, "//span[contains(text(),'Getting paid')]"
        ),
        "export plan home": Selector(
            By.CSS_SELECTOR,
            "#funding-and-credit-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > div.m-t-l > a"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav getting paid": Selector(
            By.XPATH, "//a[contains(text(),'Getting paid')]"
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
        "avoid cashflow challenges when exporting": Selector(
            By.XPATH, "//h4[contains(text(),'Avoid cashflow challenges when exporting')]"
        ),
        "choose the right funding": Selector(
            By.XPATH, "//h4[contains(text(),'Choose the right funding and credit options')]"
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


def enter_business_objectives_details(driver: WebDriver, startdate: str, enddate: str, objectives: str, owner: str,
                                      plannedreviews: str):
    input_field_selectors = SELECTORS["business objectives"]
    input_details_dict = {"start date": startdate, "end date": enddate, "owner": owner}
    fill_out_input_fields(driver, input_field_selectors, input_details_dict)

    text_area_details_dict = {"objective text": objectives, "planned review": plannedreviews}
    fill_out_textarea_fields(driver, input_field_selectors, text_area_details_dict)
    time.sleep(1)


def enter_value(driver: WebDriver, element_name: str):
    value_element = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    value_element.clear()
    value_element.send_keys("5000")
    time.sleep(2)


def find_and_select_random_funding_options(driver: WebDriver, position: str, amount: str):
    # every call of this function, click on Add Goal
    find_and_click(driver, element_selector_name="Add a funding option")
    driver.implicitly_wait(5)

    actual_positon = 1
    if int(position) != 1:
        actual_positon = int(position) + (int(position) - 1)

    # funding_option_element_xpath = "//body/main/div[2]/div/div/div[2]/div/div[3]/div[1]/table/tbody/tr" + "[" + str(actual_positon) + "]"
    # funding_option_1_element = funding_option_element_xpath + "/td[1]/div/div/div[2]/button"
    # driver.find_element_by_xpath(funding_option_1_element).click()
    # driver.implicitly_wait(5)
    #
    # #driver.implicitly_wait(5)
    # #/html/body/main/div[2]/div/div/div[2]/div/div[3]/div[1]/table/tbody/tr[1]/td[1]/div/div/ul/li[3]
    # ulist_funding_options_xpath = "//body/main/div[2]/div/div/div[2]/div/div[3]/div[1]/table/tbody/tr[1]/td[1]/div/div/ul"
    # ulist_funding_options_element = driver.find_element_by_xpath(ulist_funding_options_xpath)
    # funding_options_elements = ulist_funding_options_element.find_elements_by_tag_name("li")
    #
    # random_number = 0
    # if len(funding_options_elements) > 2:
    #     random_number = random.randint(1, len(funding_options_elements) - 1)
    # #random_li_element = funding_options_elements[random_number]
    # #random_li_element.click()
    # random_li_element = driver.find_element_by_xpath(ulist_funding_options_xpath + "/li[" + str(random_number) + "]")
    # random_li_element.click()
    # time.sleep(2)

    gbp_elem_xpath = "//body/main/div[2]/div/div/div[2]/div/div[3]/div[1]/table/tbody/tr" + "[" + str(
        actual_positon) + "]"
    gbp_text_elem_xpath = gbp_elem_xpath + "/td[2]/div/div[2]/input"
    driver.find_element_by_xpath(gbp_text_elem_xpath).clear()
    driver.find_element_by_xpath(gbp_text_elem_xpath).send_keys(amount)
    time.sleep(2)

    # try to run the code
    #
    #
    #
    #
    #
    #
    # funding_option_1_drop_down_element = driver.find_element_by_css_selector("#finance-funding-credit-options > div.costs.costs--funding.bg-blue-deep-10.p-v-s > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > ul")
    # funding_option_2_drop_down_element = driver.find_element_by_css_selector("#finance-funding-credit-options > div.costs.costs--funding.bg-blue-deep-10.p-v-s > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > ul")
    # funding_option_3_drop_down_element = driver.find_element_by_css_selector("#finance-funding-credit-options > div.costs.costs--funding.bg-blue-deep-10.p-v-s > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > ul")
    # funding_option_4_drop_down_element = driver.find_element_by_css_selector("#finance-funding-credit-options > div.costs.costs--funding.bg-blue-deep-10.p-v-s > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > ul")
    # funding_option_5_drop_down_element = driver.find_element_by_css_selector("#finance-funding-credit-options > div.costs.costs--funding.bg-blue-deep-10.p-v-s > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > ul")
    # li_elements = funding_option_1_drop_down_element.find_elements_by_tag_name("li")
    # li_elements = funding_option_2_drop_down_element.find_elements_by_tag_name("li")
    # li_elements = funding_option_3_drop_down_element.find_elements_by_tag_name("li")
    # li_elements = funding_option_4_drop_down_element.find_elements_by_tag_name("li")
    # li_elements = funding_option_5_drop_down_element.find_elements_by_tag_name("li")
    #
    # random_number = 0
    # if len(li_elements) > 2:
    #     random_number = random.randint(1, len(li_elements)-1)
    # random_li_element = li_elements[random_number]

    # time.sleep(1)


def delete_all_funding_options(driver: WebDriver, position: str):
    actual_position = int(position) * 2
    objective_div_element_xpath = "/html/body/main/div[2]/div/div/div[2]/div/div[3]/div[1]/table/tbody/tr" + "[" + str(
        actual_position) + "]"
    del_btn_ele_xpath = objective_div_element_xpath + "/td/button"

    driver.find_element_by_xpath(del_btn_ele_xpath).click()
    time.sleep(1)
