import logging
import random
import time
from types import ModuleType
from typing import List, Union

from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Actor,
    Selector,
    assertion_msg,
    check_for_sections,
    check_if_element_is_not_present,
    check_if_element_is_visible,
    check_random_radio,
    check_url,
    fill_out_email_address,
    fill_out_input_fields,
    find_element,
    find_elements,
    find_selector_by_name,
    go_to_url,
    is_element_present,
    pick_option,
    submit_form,
    take_screenshot,
    wait_for_page_load_after_action,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from great_magna_tests_shared.utils import check_url_path_matches_template

NAME = "Costs and Pricing"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_COSTS_AND_PRICING.absolute_template
PAGE_TITLE = "Costs and pricing Page"

SELECTORS = {
    "costs and pricing": {
        "product cost educational": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[1]/div[1]/div/div[1]/div/div"
            # "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/div/button/i"
        ),
        "product cost": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/input",
            type=ElementType.INPUT,
        ),
        "labour cost educational": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/button"
            # "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[1]/table/tbody/tr[2]/td[1]/div/div/button/i"
        ),
        "labour cost": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/input",
            type=ElementType.INPUT,
        ),
        "additional margin": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[1]/div[3]/div/div[2]/div/div[2]/input",
            type=ElementType.INPUT,
        ),
        "direct costs total": Selector(
            By.XPATH, "//span[@class='body-l-b text-white']"
        ),
        "product adaptation educational": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[3]/div[1]/div/div[1]/div/div"
            # "//body[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[2]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/button[1]/i[1]"
        ),
        "product adaptation": Selector(
            By.XPATH, "//input[@id='product_adaption']", type=ElementType.INPUT
        ),
        "freight and logistics educational": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[3]/div[2]/div/div[1]/div/div"
            # "//body[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[2]/div[3]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/button[1]/i[1]"
        ),
        "freight and logistics": Selector(
            By.XPATH, "//input[@id='freight_logistics']", type=ElementType.INPUT
        ),
        "agent and distribution fees educational": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[3]/div[3]/div/div[1]/div/div"
            # "//tbody/tr[3]/td[1]/div[1]/div[1]/button[1]/i[1]"
        ),
        "agent and distribution fees": Selector(
            By.XPATH, "//input[@id='agent_distributor_fees']", type=ElementType.INPUT
        ),
        "marketing educational": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[3]/div[4]/div/div[1]/div/div"
            # "//tbody/tr[4]/td[1]/div[1]/div[1]/button[1]/i[1]"
        ),
        "marketing": Selector(By.CSS_SELECTOR, "#marketing", type=ElementType.INPUT),
        "insurance educational": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[3]/div[5]/div/div[1]/div/div"
            # "//tbody/tr[5]/td[1]/div[1]/div[1]/button[1]/i[1]"
        ),
        "insurance": Selector(By.CSS_SELECTOR, "#insurance", type=ElementType.INPUT),
        "other overhead costs": Selector(
            By.XPATH, "#other_overhead_costs", type=ElementType.INPUT
        ),
        "overhead costs total": Selector(
            By.XPATH,
            "//body[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[2]/div[4]/table[1]/tbody[1]/tr[1]/td[2]/span[2]",
        ),
        "number of units": Selector(By.CSS_SELECTOR, "#units_to_export"),
        "select unit": Selector(
            By.XPATH,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(16) > div > div.c-1-3 > div > div > div.select__placeholder.text-blue-deep-60.bg-white.radius",
        ),
        "time frame": Selector(By.CSS_SELECTOR, "#time_frame"),
        "select time": Selector(
            By.XPATH,
            '//*[@id="cost-and-pricing"]/section[1]/div/div[2]/div[6]/div/div[2]/div/div/div[3]',
        ),
        "estimate": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(19) > div.m-b-xs > button",
        ),
        "final cost per unit": Selector(By.CSS_SELECTOR, "#final_cost_per_unit"),
        "average price per unit educational": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(20) > div.m-b-xs > div > div > button > i",
        ),
        "average price per unit": Selector(By.XPATH, "#average_price_per_unit"),
        "net price example": Selector(
            By.XPATH,
            '//*[@id="cost-and-pricing"]/section[1]/div/div[2]/div[9]/div[2]/div[1]/button'
            # "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(21) > div.learning > div.learning__buttons.m-b-xs > button"
        ),
        "net price educational": Selector(
            By.XPATH,
            '//*[@id="cost-and-pricing"]/section[1]/div/div[2]/div[9]/div[2]/div[1]/div/div/button'
            # "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[9]/div[2]/div[1]/div/div/button/i"
        ),
        "net price": Selector(
            By.XPATH, "//input[@id='net_price']", type=ElementType.INPUT
        ),
        "local taxes example": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(22) > div.learning > div.learning__buttons > button.button-example.button.button--small.button--tertiary.m-r-xxs.m-b-xs"
            # "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(22) > div.m-b-xs > button"
        ),
        "local taxes educational": Selector(
            By.XPATH,
            '//*[@id="cost-and-pricing"]/section[1]/div/div[2]/div[10]/div[2]/div[1]/div/div/button/i'
            # "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(22) > div.m-b-xs > div > div > button > i"
        ),
        "local taxes": Selector(
            By.CSS_SELECTOR, "#local_tax_charges", type=ElementType.INPUT
        ),
        "duty educational": Selector(
            By.CSS_SELECTOR,
            "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(23) > div.learning > div.learning__buttons > div > div > button > i"
            # "#cost-and-pricing > section.container > div > div.c-1-1.c-2-3-m.c-1-2-xl > div:nth-child(23) > div.m-b-xs > div > div > button > i"
        ),
        "duty": Selector(By.CSS_SELECTOR, "#duty_per_unit", type=ElementType.INPUT),
        "duty lesson": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[11]/div[2]/div[1]/button",
        ),
        # "select currency": Selector(
        #     By.CSS_SELECTOR, "#cost-and-pricing > section.bg-blue-deep-10.m-t-l.p-v-s > div > div > div.c-1-1.c-2-3-m.c-1-2-xl > div.bg-white.radius.p-xs.c-full.m-b-s.gross-price > div:nth-child(3) > div > div > div.c-1-6.m-r-xs > div > div > div.select__placeholder.text-blue-deep-60.bg-white.radius"
        # ),
        "gross price per unit": Selector(
            By.CSS_SELECTOR, "#gross_price_per_unit_invoicing", type=ElementType.INPUT
        ),
        "profit per unit": Selector(
            By.XPATH,
            "#cost-and-pricing > section.bg-blue-deep-10.m-t-l.p-v-s > div > div > div.c-1-1.c-2-3-m.c-1-2-xl > div.grid > div:nth-child(1) > div > h3",
        ),
        "potential total profit": Selector(
            By.XPATH,
            "#cost-and-pricing > section.bg-blue-deep-10.m-t-l.p-v-s > div > div > div.c-1-1.c-2-3-m.c-1-2-xl > div.grid > div:nth-child(2) > div > h3",
        ),
        "section complete": Selector(
            By.XPATH, "//body/main/div/div[2]/div[2]/div/div/div[2]/fieldset/div/div"
        ),
        "funding and credit": Selector(
            By.CSS_SELECTOR,
            "#costs-and-pricing-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > a > span",
        ),
        "export plan home": Selector(
            By.CSS_SELECTOR,
            "#costs-and-pricing-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > div.m-t-l > a",
        ),
        "Selling direct to your customer link": Selector(
            By.CSS_SELECTOR,
            "#marketing-approach-content > section.container.m-b-l > div > div.c-1-4.m-t-s > div > a > div > p",
        ),
        "manage exchange rates": Selector(
            By.XPATH, "//body/main/div[2]/div/section[2]/div/div/div[2]/div[1]/div[2]/a"
        ),
        "choose the right payment method": Selector(
            By.XPATH, "//h4[contains(text(),'Choose the right payment method')]"
        ),
        "decide when to get paid": Selector(
            By.XPATH, "//h4[contains(text(),'Decide when to get paid')]"
        ),
        "choose which incoterms are right for you": Selector(
            By.XPATH,
            "//h4[contains(text(),'Choose which incoterms are right for you')]",
        ),
        "lesson": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[2]/div/div/div[2]/div[1]/div[1]/button"
            # cost-and-pricing > section.bg-blue-deep-10.m-t-l.p-v-s > div > div > div.c-1-1.c-2-3-m.c-1-2-xl > button"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]",
        ),
        "nav funding and credit": Selector(
            By.CSS_SELECTOR, "#collapseNav > div > ul > li:nth-child(7)"
        ),
        "back": Selector(By.XPATH, "//body/div[10]/div/div/div/div[1]/a"),
        "add a product": Selector(
            By.XPATH, "//button[contains(text(),'Add a product')]"
        ),
        "add a target market": Selector(
            By.XPATH, "//button[contains(text(),'Add a target market')]"
        ),
        "top export plan home": Selector(
            By.XPATH,
            '//*[@id="costs-and-pricing-content"]/section[1]/div/div/div[2]/span/a'
            # "//*[@id=\"costs-and-pricing-content\"]/section[1]/div/div/div[2]/span/a/"
        ),
        "yes checkbox": Selector(By.CSS_SELECTOR, "#section-complete > div > label"),
        "search next button": Selector(
            By.XPATH,
            "//body/div[9]/div/div/form/div[2]/div/span/div/section/div/div/button",
        ),
        "dashboard": Selector(By.XPATH, "//a[contains(text(),'Dashboard')]"),
        "understand duties and taxes": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[11]/div[2]/div[2]/a",
        ),
        "local taxes understand duties and taxes": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[10]/div[2]/div[2]/a",
        ),
        "local taxes lesson": Selector(
            By.XPATH,
            "//body/main/div[2]/div/section[1]/div/div[2]/div[10]/div[2]/div[1]/button[2]",
        ),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


