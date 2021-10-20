import logging
import random
import time
from types import ModuleType
from typing import List, Union
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.actions import action_builder

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

NAME = "Dashboard"
SERVICE = Service.GREATMAGNA
TYPE = PageType.DASHBOARD
URL = URLs.GREAT_MAGNA_DASHBOARD.absolute
PAGE_TITLE = "Dashboard Page "

SELECTORS = {
    "dashboard": {
        "learn to export": Selector(
            By.XPATH, "//a[@id='header-link-learning']"  # "//a[@id='header-link-learning']"
        ),
        "where to export": Selector(
            By.CSS_SELECTOR, "#header-link-markets"  # //a[@id='header-link-markets']"
        ),
        "build an export plan": Selector(
            By.XPATH, "//a[@id='header-link-exporting-plan']"  # "//a[@id='header-link-exporting-plan']"
        ),
        "sign out": Selector(
            By.XPATH, "//span[contains(text(),'Sign out')]"
        ),
        "skipwalkthrough": Selector(
            By.XPATH, "//*[@id=\"page-tour-skip\"]"
        ),
        "menu": Selector(
            By.CSS_SELECTOR, "#header-link-user-profile > div > button", time.sleep(2)
        ),
        "product-btn": Selector(
            By.CSS_SELECTOR, "#set-product-button > span > button"
        ),
        "country-btn": Selector(
            By.CSS_SELECTOR, "#set-country-button > span > button"
        ),
        "i have exported in last 12 months": Selector(
            By.XPATH, "//label[contains(text(),'I have exported in the last 12 months')]"
        ),
        "i have exported before but not in the last 12 months": Selector(
            By.XPATH, "//label[contains(text(),'I have exported before but not in the last 12 mont')]"
        ),
        "i have never exported but have a product or service": Selector(
            By.XPATH, "//label[contains(text(),'I have never exported but have a product or servic')]"
        ),
        "i do not have a product or service for export": Selector(
            By.XPATH, "//label[contains(text(),'I do not have a product or service for export')]"
        ),
        "save": Selector(
            By.XPATH, "//button[contains(text(),'Save')]"
        ),
        "go to export plan": Selector(
            By.XPATH, "//a[contains(text(),'Go to export plan')]"
        ),
        "start": Selector(
            By.XPATH, "//a[contains(text(),'Start')]"
        ),
        "export plan progress bar": Selector(
            By.XPATH, "//body/main[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]"
        ),
        "top search again": Selector(
            By.XPATH, "//body/div[4]/div/div/form/div[2]/div/div/section/button"
        ),
        "bottom search again": Selector(
            By.XPATH, "//body/div[4]/div/div/form/div[2]/div/div/section/button"
        ),
        "search next button": Selector(
            By.XPATH, "//body/div[4]/div/div/form/div[2]/div/span/div/section[1]/div/fieldset/button"#//body/div[4]/div/div/form/div[2]/div/span/div/section[1]/div/div/button"
        ),
        "save product": Selector(
            By.XPATH, "//body/div[4]/div/div/form/div[2]/div/span/div/section[1]/button"#//body/div[4]/div/div/form/div[2]/div/span/div/section[1]/div[2]/button"
        ),
        "home": Selector(
            By.XPATH, "//span[contains(text(),'Home')]"
        ),
        "menu learn to export": Selector(
            By.XPATH, "//span[contains(text(),'Learn to export')]"
        ),
        "menu where to export": Selector(
            By.XPATH, "//span[contains(text(),'Where to export')]"
        ),
        "menu make an export plan": Selector(
            By.XPATH, "//span[contains(text(),'Make an export plan')]"
        ),
        "menu advice": Selector(
            By.XPATH, "//span[contains(text(),'Advice')]"
        ),
        "menu markets": Selector(
            By.XPATH, "//span[contains(text(),'Markets')]"
        ),
        "dashboard": Selector(
            By.XPATH, "//a[contains(text(),'Dashboard')]"
        ),
        "contact us": Selector(
            By.CSS_SELECTOR, "#footer > nav > ul > li:nth-child(1) > a", type=ElementType.LINK
        ),
        "learn to export button": Selector(
            By.XPATH, "//a[contains(text(),'Learn to Export')]"
        ),
        "where to export button": Selector(
            By.XPATH, "//a[contains(text(),'Compare places')]"
        ),
        "go to export plan button": Selector(
            By.XPATH, "//a[contains(text(),'Go to export plan')]"
        ),
        "continue": Selector(
            By.XPATH, "//a[contains(text(),'Continue')]"
        ),
        "coming soon": Selector(
            By.XPATH, "//button[contains(text(),'Coming soon')]"
        ),
        "privacy and cookies": Selector(
            By.XPATH, "//a[contains(text(),'Privacy and cookies')]", type=ElementType.LINK
        ),
        "terms and conditions": Selector(
            By.XPATH, "//a[contains(text(),'Terms and conditions')]", type=ElementType.LINK
        ),
        "accessibility": Selector(
            By.XPATH, "//a[contains(text(),'Accessibility')]", type=ElementType.LINK
        ),
        "performance": Selector(
            By.XPATH, "//a[contains(text(),'Performance')]", type=ElementType.LINK
        ),
        "dit": Selector(
            By.XPATH, "//a[contains(text(),'Department for International Trade on GOV.UK')]", type=ElementType.LINK
        ),
        "footer logo": Selector(
            By.CSS_SELECTOR, "#footer > nav > div > a > img"
        ),
        "header logo": Selector(
            By.XPATH, "//img[@id='header-logo-exporting-is-great']"
        ),
        "my products": Selector(
            By.CSS_SELECTOR, "#set-product-button > span:nth-child(1) > button > span"
        ),
        "add product": Selector(
            By.CSS_SELECTOR, "#set-product-button > span:nth-child(1) > div > button > i"
        ),
        "my markets": Selector(
            By.CSS_SELECTOR, "#set-country-button > span > span:nth-child(1) > button > span"
        ),
        "add market": Selector(
            By.CSS_SELECTOR, "#set-country-button > span > span:nth-child(1) > div > button"
        ),
        "vfm close": Selector(
            By.XPATH, "//body/div[7]/div/div/button"
        ),
        "not now": Selector(
            By.XPATH, "//body/div[7]/div/div/div/div[2]/button[1]"
        ),
        "vfm continue": Selector(
            By.XPATH, "//body/div[7]/div/div/div/div[2]/button[2]"
        ),

    },
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def find_and_click_change_link(driver: WebDriver, element_selector_name: str):
    change_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    change_link.click()


def should_see_following_sections(driver: WebDriver, names: List[str]):
    # desc = ["dashboard"]
    # check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)
    #
    section = SELECTORS["dashboard"]
    names = [each_string.lower() for each_string in names]
    for key, selector in section.items():
        logging.debug(key)
        if key in names:
            element = find_element(
                driver,
                selector,
                element_name=key,
            )
            check_if_element_is_visible(element, element_name=key)


def click_skip_walk_through(driver: WebDriver):
    skip_link = find_element(
        driver, find_selector_by_name(SELECTORS, "skipwalkthrough")
    )
    skip_link.click()


def click_signout(driver: WebDriver):
    signout_link = find_element(
        driver, find_selector_by_name(SELECTORS, "sign out")
    )
    signout_link.click()


def click_avatar(driver: WebDriver):
    avatar_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "avatar")
    )
    avatar_btn.click()


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


