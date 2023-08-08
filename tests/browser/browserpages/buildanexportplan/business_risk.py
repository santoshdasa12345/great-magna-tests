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

NAME = "Business Risk"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_BUSINESS_RISK.absolute_template
PAGE_TITLE = "Business Risk Page"

SELECTORS = {
    "business risk": {
        "risk educational": Selector(
            By.XPATH,
            '//*[@id="business-risks"]/div[2]/table/tbody/tr[1]/td/div[1]/div[1]/div/div/button/i',
        ),
        "risk example": Selector(
            By.XPATH,
            "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/button",
        ),
        "risk": Selector(
            By.XPATH,
            '//*[@id="cost-and-pricing"]/section[1]/div/div[2]/div[1]/table/tr[2]/td[1]/div/div[1]/button/i',
            type=ElementType.INPUT,
        ),
        "risk likelihood educational": Selector(
            By.XPATH,
            '//*[@id="business-risks"]/div[2]/table/tbody/tr[2]/td/div[1]/div[1]/div/div/button/i',
        ),
        "risk impact educational": Selector(
            By.XPATH,
            '//*[@id="business-risks"]/div[2]/table/tbody/tr[3]/td/div[1]/div[1]/div/div[1]/button/i',
        ),
        "rare": Selector(By.XPATH, "//label[contains(text(),'Rare')]"),
        "unlikely": Selector(By.XPATH, "//label[contains(text(),'Unlikely')]"),
        "possible": Selector(By.XPATH, "//label[contains(text(),'Possible')]"),
        "likely": Selector(By.XPATH, "//label[contains(text(),'Likely')]"),
        "certain": Selector(By.XPATH, "//label[contains(text(),'Certain')]"),
        "freight and logistics": Selector(By.XPATH, "//input[@id='freight_logistics']"),
        "trivial": Selector(By.XPATH, "//label[contains(text(),'Trivial')]"),
        "minor": Selector(By.XPATH, "//label[contains(text(),'Minor')]"),
        "moderate": Selector(By.XPATH, "//label[contains(text(),'Moderate')]"),
        "severe": Selector(By.XPATH, "//label[contains(text(),'Severe')]"),
        "major": Selector(By.XPATH, "//label[contains(text(),'Major')]"),
        "contingency plan educational": Selector(
            By.XPATH,
            '//*[@id="business-risks"]/div[2]/table/tbody/tr[4]/td/div[1]/div[1]/div/div/button/i',
        ),
        "contingency plan example": Selector(
            By.CSS_SELECTOR,
            '//*[@id="business-risks"]/div[2]/table/tbody/tr[4]/td/div[1]/div[1]/button'
            # "#business-risks > div.costs.costs--risks.bg-blue-deep-10.p-v-s.m-b-s > table > tbody > tr:nth-child(4) > td > div.learning > div.learning__buttons.m-b-xs > button"
        ),
        "add a risk": Selector(
            By.XPATH, "//body/main/div[2]/section[3]/div/div[2]/div/button"
        ),
        "export plan home": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='business-risk-content']/section[4]/div[1]/div[1]/div[2]/div[2]/a[1]",
        ),
        "top export plan home": Selector(
            By.CSS_SELECTOR,
            "#business-risk-content > section.section--intro.bg-blue-deep-90 > div > div > div.c-2-3-m.c-1-2-xl.p-t-xl.p-b-s.text-white > span > a > span"
            # "//*[@id=\"business-risk-content\"]/section[1]/div/div/div[2]/a/span"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]",
        ),
        "nav Adapting Your Product": Selector(
            By.XPATH, "//a[contains(text(),'Adapting Your Product')]"
        ),
        "back": Selector(By.XPATH, "//body/div[10]/div/div/div/div[1]/a"),
        "add a target market": Selector(
            By.XPATH, "//button[contains(text(),'Add a target market')]"
        ),
        "nav download export plan": Selector(
            By.XPATH, "//body/main/div[1]/nav/div/div[2]/button[2]/i"
        ),
        "share": Selector(By.XPATH, "//body/main/div[1]/nav/div/div[2]/button[1]/i"),
        # "download export plan": Selector(
        #     By.XPATH, "//body/main/div[1]/nav/div/div[2]/button[1]/i"
        # ),
        "yes checkbox": Selector(By.CSS_SELECTOR, "#section-complete > div > label"),
        "add a product": Selector(
            By.XPATH, "//button[contains(text(),'Add a product')]"
        ),
        "search next button": Selector(
            By.XPATH,
            "//body/div[9]/div/div/form/div[2]/div/span/div/section/div/div/button",
        ),
        "dashboard": Selector(By.XPATH, "//a[contains(text(),'Dashboard')]"),
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


