from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import time
import os
import utilities.custom_logger as cl


class SeleniumDriver:

    log = cl.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, result_message):
        """
        Takes a screenshot of the current page.
        """
        file_name = result_message + "." + str(round(time.time() *1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to directory: " + destination_file)
        except:
            self.log.error("Exception occured when taking screenshot.")
            print_stack()

    def get_title(self):

        title = self.driver.title

        return title
        log.info("Title is: ")


    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'classname':
            return By.CLASS_NAME
        elif locator_type == 'linktext':
            return By.LINK_TEXT
        else:
            self.log.info("Locator type "+ locator_type + " not correct/supported")
        return False


    def get_element(self, locator, locator_type='id', element=None):
        element = None
        try:
            locator = locator
            locator_type = locator_type
            byType = self.get_by_type(locator_type)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator + " and locatorType: " + locator_type)
        except:
            self.log.info("Element not found with locator: " + locator + " and locatorType: " + locator_type)
        return element


    def get_element_list(self, locator, locator_type="id"):
        """
        Get list of elements
        """
        elements = []
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)

            self.log.info("Element list found with locator: " + locator + " and locatorType: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator + " and locatorType: " + locator_type)
        return elements


    def element_click(self, locator, locator_type ='id', element=None):
        try:
            if locator:
                locator = locator
                locator_type = locator_type
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Can'/t not click on the element with locator: " + locator + " locatorType: " + locator_type)
            print_stack()


    def send_keys(self, data, locator, locatorType ='id'):
        try:
            if locator:
                element = self.get_element(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: "+ locator + " locatorType: " + locatorType)
        except:
            self.log.info("Can'/t sent on the element with locator: " + locator + " locatorType: " + locatorType )


    def clear_field(self, locator="", locatorType="id"):
        element = self.get_element(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator + "locatorType: " + locatorType)


    def get_text(self, locator="", locator_type="id", element=None, info=""):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text


    def is_element_present(self, locator="", locator_type="id"):
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
                if element is not None:
                    self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locator_type)
                    return True
                else:
                    self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locator_type)
                    return False
        except:
            print("Element not found")
            return False


    def is_element_displayed(self, locator="", locator_type="id", element=None):
        is_displayed = False
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                is_displayed = True
                self.log.info("Element is displayed")
            else:
                self.log.info("Element not displayed")
            return is_displayed
        except:
            print("Element not found")
            return False


    def element_presence_check(self, locator, by_type):
        """
        Check if element is present.
        """
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element present with locator: " + locator +" locator_type: " + str(by_type))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locator_type: " + str(by_type))
                return False
        except:
            self.log.info("Element not found")
            return False


    def wait_for_element(self, locator, locator_type="id", timeout=10, poll_frequency=0.2):
        element = None
        try:
            byType = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element


    def web_scroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")


