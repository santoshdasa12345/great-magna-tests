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

NAME = "Travel Plan"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_TRAVEL_PLAN.absolute
PAGE_TITLE = "Travel Plan Page"

SELECTORS = {
    "travel plan": {
        "back": Selector(
            By.XPATH, "//body/div[7]/div/div/div/div[1]/a"
        ),
        "travel information": Selector(
            By.XPATH, "//textarea[@id='travel_information']", type=ElementType.INPUT
        ),
        "travel information educational": Selector(
            By.XPATH, "//*[@id=\"culture-and-rules\"]/div[1]/div/button/i"
        ),
        "cultural information": Selector(
            By.XPATH, "//textarea[@id='cultural_information']", type=ElementType.INPUT
        ),
        "languages educational": Selector(
            By.XPATH, "//*[@id=\"stats-for-target-market\"]/div[1]/div/div/div/div/div/div/button/i" #//*[@id=\"stats-for-target-market\"]/div[1]/div/div/div/div/div/button/i"
        ),
        "open datasnapshot": Selector(
            By.XPATH, "//*[@id=\"stats-for-target-market\"]/div/button"
        ),
        "i dont need visa": Selector(
            By.XPATH, "//body/main/div[2]/section[5]/div/div[2]/div[2]/div/div[1]/div[1]/label" #//*[@id=\"need-visa-false\"]"#//body/main/div[2]/section[5]/div/div[2]/div[2]/div/div[1]/label"
        ),
        "i need a visa": Selector(
            By.XPATH, "//body/main/div[2]/section[5]/div/div[2]/div[2]/div/div[1]/div[2]/label"
        ),
        "planned travel educational": Selector(
            By.XPATH, "//*[@id=\"planned-travel\"]/div/div[1]/div/div/button/i",
            type=ElementType.INPUT
        ),
        "add a trip": Selector(
            By.XPATH, "//body/main/div[2]/section[6]/div/div[2]/div/button"
        ),
        "delete message": Selector(
            By.XPATH, "//body/div[12]/div/div/div/div[2]/div[2]/button[1]/i"
        ),
        "how and where": Selector(
            By.CSS_SELECTOR, "#how_where_visa"
        ),
        "how long": Selector(
            By.CSS_SELECTOR, "#how_long"
        ),
        "notes": Selector(
            By.CSS_SELECTOR, "#notes"
        ),
        "yes checkbox": Selector(
            By.CSS_SELECTOR, "#section-complete > div"#//input[@id='checkbox_complete']"
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
            By.XPATH, "//*[@id=\"collapseNav\"]/div/button/i"
        ),
        "nav business risk": Selector(
            By.XPATH, "//*[@id=\"collapseNav\"]/div/ul/li[10]/a"
        ),
        "add a target market": Selector(
            By.XPATH, "//button[contains(text(),'Add a target market')]"
        ),
        "top export plan home": Selector(
            By.XPATH, "//*[@id=\"travel-plan-content\"]/section[1]/div/div/div[2]/span/a"#//*[@id=\"travel-plan-content\"]/section[1]/div/div/div[2]/a/span"
        ),
        "add a product": Selector(
            By.XPATH, "//button[contains(text(),'Add a product')]"
        ),
        "search": Selector(
            By.XPATH, "#search-input"
        ),
        "next": Selector(
            By.XPATH,
            "body > div:nth-child(17) > div > div > form > div.scroll-area > div > div > div.flex-centre.m-t-xs.search-input > button > i"
        ),
        "search next button": Selector(
            By.XPATH, "//body/div[9]/div/div/form/div[2]/div/span/div/section/div/div/button"
        ),
        "dashboard": Selector(
            By.XPATH, "//a[contains(text(),'Dashboard')]"
        ),
        "export plan home": Selector(
            By.CSS_SELECTOR,
            "#travel-plan-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > div.m-t-l > a"
        ),
        "business risk": Selector(
            By.CSS_SELECTOR, "#travel-plan-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > a > span"
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


def enter_trip_details(driver: WebDriver, position: str, trip_name: str):
    # every call of this function, click on Add Goal
    find_and_click(driver, element_selector_name="Add a trip")
    time.sleep(2)
    document_div_element_xpath = "//body/main/div[2]/section[6]/div/div[2]/div/div[2]/div" + "[" + position + "]"
    document_text_ele_xpath = document_div_element_xpath + "/div[1]/div/textarea"
    driver.find_element_by_xpath(document_text_ele_xpath).send_keys(trip_name)
    time.sleep(2)
    #//body/main/div[2]/section[6]/div/div[2]/div/div[2]/table/tbody/tr[1]/td/div/textarea
    #//body/main/div[2]/section[6]/div/div[2]/div/div[2]/div/div[1]/div/textarea
    #//body/main/div[2]/section[6]/div/div[2]/div/div[2]/div[2]/div[1]/div/textarea

def delete_all_trip_details(driver: WebDriver, del_button_position: str):
    driver.implicitly_wait(4)
    # 1,3,5,7,......
    #//body/main/div[2]/section[6]/div/div[2]/div/div[2]/div[5]/div[2]/button
    trip_text_area_element_index = int(del_button_position)
    trip_text_area_element_x_path = "//body/main/div[2]/section[6]/div/div[2]/div/div[2]/div" \
                                    + "[" + str(trip_text_area_element_index) + "]" + "/div[2]/button"
    trip_text_area_text_exists = True
    try:
        trip_text_area_text = driver.find_element_by_xpath(trip_text_area_element_x_path).text
        if trip_text_area_text == None or len(trip_text_area_text) <= 0:
            trip_text_area_text_exists = False
    except:
        trip_text_area_text_exists = False

    # del_button_position: 2,4,6,8,10,..... 1,2,3,4,5
    document_div_element_xpath = "//body/main/div[2]/section[6]/div/div[2]/div/div[2]/div" + "[" + del_button_position + "]"
    del_btn_ele_xpath = document_div_element_xpath + "/div[2]/button/i"
    print(del_btn_ele_xpath)
    driver.find_element_by_xpath(del_btn_ele_xpath).click()

    if trip_text_area_text_exists == True:
        driver.implicitly_wait(1)
        #15,14,13,12,11
        #
        #//body/div[11]/div/div/div/div[2]/div[2]/button[1]
        #//body/div[12]/div/div/div/div[2]/div[2]/button[1]/i
        # 12,13,14,15.......
        # 12 + (2/2 - 1), 12 + (4/2 - 1), 12 + (6/2 - 1), 12 + (8/2 - 1),.........
        delete_msg_yes_index = int(11 + (int((int(del_button_position))) - 1))
        delete_message_yes_element_xpath = "//body/div" + "[" + str(
            delete_msg_yes_index) + "]" + "/div/div/div/div[2]/div[2]/button[1]/i"
        delete_message_yes_element = driver.find_element_by_xpath(delete_message_yes_element_xpath)
        delete_message_yes_element.click()
        time.sleep(1)


def select_radio_button(driver: WebDriver, element_name: str):
    # i dont need visa
    driver.implicitly_wait(5)
    #                             //body[1]/main[1]/div[2]/section[5]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]
    driver.find_element_by_xpath("//body[1]/main[1]/div[2]/section[5]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/input[1]")#//body/main/div[2]/section[5]/div/div[2]/div[2]/div/h2")
    lower_case_element_name = element_name.lower()
    find_and_click(driver, element_selector_name=element_name)
    # logging.debug(SELECTORS["travel plan"][lower_case_element_name])
    # logging.debug(SELECTORS["travel plan"][lower_case_element_name].value)
    radio_element_x_path = SELECTORS["travel plan"][lower_case_element_name].value
    radio_i_dont_need_visa_elem = driver.find_element_by_xpath(radio_element_x_path)
    radio_i_dont_need_visa_elem.click()

# def select_radio_button(driver: WebDriver, element_name: str):
#     # i dont need visa
#     driver.implicitly_wait(5)
#     div_radio_button_element = driver.find_element_by_class_name("multiple-choice large")#//body/main/div[2]/section[5]/div/div[2]/div[2]/div/h2")
#     for multiple_choice_elements in div_radio_button_element
#         if
#             need_visa_false == False
#             need_visa_false.click()
#         else
#             need_visa_true == True
#
#
#         input_element = id_element.find_element_by_tag_name("input")
#         input_element.click()
#     div_1_element = find_elements_by_class_name("multiple-choice large")
#     for multiple_choice_element in multiple_choice_elements
#     lower_case_element_name = element_name.lower()
#     # find_and_click(driver, element_selector_name=element_name)
#     # logging.debug(SELECTORS["travel plan"][lower_case_element_name])
#     # logging.debug(SELECTORS["travel plan"][lower_case_element_name].value)
#     radio_element_x_path = SELECTORS["travel plan"][lower_case_element_name].value
#     radio_i_dont_need_visa_elem = driver.find_element_by_xpath(radio_element_x_path)
#     radio_i_dont_need_visa_elem.click()


def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()


# def fill_out_products_and_country(driver: WebDriver, products: str, country: str):
#     fill_out_product(driver, products)
#
#     fill_out_country(driver, country)

def find_and_click_change_link(driver: WebDriver, element_selector_name: str):
    change_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    change_link.click()


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