def fill_out_product(driver: WebDriver, products: str):
    product_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "product-btn")
    )
    product_btn.click()

    try:
        if driver.find_element_by_css_selector("body > div:nth-child(11) > div > div > button").is_displayed():
            driver.find_element_by_css_selector("body > div:nth-child(11) > div > div > button").click()
    except:
        pass

    try:

        product_input_text = driver.find_element_by_xpath("//input[@id='input-commodity-name']").text
        logging.debug("product_input_text -> " + product_input_text)

        for i in range(len(product_input_text)):
            driver.find_element_by_xpath(
                "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").sendKeys(
                Keys.BACKSPACE)
        driver.find_element_by_xpath(
            "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("")
        driver.find_element_by_xpath(
            "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys(products)
        driver.find_element_by_xpath(
            "//body/div[3]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/button[1]/i[1]").click()

        while True:
            find_and_select_random_radio_and_click_next(driver)
            time.sleep(1)  # seconds
            try:
                if driver.find_element_by_xpath("//button[contains(text(),'Save product')]").is_displayed():
                    driver.find_element_by_xpath("//button[contains(text(),'Save product')]").click()
                    break
                else:
                    continue
            except:
                pass
    except Exception as ex:
        logging.debug("Exception in product input " + str(ex))
        driver.find_element_by_css_selector("#input-commodity-name").send_keys(products)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/form/div[2]/div/div/section/div/button").click()


def fill_out_country(driver: WebDriver, country: str):
    driver.implicitly_wait(1)
    # parent div: //body/div[5]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]
    # parent ul: //body/div[5]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/ul

    # where to export : country search
    # //body/div[8]/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]
    # //body/div[8]/div/div/div/div/div/div[1]/div[3]/div[2]/div[2]/ul

    # country
    country_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "country-btn")  # dashboard add country button
    )
    country_btn.click()

    try:
        if driver.find_element_by_xpath("//button[contains(text(),'Got it')]").is_displayed():
            driver.find_element_by_xpath("//button[contains(text(),'Got it')]").click()
    except:
        pass

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
            "//body/div[5]/div/div/div/div/div/div[1]/div[4]/div[2]/div[2]/ul")

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
                break
        if country_name_found == False:
            raise Exception("Country name could not be found " + str(country))


