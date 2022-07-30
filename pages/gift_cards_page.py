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
        driver.execute_script("window.scrollTo(0,400);")
        self.wait_for_element(self.locator['currency_option'], locator_type="xpath")
        print(self.get_element_list(self.locator['currency_option'], locator_type="xpath"))
        print(self.get_element_list(self.locator['currency_amount_option'], locator_type="xpath"))


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




bc = BrowserConfiguration("chrome")
driver = bc.web_driver_instance()
tete = GiftCardsPage(driver).check_available_gift_cards()