def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()


def find_and_select_random_radio_and_click_next(driver: WebDriver):
    parent_div_radio_element = driver.find_element_by_class_name("m-b-xs")
    time.sleep(2)
    child_radio_div_elements = parent_div_radio_element.find_elements_by_xpath(
        "//input[@type='radio']"
    )
    RADIO_SELECTORS_DICT = {}
    for index in range(len(child_radio_div_elements)):
        child_radio_element = child_radio_div_elements[index]
        key_name = "radio" + str(index)
        radio_element_xpath = (
            f"//input[@id='" + str(child_radio_element.get_attribute("id")) + "']"
        )
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


def fill_out_country(driver: WebDriver, country: str):
    driver.implicitly_wait(1)

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


def enter_risk_details(
    driver: WebDriver, position: str, risktext: str, contingencyplan: str
):
    # every call of this function, click on Add Goal
    find_and_click(driver, element_selector_name="Add a risk")
    time.sleep(1)

    position = int(position)
    risktext_position = int((int(position) * 5) - 4)
    risk_div_element_xpath = (
        "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div"
        + "["
        + str(risktext_position)
        + "]"
    )
    risk_text_ele_xpath = risk_div_element_xpath + "/div[1]/div[2]/textarea"
    driver.find_element_by_xpath(risk_text_ele_xpath).send_keys(risktext)
    logging.debug(risk_text_ele_xpath)
    logging.debug(risktext)
    time.sleep(1)

    path_random_risk_likelihood = (
        "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/table/tbody/tr"
        + "["
        + str(risktext_position + 1)
        + "]"
        + "/td/div[2]/div"
        + "["
        + str(random.randint(1, 5))
        + "]"
    )
    path_random_risk_likelihood_button_ele_xpath = (
        path_random_risk_likelihood + "/label"
    )
    driver.find_element_by_xpath(path_random_risk_likelihood_button_ele_xpath).click()
    time.sleep(1)
    risk_impact_button_element_xpath = (
        "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/table/tbody/tr"
        + "["
        + str(risktext_position + 2)
        + "]"
        + "/td/div[2]/div"
        + "["
        + str(random.randint(1, 5))
        + "]"
        + "/label"
    )
    driver.find_element_by_xpath(risk_impact_button_element_xpath).click()

    contingencyplan_div_element_xpath = (
        "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/div"
        + "["
        + str(risktext_position + 3)
        + "]"
    )
    contingencyplan_text_element_xpath = (
        contingencyplan_div_element_xpath + "/div[4]/div[2]/textarea"
    )
    driver.find_element_by_xpath(contingencyplan_text_element_xpath).send_keys(
        contingencyplan
    )

    time.sleep(5)


def delete_all_risk_details(driver: WebDriver, del_button_position: str):
    # 1,3,5,7,......
    # /html/body/main/div[2]/section[3]/div/div[2]/div/div[2]/table/tbody/tr[5]/td/button/i
    # del_button_position: 5,10,15,20,25
    driver.implicitly_wait(5)
    time.sleep(5)
    del_button_index = int(del_button_position) * 5
    risk_detail_div_element_xpath = (
        "//body/main/div[2]/section[3]/div/div[2]/div/div[2]/table/tbody/tr"
        + "["
        + str(del_button_index)
        + "]"
    )
    risk_btn_ele_xpath = risk_detail_div_element_xpath + "/td/button/i"
    driver.find_element_by_xpath(risk_btn_ele_xpath).click()
    # logging.debug("del_button_position " + str(del_button_position))
    time.sleep(5)
    driver.implicitly_wait(5)

    # 12,13,14,15.......
    # 12 + (1 - 1), 12 + (2 - 1), 12 + (3 - 1), 12 + (4 - 1),.........
    # //body/div[12]/div/div/div/div[2]/div[2]/button[1]/span
    delete_msg_yes_index = int(12 + (int(del_button_position) - 1))
    delete_message_yes_element_xpath = (
        "//body/div"
        + "["
        + str(delete_msg_yes_index)
        + "]"
        + "/div/div/div/div[2]/div[2]/button[1]/span"
    )
    logging.debug(delete_message_yes_element_xpath)
    delete_message_yes_element = driver.find_element_by_xpath(
        delete_message_yes_element_xpath
    )
    delete_message_yes_element.click()
    time.sleep(1)
