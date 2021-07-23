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

NAME = "Costs and Pricing"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_COSTS_AND_PRICING.absolute
PAGE_TITLE = "Costs and pricing Page"

SELECTORS = {
    "costs and pricing": {
        "product cost educational": Selector(
            By.XPATH,
            "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/div/button/i"
        ),
        "product cost": Selector(
            By.XPATH, "//input[@id='product_costs']", type=ElementType.INPUT
        ),
        "labour cost educational": Selector(
            By.XPATH,
            "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[1]/table/tbody/tr[2]/td[1]/div/div/button/i"
        ),
        "labour cost": Selector(
            By.XPATH, "//input[@id='labour_costs']", type=ElementType.INPUT
        ),
        "additional margin": Selector(
            By.XPATH, "//input[@id='other_direct_costs']", type=ElementType.INPUT
        ),
        "direct costs total": Selector(
            By.XPATH, "//span[@class='body-l-b text-white']"
        ),
        "product adaptation educational": Selector(
            By.XPATH,
            "//body[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[2]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/button[1]/i[1]"
        ),
        "product adaptation": Selector(
            By.XPATH, "//input[@id='product_adaption']", type=ElementType.INPUT
        ),
        "freight and logistics educational": Selector(
            By.XPATH,
            "//body[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[2]/div[3]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/button[1]/i[1]"
        ),
        "freight and logistics": Selector(
            By.XPATH, "//input[@id='freight_logistics']", type=ElementType.INPUT
        ),
        "agent and distribution fees educational": Selector(
            By.XPATH, "//tbody/tr[3]/td[1]/div[1]/div[1]/button[1]/i[1]"
        ),
        "agent and distribution fees": Selector(
            By.XPATH, "//input[@id='agent_distributor_fees']", type=ElementType.INPUT
        ),
        "marketing educational": Selector(
            By.XPATH, "//tbody/tr[4]/td[1]/div[1]/div[1]/button[1]/i[1]"
        ),
        "marketing": Selector(
            By.CSS_SELECTOR, "#marketing", type=ElementType.INPUT
        ),
        "insurance educational": Selector(
            By.XPATH, "//tbody/tr[5]/td[1]/div[1]/div[1]/button[1]/i[1]"
        ),
        "insurance": Selector(
            By.CSS_SELECTOR, "#insurance", type=ElementType.INPUT
        ),
        "other overhead costs": Selector(
            By.XPATH, "#other_overhead_costs", type=ElementType.INPUT
        ),
        "overhead costs total": Selector(
            By.XPATH,
            "//body[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[2]/div[4]/table[1]/tbody[1]/tr[1]/td[2]/span[2]"
        ),
        "number of units": Selector(
            By.CSS_SELECTOR, "#units_to_export"
        ),
        "select unit": Selector(
            By.XPATH,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(16) > div > div.c-1-3 > div > div > div.select__placeholder.text-blue-deep-60.bg-white.radius"
        ),
        "time frame": Selector(
            By.CSS_SELECTOR, "#time_frame"
        ),
        "select time": Selector(
            By.XPATH, "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[6]/div/div[2]/div/div/div[3]"
        ),
        "estimate": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(19) > div.m-b-xs > button"
        ),
        "final cost per unit": Selector(
            By.CSS_SELECTOR, "#final_cost_per_unit"
        ),
        "average price per unit educational": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(20) > div.m-b-xs > div > div > button > i"
        ),
        "average price per unit": Selector(
            By.XPATH, "#average_price_per_unit"
        ),
        "net price example": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(21) > div.m-b-xs > button"
        ),
        "net price educational": Selector(
            By.CSS_SELECTOR,
            "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[9]/div[2]/div[1]/div/div/button/i"
        ),
        "net price": Selector(
            By.XPATH, "//input[@id='net_price']", type=ElementType.INPUT
        ),
        "local taxes example": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(22) > div.m-b-xs > button"
        ),
        "local taxes educational": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(22) > div.m-b-xs > div > div > button > i"
        ),
        "local taxes": Selector(
            By.CSS_SELECTOR, "#local_tax_charges", type=ElementType.INPUT
        ),
        "duty educational": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(23) > div.m-b-xs > div > div > button > i"
        ),
        "duty": Selector(
            By.CSS_SELECTOR, "#duty_per_unit", type=ElementType.INPUT
        ),
        # "select currency": Selector(
        #     By.CSS_SELECTOR, "#cost-and-pricing > section.bg-blue-deep-10.m-t-l.p-v-s > div > div > div.c-1-1.c-2-3-m.c-1-2-xl > div.bg-white.radius.p-xs.c-full.m-b-s.gross-price > div:nth-child(3) > div > div > div.c-1-6.m-r-xs > div > div > div.select__placeholder.text-blue-deep-60.bg-white.radius"
        # ),
        "gross price per unit": Selector(
            By.CSS_SELECTOR, "#gross_price_per_unit_invoicing"
        ),
        "profit per unit": Selector(
            By.XPATH,
            "#cost-and-pricing > section.bg-blue-deep-10.m-t-l.p-v-s > div > div > div.c-1-1.c-2-3-m.c-1-2-xl > div.grid > div:nth-child(1) > div > h3"
        ),
        "potential total profit": Selector(
            By.XPATH,
            "#cost-and-pricing > section.bg-blue-deep-10.m-t-l.p-v-s > div > div > div.c-1-1.c-2-3-m.c-1-2-xl > div.grid > div:nth-child(2) > div > h3"
        ),
        "section complete": Selector(
            By.XPATH, "//label[contains(text(),'Yes')]"
        ),
        "funding and credit": Selector(
            By.CSS_SELECTOR, "#costs-and-pricing-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > a > span"
        ),
        "export plan home": Selector(
            By.CSS_SELECTOR,
            "#costs-and-pricing-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > div.m-t-l > a"
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
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav Adapting Your Product": Selector(
            By.XPATH, "//a[contains(text(),'Adapting Your Product')]"
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


def find_and_select_random_item_list(driver: WebDriver, element_selector_name: str):
    number_of_units_btn = driver.find_element_by_css_selector(
        "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(16) > div > div.c-1-3 > div > button")
    number_of_units_btn.click()
    time_frame_btn = driver.find_element_by_css_selector(
        "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(18) > div > div.c-1-3 > div > button")
    time_frame_btn.click()
    select_currency_btn = driver.find_element_by_css_selector(
        "#cost-and-pricing > section.bg-blue-deep-10.m-t-l.p-v-s > div > div > div.c-1-1.c-2-3-m.c-1-2-xl > div.bg-white.radius.p-xs.c-full.m-b-s.gross-price > div:nth-child(3) > div > div > div.c-1-6.m-r-xs > div > div > div.select__button.text-blue-deep-20.button--toggle.select__button--close > button")
    select_currency_btn.click()

    driver.implicitly_wait(5)
    # select__list body-l bg-white radius
    number_of_units_element = driver.find_element_by_css_selector(
        "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(16) > div > div.c-1-3 > div > ul")
    time_frame_element = driver.find_element_by_css_selector(
        "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(18) > div > div.c-1-3 > div > ul")
    select_currency_element = driver.find_element_by_css_selector(
        "#cost-and-pricing > section.bg-blue-deep-10.m-t-l.p-v-s > div > div > div.c-1-1.c-2-3-m.c-1-2-xl > div.bg-white.radius.p-xs.c-full.m-b-s.gross-price > div:nth-child(3) > div > div > div.c-1-6.m-r-xs > div > div > ul")

    li_elements = number_of_units_element.find_elements_by_tag_name("li")
    li_elements = time_frame_element.find_elements_by_tag_name("li")
    li_elements = select_currency_element.find_elements_by_tag_name("li")
    logging.debug("list elements")
    logging.debug(li_elements)
    random_number = 0
    if len(li_elements) > 2:
        random_number = random.randint(1, len(li_elements) - 1)
    random_li_element = li_elements[random_number]


def enter_direct_costs(driver: WebDriver, productcost: str, labourcost: str, additionalmargin: str):
    base_element_xpath = "//body/main/div[2]/div/section[1]/div/div[2]/div[1]/table/tbody/tr"
    productcost_ele_xpath = base_element_xpath + "[" + "1" + "]/td[2]/div/div[2]/input"
    labourcost_xpath = base_element_xpath + "[" + "2" + "]/td[2]/div/div[2]/input"
    additionalmargin_xpath = base_element_xpath + "[" + "3" + "]/td[2]/div/div[2]/input"

    # clear text
    driver.find_element_by_xpath(productcost_ele_xpath).clear()
    time.sleep(2)
    driver.find_element_by_xpath(labourcost_xpath).clear()
    # driver.implicitly_wait(1)
    time.sleep(2)
    driver.find_element_by_xpath(additionalmargin_xpath).clear()
    # driver.implicitly_wait(1)
    time.sleep(2)
    # send data to elements
    driver.find_element_by_xpath(productcost_ele_xpath).send_keys(productcost)
    time.sleep(2)
    driver.find_element_by_xpath(labourcost_xpath).send_keys(labourcost)
    time.sleep(2)
    driver.find_element_by_xpath(additionalmargin_xpath).send_keys(additionalmargin)
    time.sleep(2)
    # driver.implicitly_wait(5)
    # wait and then check the summation of all fields
    summation = int(productcost) + int(labourcost) + int(additionalmargin)
    summation_ele_xpath = "//body/main/div[2]/div/section[1]/div/div[2]/div[2]/table/tbody/tr/td[2]/span[2]"
    summation_ele_value = driver.find_element_by_xpath(summation_ele_xpath).text
    if float(summation) == float(summation_ele_value):
        raise Exception("Direct Costs Summation do not match")
    # //body/main/div[2]/div/section[1]/div/div[2]/div[4]/table/tbody/tr/td[2]/span[2]


def enter_overhead_costs(driver: WebDriver, productadaptation: str, freightandlogistics: str,
                         agentanddistributionfees: str, marketing: str, insurance: str):
    base_element_xpath = "//body/main/div[2]/div/section[1]/div/div[2]/div[3]/table/tbody/tr"

    productadaptation_ele_xpath = base_element_xpath + "[" + "1" + "]/td[2]/div/div[2]/input"
    freightandlogistics_xpath = base_element_xpath + "[" + "2" + "]/td[2]/div/div[2]/input"
    agentanddistributionfees_xpath = base_element_xpath + "[" + "3" + "]/td[2]/div/div[2]/input"
    marketing_xpath = base_element_xpath + "[" + "3" + "]/td[2]/div/div[2]/input"
    insurance_xpath = base_element_xpath + "[" + "3" + "]/td[2]/div/div[2]/input"

    # clear text
    driver.find_element_by_xpath(productadaptation_ele_xpath).clear()
    time.sleep(1)
    driver.find_element_by_xpath(freightandlogistics_xpath).clear()
    time.sleep(1)
    driver.find_element_by_xpath(agentanddistributionfees_xpath).clear()
    time.sleep(1)
    driver.find_element_by_xpath(marketing_xpath).clear()
    time.sleep(1)
    driver.find_element_by_xpath(insurance_xpath).clear()
    time.sleep(1)
    # time.sleep(1)
    # send data to elements
    driver.find_element_by_xpath(productadaptation_ele_xpath).send_keys(productadaptation)
    time.sleep(2)
    driver.find_element_by_xpath(freightandlogistics_xpath).send_keys(freightandlogistics)
    time.sleep(2)
    driver.find_element_by_xpath(agentanddistributionfees_xpath).send_keys(agentanddistributionfees)
    time.sleep(2)
    driver.find_element_by_xpath(marketing_xpath).send_keys(marketing)
    time.sleep(2)
    driver.find_element_by_xpath(insurance_xpath).send_keys(insurance)

    time.sleep(2)

    # wait and then check the summation of all fields
    summation = int(productadaptation) + int(freightandlogistics) + int(agentanddistributionfees) + int(
        marketing) + int(insurance)
    summation_ele_xpath = "//body/main/div[2]/div/section[1]/div/div[2]/div[4]/table/tbody/tr/td[2]/span[2]"
    summation_ele_value = driver.find_element_by_xpath(summation_ele_xpath).text
    if float(summation) == float(summation_ele_value):
        raise Exception("Overhead Costs Summation do not match")
    time.sleep(2)
    # //body/main/div[2]/div/section[1]/div/div[2]/div[4]/table/tbody/tr/td[2]/span[2]


def enter_value(driver: WebDriver, element_name: str):
    value_element = find_element(
        driver, find_selector_by_name(SELECTORS, element_name)
    )
    value_element.clear()
    value_element.send_keys("20")
    time.sleep(2)
