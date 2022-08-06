from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LocatorHelper(object):
    def __init__(self, browser):
        self.timeout = 15
        self.driver = browser

    def wait_for_element_presence(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def wait_for_element_visibility(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisibility(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_all_elements_presence(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))

    def type_text(self, locator, value):
        element = self.wait_for_element_visibility(locator)
        element.clear()
        element.send_keys(value)