# def should_be_here(driver: WebDriver):
#     check_url(driver, URL, exact_match=False)


def should_be_here(driver: WebDriver):
    check_url_path_matches_template(URL, driver.current_url)


def enter_text(driver: WebDriver, element_name: str):
    text_element = find_element(driver, find_selector_by_name(SELECTORS, element_name))
    text_element.clear()
    text_element.send_keys("Automated tests")


def validate_entered_text(driver: WebDriver, element_name: str):
    text_element = find_element(driver, find_selector_by_name(SELECTORS, element_name))
    if "Automated tests" in text_element.text:
        return True
    return False


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()


def find_and_select_random_unit_list(driver: WebDriver, element_selector_name: str):
    driver.implicitly_wait(5)
    number_of_units_btn = driver.find_element_by_xpath(
        "//body/main/div[2]/div/section[1]/div/div[2]/div[5]/div/div[2]/div/div/div[2]"
    )
    # "//body/main/div[2]/div/section[1]/div/div[2]/div[5]/div/div[2]/div/div/div[2]/div[3]")
    number_of_units_btn.click()

    # select__list body-l bg-white radius
    number_of_units_element = driver.find_element_by_xpath(
        "//body/main/div[2]/div/section[1]/div/div[2]/div[5]/div/div[2]/div/div/div[2]/div[4]/ul"
    )
    nou_li_elements = number_of_units_element.find_elements_by_tag_name("li")
    random_number = 0
    if len(nou_li_elements) > 0:
        if len(nou_li_elements) > 2:
            random_number = random.randint(1, len(nou_li_elements) - 1)
        random_li_element = nou_li_elements[random_number]
        logging.debug("length of li elements " + str(len(nou_li_elements)))
        logging.debug("list elements")
        logging.debug(random_number)
        logging.debug(random_li_element.tag_name)
        logging.debug(random_li_element)
        time.sleep(2)
        random_li_element.click()
        time.sleep(2)


