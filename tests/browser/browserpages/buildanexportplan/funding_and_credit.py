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
        "lesson": Selector(
            By.CSS_SELECTOR, "#finance-how-much-funding > div > div.learning > div.learning__buttons > button"
            #"#finance-funding-credit-options > button"
        ),
        "add a funding option": Selector(
            By.XPATH, "//body/main/div[2]/div/div/div[2]/div/div[3]/div[1]/table/tfoot/tr/td/button"
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
            By.CSS_SELECTOR, "#finance-how-much-funding > div > div.learning > div.learning__content > a > div"
        ),
        "choose the right funding": Selector(
            By.XPATH, "//*[@id=\"finance-funding-credit-options\"]/a/div/h4"
        ),
        "top export plan home": Selector(
            By.XPATH, "//*[@id=\"funding-and-credit-content\"]/section[1]/div/div/div[2]/span/a"
        ),
        "yes checkbox": Selector(
            By.CSS_SELECTOR, "#section-complete > div > label"
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
def delete_all_funding_options(driver: WebDriver, del_button_position: str):
    # 1,3,5,7,......
    time.sleep(1)

    funding_options_div_element_xpath = "//body/main/div[2]/div/div/div[2]/div/div[3]/div[1]/table/tbody/tr" + "[" + del_button_position + "]"
    del_btn_ele_xpath = funding_options_div_element_xpath + "/td/button"
    driver.find_element_by_xpath(del_btn_ele_xpath).click()

    driver.implicitly_wait(2)
    delete_msg_yes_index = int(12 + (int((int(del_button_position) / 2)) - 1))
    time.sleep(1)
    delete_message_yes_element_xpath = "//body/div" + "[" + str(
        delete_msg_yes_index) + "]" + "/div/div/div/div[2]/div[2]/button[1]"
    logging.debug(delete_message_yes_element_xpath)
    delete_message_yes_element = driver.find_element_by_xpath(delete_message_yes_element_xpath)
    delete_message_yes_element.click()

# def delete_all_funding_options(driver: WebDriver, position: str):
#     actual_position = int(position) * 2
#     objective_div_element_xpath = "/html/body/main/div[2]/div/div/div[2]/div/div[3]/div[1]/table/tbody/tr" + "[" + str(
#         actual_position) + "]"
#     del_btn_ele_xpath = objective_div_element_xpath + "/td/button"
#
#     driver.find_element_by_xpath(del_btn_ele_xpath).click()
#     time.sleep(1)

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
    # search_again_top_bottom(driver)
    driver.implicitly_wait(1)
    driver.find_element_by_xpath("//body/div[9]/div/div/form/div[2]/div/div/div[2]/label/div/input").clear()
    driver.find_element_by_xpath("//body/div[9]/div/div/form/div[2]/div/div/div[2]/label/div/input").send_keys(
        product_name)
    driver.find_element_by_xpath("//body/div[9]/div/div/form/div[2]/div/div/div[2]/button/i").click()

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