def fill_out_products_and_country(driver: WebDriver, products: str, country: str):
    fill_out_product(driver, products)

    fill_out_country(driver, country)


def fill_out_products(driver: WebDriver, products: str):
    # details_dict = {"emailaddress": products}
    # product_selectors = SELECTORS["dashboard"]
    # fill_out_input_fields(driver, product_selectors, details_dict)
    product_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "product-btn")
    )
    product_btn.click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath("//body/div[4]/div/div/form/div[2]/div/div/div[2]/label/div/input").clear()
    driver.find_element_by_xpath("//body/div[4]/div/div/form/div[2]/div/div/div[2]/label/div/input").send_keys(products)
    driver.find_element_by_xpath("//body/div[4]/div/div/form/div[2]/div/div/div[2]/button").click()
    time.sleep(5)


def click_on_i_have_exported_in_the_last_12_months(driver: WebDriver):
    click_element = find_element(
        driver, find_selector_by_name(SELECTORS, "i have exported in last 12 months")
    )
    click_element.click()
    save = find_element(
        driver, find_selector_by_name(SELECTORS, "save")
    )
    save.click()


def search_again_top_bottom(driver: WebDriver):
    try:
        search_again_top_btn = find_element(
            driver, find_selector_by_name(SELECTORS, "top search again")
        )
        search_again_top_btn.click()
    except:
        try:
            search_again_btm_btn = find_element(
                driver, find_selector_by_name(SELECTORS, "bottom search again")
            )
            search_again_btm_btn.click()
        except:
            pass


def select_product_search_again_top_bottom(driver: WebDriver, product_name: str):
    product_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "product-btn")
    )
    product_btn.click()
    search_again_top_bottom(driver)
    driver.implicitly_wait(1)
    driver.find_element_by_xpath("//body/div[4]/div/div/form/div[2]/div/div/div[2]/label/div/input").clear()
    driver.find_element_by_xpath("//body/div[4]/div/div/form/div[2]/div/div/div[2]/label/div/input").send_keys(
        product_name)
    driver.find_element_by_xpath("//body/div[4]/div/div/form/div[2]/div/div/div[2]/button").click()


# Inorder to copy this code, 3 elements to be copied
# as per the element path on the browser
# save_product_btn, parent_1_div_element, search next button
def search_select_save_radio(driver: WebDriver):
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
                "//body/div[4]/div/div/form/div[2]/div/span/div/section[1]/button")
            save_btn_found = True
        except Exception as ex:
            logging.debug("save button not found.Exception: " + str(ex))

        if save_btn_found == True:
            logging.debug("Save button found")
            save_product_btn.click()
            return
        # look for div's and radio buttons
        parent_1_div_element = driver.find_element_by_xpath(
            "//body/div[4]/div/div/form/div[2]/div/span/div/section[1]/div")  # ("interaction grid m-v-xs")
        #child_1_div_element = parent_1_div_element.find_element_by_tag_name("div")  # ("c-fullwidth")
        main_div_element = parent_1_div_element.find_element_by_tag_name("div")  # "m-b-xs"
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


def search_select_save_random_next(driver: WebDriver):
    search_select_save_radio(driver)


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()


# def generate_form_details(actor: Actor) -> dict:
#     result = {
#         "please give detail": "automated tests",
#         "first name": f"send by {actor.alias} - automated tests",
#         "last name": "automated tests",
#
#     }
#     return result
#     driver.find_element_by_css_selector("#id_terms_agreed-label").click()
#     driver.find_element_by_css_selector("#form-container > button").click()

def fills_out_submit(driver: WebDriver, page_name):
    driver.find_element_by_css_selector("#id_comment").clear()
    driver.find_element_by_css_selector("#id_comment").send_keys("Automated Tests")

def find_and_select_random_export_plan(driver: WebDriver):
    div_list_export_plan_xpath = driver.find_element_by_xpath("//body/main/div/div/div[1]/div")
    export_plan_xpath_div_1_elements = div_list_export_plan_xpath.find_elements_by_tag_name("div[1]")
    random_number = 1
    if len(export_plan_xpath_div_1_elements) > 2:
        random_number = random.randint(1, len(export_plan_xpath_div_1_elements) - 1)
    random_li_element = export_plan_xpath_div_1_elements[random_number]
    export_plan_xpath_div_2_elements = export_plan_xpath_div_1_elements.find_element_by_tag_name("div")
    article_element= random_li_element.find_element_by_tag_name("article")
    article_element.find_element_by_tag_name("a").click()


#/html/body/main/div/div/div[1]/div/div[2]/article/a
#/html/body/main/div/div/div[1]/div/div[3]/article/a
