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

NAME = "Business Risk"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_BUSINESS_RISK.absolute_template
PAGE_TITLE = "Business Risk Page"

SELECTORS = {
    "business risk": {
        "risk educational": Selector(
            By.XPATH, "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/button/i"
        ),
        "risk example": Selector(
            #        "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/button
            By.XPATH, "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/button/i"
        ),
        "risk": Selector(
            By.XPATH,
            "//*[@id=\"cost-and-pricing\"]/section[1]/div/div[2]/div[1]/table/tr[2]/td[1]/div/div[1]/button/i",
            type=ElementType.INPUT
        ),
        "risk likelihood educational": Selector(
            By.XPATH, "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/button/i"
        ),
        "risk impact educational": Selector(
            By.XPATH, "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[1]/div/div/button/i"
        ),
        "rare": Selector(
            By.XPATH, "//label[contains(text(),'Rare')]"
        ),
        "unlikely": Selector(
            By.XPATH, "//label[contains(text(),'Unlikely')]"
        ),
        "possible": Selector(
            By.XPATH, "//label[contains(text(),'Possible')]"
        ),
        "likely": Selector(
            By.XPATH, "//label[contains(text(),'Likely')]"
        ),
        "certain": Selector(
            By.XPATH, "//label[contains(text(),'Certain')]"
        ),
        "freight and logistics": Selector(
            By.XPATH, "//input[@id='freight_logistics']"
        ),
        "trivial": Selector(
            By.XPATH, "//label[contains(text(),'Trivial')]"
        ),
        "minor": Selector(
            By.XPATH, "//label[contains(text(),'Minor')]"
        ),
        "moderate": Selector(
            By.XPATH, "//label[contains(text(),'Moderate')]"
        ),
        "severe": Selector(
            By.XPATH, "//label[contains(text(),'Severe')]"
        ),
        "major": Selector(
            By.XPATH, "//label[contains(text(),'Major')]"
        ),
        "contingency plan educational": Selector(
            By.XPATH, "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div/div[4]/div[1]/div[1]/div/div/button/i"
        ),
        "contingency plan example": Selector(
            By.CSS_SELECTOR,
            "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div/div[4]/div[1]/div[1]/button"
            # "#business-risks > div.costs.costs--risks.bg-blue-deep-10.p-v-s.m-b-s > table > tbody > tr:nth-child(4) > td > div.learning > div.learning__buttons.m-b-xs > button"
        ),
        "add a risk": Selector(
            By.XPATH, "//body/main/div[2]/section[3]/div/div[2]/div/button"
        ),
        "export plan home": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='business-risk-content']/section[4]/div[1]/div[1]/div[2]/div[2]/a[1]"
        ),
        "top export plan home": Selector(
            By.CSS_SELECTOR,
            "#business-risk-content > section.section--intro.bg-blue-deep-90 > div > div > div.c-2-3-m.c-1-2-xl.p-t-xl.p-b-s.text-white > span > a > span"
            # "//*[@id=\"business-risk-content\"]/section[1]/div/div/div[2]/a/span"
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
        "add a target market": Selector(
            By.XPATH, "//button[contains(text(),'Add a target market')]"
        ),
        "nav download export plan": Selector(
            By.XPATH, "//body/main/div[1]/nav/div/div[2]/button[2]/i"
        ),
        "share": Selector(
            By.XPATH, "//body/main/div[1]/nav/div/div[2]/button[1]/i"
        ),
        # "download export plan": Selector(
        #     By.XPATH, "//body/main/div[1]/nav/div/div[2]/button[1]/i"
        # ),
        "yes checkbox": Selector(
            By.CSS_SELECTOR, "#section-complete > div > label"
        ),
        "add a product": Selector(
            By.XPATH, "//button[contains(text(),'Add a product')]"
        ),
        "search next button": Selector(
            By.XPATH, "//body/div[9]/div/div/form/div[2]/div/span/div/section/div/div/button"
        ),
        "dashboard": Selector(
            By.XPATH, "//a[contains(text(),'Dashboard')]"
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


def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()


def find_and_select_random_radio_and_click_next(driver: WebDriver):
    parent_div_radio_element = driver.find_element_by_class_name("m-b-xs")
    time.sleep(2)
    child_radio_div_elements = parent_div_radio_element.find_elements_by_xpath("//input[@type='radio']");
    RADIO_SELECTORS_DICT = {}
    for index in range(len(child_radio_div_elements)):
        child_radio_element = child_radio_div_elements[index]
        key_name = "radio" + str(index)
        radio_element_xpath = f"//input[@id='" + str(child_radio_element.get_attribute("id")) + "']"
        key_value = Selector(By.XPATH, radio_element_xpath, type=ElementType.RADIO)

        if index == 0:
            rsdict = {}
            rsdict[key_name] = key_value
            RADIO_SELECTORS_DICT["product radio info"] = rsdict
        else:
            rsdict = RADIO_SELECTORS_DICT["product radio info"]
            rsdict[key_name] = key_value
            RADIO_SELECTORS_DICT.clear()
            RADIO_SELECTORS_DICT["product radio info"] = rsdict

    radio_selectors = RADIO_SELECTORS_DICT["product radio info"]
    check_random_radio(driver, radio_selectors)

    nextbtnclick(driver)


def nextbtnclick(driver: WebDriver):
    driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

def enter_risk_details(driver: WebDriver, position: str, risktext: str, contingencyplan: str):
    # every call of this function, click on Add Goal
    find_and_click(driver, element_selector_name="Add a risk")
    time.sleep(1)

    position = int(position)
    risktext_position = int((int(position) * 5) - 4)
    risk_div_element_xpath = "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div" + "[" + str(
        risktext_position) + "]"
    risk_text_ele_xpath = risk_div_element_xpath + "/div[1]/div[2]/textarea"
    driver.find_element_by_xpath(risk_text_ele_xpath).send_keys(risktext)
    logging.debug(risk_text_ele_xpath)
    logging.debug(risktext)
    time.sleep(1)

    path_random_risk_likelihood = "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/table/tbody/tr" \
                                  + "[" + str(risktext_position + 1) + "]" + "/td/div[2]/div" \
                                  + "[" + str(random.randint(1, 5)) + "]"
    path_random_risk_likelihood_button_ele_xpath = path_random_risk_likelihood + "/label"
    driver.find_element_by_xpath(path_random_risk_likelihood_button_ele_xpath).click()
    time.sleep(1)
    risk_impact_button_element_xpath = "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/table/tbody/tr" \
                                       + "[" + str(risktext_position + 2) + "]" \
                                       + "/td/div[2]/div" + "[" + str(random.randint(1, 5)) + "]" + "/label"
    driver.find_element_by_xpath(risk_impact_button_element_xpath).click()

    contingencyplan_div_element_xpath = "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div" \
                                        + "[" + str(risktext_position + 3) + "]"
    contingencyplan_text_element_xpath = contingencyplan_div_element_xpath + "/div[4]/div[2]/textarea"
    driver.find_element_by_xpath(contingencyplan_text_element_xpath).send_keys(contingencyplan)

    time.sleep(5)


def delete_all_risk_details(driver: WebDriver, del_button_position: str):
    # 1,3,5,7,......
    # /html/body/main/div[2]/section[3]/div/div[2]/div/div[2]/table/tbody/tr[5]/td/button/i
    # del_button_position: 5,10,15,20,25
    driver.implicitly_wait(5)
    time.sleep(5)
    del_button_index = int(del_button_position) * 5
    risk_detail_div_element_xpath = "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/table/tbody/tr" + "[" + str(
        del_button_index) + "]"
    risk_btn_ele_xpath = risk_detail_div_element_xpath + "/td/button/i"
    driver.find_element_by_xpath(risk_btn_ele_xpath).click()
    # logging.debug("del_button_position " + str(del_button_position))
    time.sleep(5)
    driver.implicitly_wait(5)

    # 12,13,14,15.......
    # 12 + (1 - 1), 12 + (2 - 1), 12 + (3 - 1), 12 + (4 - 1),.........
    # //body/div[12]/div/div/div/div[2]/div[2]/button[1]/span
    delete_msg_yes_index = int(12 + (int(del_button_position) - 1))
    delete_message_yes_element_xpath = "//body/div" + "[" + str(
        delete_msg_yes_index) + "]" + "/div/div/div/div[2]/div[2]/button[1]/span"
    logging.debug(delete_message_yes_element_xpath)
    delete_message_yes_element = driver.find_element_by_xpath(delete_message_yes_element_xpath)
    delete_message_yes_element.click()
    time.sleep(1)
