import sys
import time
from utilities import custom_logger as cl
import logging
from base.base_page import BasePage
from locators.read_locators import get_locator as locator
from base.browser_configuration import BrowserConfiguration
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class GiftCardsPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = locator()['GIFT_CARDS']

    def check_available_gift_cards(self):
        self.get_title()

        self.wait_for_element(self.locator['cookies_pop_up_window'])
        self.element_click(self.locator['cookies_accept'], locator_type="xpath")
        self.wait_for_element(self.locator['gift_cards'], locator_type="xpath")
        self.element_click(self.locator['gift_cards'], locator_type="xpath")
        self.wait_for_element(self.locator['vouchers'], locator_type="xpath")
        driver.execute_script("window.scrollTo(0,200);")
        get_all_vouchers = self.get_element_list(self.locator['vouchers'], locator_type="xpath")
        vouchers_id = [element_id.get_attribute("id") for element_id in get_all_vouchers]

        for voucher in vouchers_id:
            driver.implicitly_wait(2)
            voucher_location = "//input[@id='{}']/parent::div".format(voucher)
            self.wait_for_element(locator=voucher_location, locator_type="xpath")
            self.is_element_present(locator=voucher_location, locator_type="xpath")
            self.element_click(locator=voucher_location, locator_type="xpath")
            driver.implicitly_wait(2)
            self.screen_shot("Voucher")
        test = self.get_voucher_currency()
        self.get_currency_value(test)


        # self.wait_for_element(self.locator['currency_option'], locator_type="xpath")
        # currency_list= self.get_element_list(self.locator['currency_option'], locator_type="xpath")
        # curr_value_list = self.get_element_list(self.locator['currency_amount_option'], locator_type="xpath")
        # new_list = []
        # for item in currency_list:
        #     xpath_item = "//select[starts-with(@id,'currencySelector')]/option[@value='{}']".format(item.get_attribute("value"))
        #     new_list.append(xpath_item)
        #
        # self.element_click(self.locator['currency_selector'], locator_type="xpath")
        # self.element_click(locator=new_list[5], locator_type="xpath")
        # print(new_list, file=sys.stderr)


    def voucher_selection_check(self):
        self.wait_for_element(self.locator['vouchers'], locator_type="xpath")
        get_all_vouchers = self.get_element_list(self.locator['vouchers'], locator_type="xpath")
        vouchers_id = [element_id.get_attribute("id") for element_id in get_all_vouchers]
        for voucher in vouchers_id:
            driver.implicitly_wait(2)
            voucher_location = "//input[@id='{}']/parent::div".format(voucher)
            self.wait_for_element(locator=voucher_location, locator_type="xpath")
            self.is_element_present(locator=voucher_location, locator_type="xpath")
            self.element_click(locator=voucher_location, locator_type="xpath")
            driver.implicitly_wait(2)
            self.screen_shot("Voucher")

    def get_voucher_currency(self):
        driver.execute_script("window.scrollTo(0,400);")
        self.wait_for_element(self.locator['currency_option'], locator_type="xpath")
        currency = self.get_element_list(self.locator['currency_option'], locator_type="xpath")
        currency_xpath_list = []
        currency_value_list = []
        for item in currency:
            currency_xpath = "//select[starts-with(@id,'currencySelector')]/option[@value='{}']".format(item.get_attribute("value"))
            currency_value = item.get_attribute("value")
            currency_xpath_list.append(currency_xpath)
            currency_value_list.append(currency_value)
        currency_val = dict(zip(currency_value_list,currency_xpath_list))
        return currency_val

    def get_currency_value(self, currency_types=dict):
            print(currency_types)
            if currency_types:
                currency_values = {}

                for key in list(currency_types.keys()):
                    print(key, file=sys.stderr)
                    self.element_click(locator=currency_types[key], locator_type="xpath")
                    currency_amount = self.get_element_list(self.locator['currency_amount_option'],
                                                                locator_type="xpath")
                    curr_ammount = []
                    for element in currency_amount:
                        element_xpath = "//select[starts-with(@id,'amountSelector')]/option[@value='{}']".format(
                        element.get_attribute("value"))
                        print(element_xpath)
                        curr_ammount.append(element_xpath)

                    currency_values[key] = curr_ammount

            return currency_values

        # self.element_click(self.locator['currency_selector'], locator_type="xpath")
        # self.element_click(locator=new_list[5], locator_type="xpath")
        # print(new_list, file=sys.stderr)
        # currency_value = self.get_element_list(self.locator['currency_amount_option'], locator_type="xpath")

bc = BrowserConfiguration("chrome")
driver = bc.web_driver_instance()
tete = GiftCardsPage(driver).check_available_gift_cards()

