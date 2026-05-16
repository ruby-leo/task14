from selenium.common import ElementClickInterceptedException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.read_json import get_config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_web_driver_wait(self):
        config = get_config()
        return WebDriverWait(self.driver, config["explicit_timeout"])

    def enter_text(self, locator, text):
        try:
            element = self.get_web_driver_wait().until(
                EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print("Timed out: Element not visible or disabled")
            raise

    def click(self, locator):
        def click_action(driver):
            try:
                element = EC.element_to_be_clickable(locator)(driver)
                if element:
                    element.click()
                    return True
            except (ElementClickInterceptedException, StaleElementReferenceException):
                return False
            return False

        try:
            self.get_web_driver_wait().until(click_action)
        except TimeoutException:
            print(f"Timed out: Element was not clickable")
            raise

    def is_displayed(self, locator):
        try:
            self.get_web_driver_wait().until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            print("Timed out: Element not displayed")
            return False

    def current_url(self, expected_url):
        try:
            self.get_web_driver_wait().until(EC.url_contains(expected_url))
        except TimeoutException:
            pass  # no action is needed in case of Time out Exception as that indicates it waited enough for the expected url
        return self.driver.current_url