def find_and_select_random_currency_list(driver: WebDriver, element_selector_name: str):
    driver.implicitly_wait(5)
    select_currency_btn = driver.find_element_by_xpath(
        "//body/main/div[2]/div/section[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[2]"
    )
    # "//body/main/div[2]/div/section[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[2]")
    select_currency_btn.click()
    select_currency_element = driver.find_element_by_xpath(
        "//body/main/div[2]/div/section[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[2]/div[4]/ul"
    )
    # "//body/main/div[2]/div/section[2]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[2]/div[4]/ul")
    currency_li_elements = select_currency_element.find_elements_by_tag_name("li")

    random_number = 0
    if len(currency_li_elements) > 0:
        if len(currency_li_elements) > 2:
            random_number = random.randint(1, len(currency_li_elements) - 1)
        random_li_element = currency_li_elements[random_number]
        random_li_element.click()
        time.sleep(2)


#
def find_and_select_random_time_list(driver: WebDriver, element_selector_name: str):
    driver.implicitly_wait(5)
    time_frame_btn = driver.find_element_by_xpath(
        "//body/main/div[2]/div/section[1]/div/div[2]/div[6]/div/div[2]/div/div/div[2]"
    )
    time_frame_btn.click()
    # select__list body-l bg-white radius
    time_frame_element = driver.find_element_by_xpath(
        "//body/main/div[2]/div/section[1]/div/div[2]/div[6]/div/div[2]/div/div/div[2]/div[4]/ul"
    )
    time_li_elements = time_frame_element.find_elements_by_tag_name("li")
    random_number = 0
    if len(time_li_elements) > 0:
        if len(time_li_elements) > 2:
            random_number = random.randint(1, len(time_li_elements) - 1)
        random_li_element = time_li_elements[random_number]
        random_li_element.click()
        time.sleep(2)


