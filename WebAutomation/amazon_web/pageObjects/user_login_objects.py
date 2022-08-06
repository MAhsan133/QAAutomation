import time
from WebAutomation.amazon_web.pageObjects.user_login_locators import UserLoginLocators
from WebAutomation.common.ElementHelper import LocatorHelper
from selenium.webdriver.common.action_chains import ActionChains


class UserLoginObjects(object):
    def __init__(self):
        self.locators = UserLoginLocators()

    def set_driver(self, browser, base_url):
        self.helper = LocatorHelper(browser)
        self.browser = browser
        self.base_url = base_url

    def open_home_page(self):
        self.browser.get("https://{}/".format(self.base_url))

    def click_link_button(self, link):
        nav_element = self.helper.wait_for_element_visibility(self.locators.SIGN_IN_NAV_LINK)
        action = ActionChains(self.browser)
        action.move_to_element(nav_element).perform()
        time.sleep(1)
        if link == 'Sign in':
            self.helper.wait_for_element_visibility(self.locators.SIGN_IN_BUTTON).click()
        else:
            self.helper.wait_for_element_visibility(self.locators.REGISTER_BUTTON).click()

    def verify_signin_screen_title(self):
        return self.helper.wait_for_element_visibility(self.locators.SIGN_IN_SCREEN_TITLE).text

    def get_signin_fields_detail(self, field):
        field_label_locator = None
        field_value_locator = None
        if field == 'Email or mobile phone number':
            field_label_locator = self.locators.SIGN_IN_EMAIL_MOBILE_LABEL
            field_value_locator = self.locators.SIGN_IN_EMAIL_MOBILE_INPUT
        elif field == 'Password':
            field_label_locator = self.locators.SIGN_IN_PASSWORD_LABEL
            field_value_locator = self.locators.SIGN_IN_PASSWORD_INPUT
        field_label = self.helper.wait_for_element_visibility(field_label_locator).text
        field_value = self.helper.wait_for_element_visibility(field_value_locator).get_attribute('value')
        return field_label, field_value

    def verify_signin_screen_button(self):
        return self.helper.wait_for_element_visibility(self.locators.SIGN_IN_CONTINUE_BUTTON).text

    def click_signin_screen_button(self, button):
        if button == 'Continue':
            self.helper.wait_for_element_visibility(self.locators.SIGN_IN_CONTINUE_BUTTON).click()
        elif button == 'Sign-In':
            self.helper.wait_for_element_visibility(self.locators.SIGN_IN_SIGNIN_BUTTON).click()
        else:
            self.helper.wait_for_element_visibility(self.locators.SIGN_IN_CREATE_AMAZON_bUTTON).click()

    def verify_signin_fields_errors(self, field):
        if field == 'Email or mobile phone number':
            return self.helper.wait_for_element_visibility(self.locators.SIGN_IN_EMAIL_FIELD_ERROR).text
        elif field == 'Password':
            return self.helper.wait_for_element_visibility(self.locators.SIGN_IN_PASSWORD_FIELD_ERROR).text

    def fill_in_fields(self, field, value):
        if field == 'Email or mobile':
            self.helper.type_text(self.locators.SIGN_IN_EMAIL_MOBILE_INPUT, value)
        elif field == 'Password':
            self.helper.type_text(self.locators.SIGN_IN_PASSWORD_INPUT, value)

    def verify_signin_errors(self, field):
        time.sleep(1)
        if field == 'Mobile number or email' or 'Password':
            return self.helper.wait_for_element_visibility(self.locators.SIGN_IN_SCREEN_ERROR).text

    def verify_create_amazon_button(self):
        return self.helper.wait_for_element_visibility(self.locators.SIGN_IN_CREATE_AMAZON_bUTTON).text

