import logging
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
import utilities.custom_logger as cl

"""

Base Page class implementation
It implements methods which are common to all the pages throughout the application

"""

class BasePage(SeleniumDriver):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        """
        Inits BasePage class
        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver


    def verify_page_title(self, title_to_verify):
        try:
            actual_title = self.get_title()
            return self.util.verifyTextContains(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