def enter_direct_costs(
    driver: WebDriver, productcost: str, labourcost: str, additionalmargin: str
):
    base_element_xpath = "//body/main/div[2]/div/section[1]/div/div[2]/div[1]/div"
    productcost_ele_xpath = (
        base_element_xpath + "[" + "1" + "]/div/div[2]/div/div[2]/input"
    )
    labourcost_xpath = base_element_xpath + "[" + "2" + "]/div/div[2]/div/div[2]/input"
    additionalmargin_xpath = (
        base_element_xpath + "[" + "3" + "]/div/div[2]/div/div[2]/input"
    )

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
    summation_ele_xpath = (
        "//body/main/div[2]/div/section[1]/div/div[2]/div[2]/span[2]/span[2]"
    )
    summation_ele_value = driver.find_element_by_xpath(summation_ele_xpath).text
    if float(summation) == float(summation_ele_value):
        raise Exception("Direct Costs Summation do not match")


def enter_overhead_costs(
    driver: WebDriver,
    productadaptation: str,
    freightandlogistics: str,
    agentanddistributionfees: str,
    marketing: str,
    insurance: str,
):
    base_element_xpath = "//body/main/div[2]/div/section[1]/div/div[2]/div[3]/div"

    productadaptation_ele_xpath = (
        base_element_xpath + "[" + "1" + "]/div/div[2]/div/div[2]/input"
    )
    freightandlogistics_xpath = (
        base_element_xpath + "[" + "2" + "]/div/div[2]/div/div[2]/input"
    )
    agentanddistributionfees_xpath = (
        base_element_xpath + "[" + "3" + "]/div/div[2]/div/div[2]/input"
    )
    marketing_xpath = base_element_xpath + "[" + "4" + "]/div/div[2]/div/div[2]/input"
    insurance_xpath = base_element_xpath + "[" + "5" + "]/div/div[2]/div/div[2]/input"

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
    driver.find_element_by_xpath(productadaptation_ele_xpath).send_keys(
        productadaptation
    )
    time.sleep(2)
    driver.find_element_by_xpath(freightandlogistics_xpath).send_keys(
        freightandlogistics
    )
    time.sleep(2)
    driver.find_element_by_xpath(agentanddistributionfees_xpath).send_keys(
        agentanddistributionfees
    )
    time.sleep(2)
    driver.find_element_by_xpath(marketing_xpath).send_keys(marketing)
    time.sleep(2)
    driver.find_element_by_xpath(insurance_xpath).send_keys(insurance)

    time.sleep(2)

    # wait and then check the summation of all fields
    summation = (
        int(productadaptation)
        + int(freightandlogistics)
        + int(agentanddistributionfees)
        + int(marketing)
        + int(insurance)
    )
    summation_ele_xpath = (
        "//body/main/div[2]/div/section[1]/div/div[2]/div[4]/span[2]/span[2]"
    )
    summation_ele_value = driver.find_element_by_xpath(summation_ele_xpath).text
    if float(summation) == float(summation_ele_value):
        raise Exception("Overhead Costs Summation do not match")
    time.sleep(2)
    # //body/main/div[2]/div/section[1]/div/div[2]/div[4]/table/tbody/tr/td[2]/span[2]


