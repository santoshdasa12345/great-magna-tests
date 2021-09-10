import logging
import random
import time
from types import ModuleType
from typing import List, Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

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

NAME = "About Your business"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_ABOUT_YOUR_BUSINESS.absolute
PAGE_TITLE = "About Your business Page"

SELECTORS = {
    "about your business": {
        "about your business": Selector(
            By.XPATH, "//*[@id=\"export-plan-dashboard\"]/div[1]/div/a/div[2]/h3"
        ),
        "how you started example": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div:nth-child(1) > div > div.learning__buttons > button"
        ),
        "how you started educational": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div:nth-child(1) > div > div.learning__buttons > div > div > button > i"#about-your-business-form > div:nth-child(1) > div > div.learning__buttons.m-b-xs > div > div > button > i"
        ),
        "how you started": Selector(
            By.XPATH, "//*[@id=\"story\"]", type=ElementType.INPUT
        ),
        "where you're based example": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div:nth-child(2) > div > div.learning__buttons > button"
        ),
        "where you're based": Selector(
            By.XPATH, "//*[@id=\"location\"]", type=ElementType.INPUT
        ),
        "how you make your products example": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div:nth-child(3) > div > div.learning__buttons > button"
        ),
        "how you make your products": Selector(
            By.XPATH, "//*[@id=\"processes\"]", type=ElementType.INPUT
        ),
        "your product packaging example": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div:nth-child(4) > div > div.learning__buttons > button"
        ),
        "your product packaging": Selector(
            By.XPATH, "//*[@id=\"packaging\"]", type=ElementType.INPUT
        ),
        "business performance drop down": Selector(
            By.XPATH, "//*[@id=\"about-your-business-form\"]/div[5]/button"
        ),
        "business objectives": Selector(
            By.CSS_SELECTOR, "#about-your-business-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > a > span"
        ),
        "export plan home": Selector(
            By.CSS_SELECTOR, "#about-your-business-content > section.p-v-m.bg-blue-deep-80 > div > div > div.c-2-3-m.c-1-2-xl > div.m-t-l > a"
        ),
        "move from accidental exporting to strategic exporting": Selector(
            By.XPATH, "//*[@id=\"about-your-business-content\"]/section[3]/div/div[1]/div/a/div/p"
        ),
        "your business performance label": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div.select.m-b-l > div > label"
        ),
        "your business performance dropdown": Selector(
            By.CSS_SELECTOR, "#about-your-business-form > div.select.m-b-l > button"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]"
        ),
        "nav business objectives": Selector(
            By.XPATH, "//a[contains(text(),'Business objectives')]"
        ),
        "yes checkbox": Selector(
            By.CSS_SELECTOR, "#section-complete > div > label"
        ),
        "top export plan home": Selector(
            By.CSS_SELECTOR, "#about-your-business-content > section.section--intro.bg-blue-deep-90 > div > div > div.c-2-3-m.c-1-2-xl.p-t-xl.p-b-s.text-white > span > a > span"
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


def find_and_select_random_item_list(driver: WebDriver, element_selector_name: str):
    # about-your-business-form > div.select.m-b-l > button
    drop_down_btn = driver.find_element_by_css_selector(
        "#about-your-business-form > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius > div.select__placeholder--value")
        #"#about-your-business-form > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius > div.select__placeholder--input")
    drop_down_btn.click()
    driver.implicitly_wait(5)
    # select__list body-l bg-white radius
    # about-your-business-form > div.select.m-b-l > ul
    drop_down_element = driver.find_element_by_css_selector("#about-your-business-form > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius > div.select__list.body-l.bg-white.radius.select__list--open")#about-your-business-form > div.select.m-b-l > div > div.select__placeholder.text-blue-deep-60.bg-white.radius > ul")
    li_elements = drop_down_element.find_elements_by_tag_name("li")
    logging.debug("list elements")
    logging.debug(li_elements)
    random_number = 0
    if len(li_elements) > 2:
        random_number = random.randint(1, len(li_elements) - 1)
    random_li_element = li_elements[random_number]
    logging.debug(random_number)
    logging.debug(random_li_element.tag_name)
    logging.debug(random_li_element)
    time.sleep(2)
    # random_li_element.click()

    # select = Select(random_li_element)
    # select.select_by_index(0)

    # £500,000 up to £1,999,999


def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()


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
    driver.find_element_by_xpath("//body/div[4]/div/div/form/div[2]/div/div/div[2]/label/div/input").send_keys(product_name)
    driver.find_element_by_xpath("//body/div[4]/div/div/form/div[2]/div/div/div[2]/button").click()


def search_select_save_random_next(driver: WebDriver):
    time.sleep(5)
    counter = 0
    while True:
        try:
            driver.implicitly_wait(1)
            logging.debug('Counter -> ' + str(counter))
            #//body/div[7]/div/div/form/div[2]/div/span/div/section[1]/div/div/div
            parent_div_element = driver.find_element_by_xpath(
                "//body/div[4]/div/div/form/div[2]/div/span/div/section[1]/div/div/div")
            logging.debug(parent_div_element)
            label_elements = parent_div_element.find_elements_by_tag_name("label")
            logging.debug('number of labels - ' + str(len(label_elements)))
            radio_elements = []
            for label_element in label_elements:
                try:
                    logging.debug(label_element)
                    radio_ele = label_element.find_element_by_tag_name("input")
                    radio_elements.append(radio_ele)
                except Exception as ex:
                    #logging.error('Érror selecting correct label -> ' + str(ex))
                    pass

            random_label_index = random.randint(0, len(radio_elements) - 1)
            logging.debug('Index of radio buttons to be selected - ' + str(random_label_index))
            if random_label_index <= len(radio_elements):
                # label_elements[random_label_index]
                for index, random_radio_element in enumerate(radio_elements):
                    if random_label_index == index:
                        logging.debug('Selecting Index of radio buttons - ' + str(index))
                        random_radio_element.click()
                        try:
                            driver.implicitly_wait(1)
                            search_next_btn = find_element(
                                driver, find_selector_by_name(SELECTORS, "search next button")
                            )
                            search_next_btn.click()
                        except Exception as ex:
                            driver.implicitly_wait(1)
                            save_product_btn = find_element(
                                driver, find_selector_by_name(SELECTORS, "save product")
                            )
                            save_product_btn.click()
                            break
            counter += 1
            if counter >= 20:
                break
        except Exception as ex:
            logging.error(str(ex))
            break



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
    try:
        time.sleep(1)
        skip_link = find_element(
            driver, find_selector_by_name(SELECTORS, "skipwalkthrough")
        )
        skip_link.click()
    except:
        pass

    try:
        time.sleep(1)
        if driver.find_element_by_css_selector("body > div:nth-child(11) > div > div > button").is_displayed():
            driver.find_element_by_css_selector("body > div:nth-child(11) > div > div > button").click()
    except:
        pass

    try:
        if driver.find_element_by_xpath("//button[contains(text(),'Got it')]").is_displayed():
            driver.find_element_by_xpath("//button[contains(text(),'Got it')]").click()
    except:
        pass

    # country
    time.sleep(1)
    country_btn = find_element(
        driver, find_selector_by_name(SELECTORS, "country-btn")
    )
    country_btn.click()
    try:
        time.sleep(1)
        if driver.find_element_by_css_selector("body > div:nth-child(14) > div > div > button").is_displayed():
            driver.find_element_by_css_selector("body > div:nth-child(14) > div > div > button").click()
    except:
        pass

    time.sleep(1)
    if 0 == len(country):
        path_random_country_element = "body > div:nth-child(13) > div > div > div > div > div > div.only-desktop > div.suggested-markets > ul > button:nth-child(" + str(
            random.randint(1, 5)) + ")"
        driver.find_element_by_css_selector(path_random_country_element).click()
    else:
        try:
            if driver.find_element_by_xpath("//button[contains(text(),'Got it')]").is_displayed():
                driver.find_element_by_xpath("//button[contains(text(),'Got it')]").click()
        except:
            pass
        driver.find_element_by_css_selector("#search-input").clear()
        driver.find_element_by_css_selector("#search-input").send_keys(country)

        buttons_elements = driver.find_elements_by_tag_name("button")
        # logging.debug(buttons_elements)
        for button_element in buttons_elements:
            # logging.debug(button_element.text)
            if button_element.text == country.lower():
                button_element.click()
                # time.sleep(5)
                break
        # country_name_btn_xpath = "//button[contains(text(),'"+ country + "')]"
        # driver.find_element_by_xpath(country_name_btn_xpath).click()
    # try:
    #     time.sleep(1)
    #     driver.find_element_by_xpath("//a[@id='page-tour-skip']").click()
    # except:
    #     pass


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