def enter_value(driver: WebDriver, element_name: str):
    value_element = find_element(driver, find_selector_by_name(SELECTORS, element_name))
    value_element.clear()
    value_element.send_keys("12450")
    time.sleep(2)


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
        driver,
        find_selector_by_name(
            SELECTORS, "add a target market"
        ),  # dashboard add country button
    )
    country_btn.click()

    # try:
    #     if driver.find_element_by_xpath("//button[contains(text(),'Got it')]").is_displayed():
    #         driver.find_element_by_xpath("//button[contains(text(),'Got it')]").click()
    # except:
    #     pass

    if 0 == len(country):
        # if country name is not provided from the test case, then select one of the random 5 countries listed on the browser
        path_random_country_element = (
            "body > div:nth-child(13) > div > div > div > div > div > div.only-desktop > div.suggested-markets > ul > button:nth-child("
            + str(random.randint(1, 5))
            + ")"
        )
        driver.find_element_by_css_selector(path_random_country_element).click()
    else:
        # search using the provide country name from the test case
        driver.find_element_by_css_selector("#search-input").clear()
        driver.find_element_by_css_selector("#search-input").send_keys(country)

        # look out for the list displayed after entering country name and select random/provided country
        ul_list_element = driver.find_element_by_xpath(
            "//body/div[11]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/ul"
        )

        section_elements = ul_list_element.find_elements_by_tag_name("section")
        logging.debug("length of section elements " + str(len(section_elements)))
        # select random section element and within that select a country
        index_random_element_to_be_selected = random.randint(
            0, len(section_elements) - 1
        )
        logging.debug(
            "Index of section elements " + str(index_random_element_to_be_selected)
        )
        section_element_selected = section_elements[index_random_element_to_be_selected]
        logging.debug(section_element_selected)

        div_elements = section_element_selected.find_elements_by_tag_name(
            "div"
        )  # 2 has to be present
        logging.debug("length of div elements " + str(len(div_elements)))
        level_1_div_element = div_elements[
            1
        ]  # section_element_selected.find_element_by_class_name("p-t-s expand-section open")
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
    # search_again_top_bottom(driver)
    driver.implicitly_wait(1)
    driver.find_element_by_xpath(
        "//body/div[9]/div/div/form/div[2]/div/div/div[2]/label/div/input"
    ).clear()
    driver.find_element_by_xpath(
        "//body/div[9]/div/div/form/div[2]/div/div/div[2]/label/div/input"
    ).send_keys(product_name)
    driver.find_element_by_xpath(
        "//body/div[9]/div/div/form/div[2]/div/div/div[2]/button/i"
    ).click()

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
                "//body/div[9]/div/div/form/div[2]/div/span/div/section[1]/div[2]/button"
            )
            save_btn_found = True
        except Exception as ex:
            logging.debug("save button not found.Exception: " + str(ex))

        if save_btn_found == True:
            logging.debug("Save button found")
            save_product_btn.click()
            return
        # look for div's and radio buttons
        parent_1_div_element = driver.find_element_by_xpath(
            "//body/div[9]/div/div/form/div[2]/div/span/div/section[1]/div"
        )  # ("interaction grid m-v-xs")
        child_1_div_element = parent_1_div_element.find_element_by_tag_name(
            "div"
        )  # ("c-fullwidth")
        main_div_element = child_1_div_element.find_element_by_tag_name(
            "div"
        )  # "m-b-xs"
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
