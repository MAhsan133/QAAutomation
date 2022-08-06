from WebAutomation.amazon_web.pageObjects.user_registration_locators import UserRegistrationLocators
from WebAutomation.common.ElementHelper import LocatorHelper


class UserRegistrationObjects(object):
    def __init__(self):
        self.locators = UserRegistrationLocators()

    def set_driver(self, browser, base_url):
        self.helper = LocatorHelper(browser)
        self.browser = browser
        self.base_url = base_url

    def verify_registration_screen(self):
        return self.helper.wait_for_element_visibility(self.locators.SIGN_UP_SCREEN_TITLE).text

    def get_your_name_info(self):
        your_name_label = self.helper.wait_for_element_visibility(self.locators.SIGN_UP_YOUR_NAME_LABEL).text
        your_name = self.helper.wait_for_element_visibility(
            self.locators.SIGN_UP_YOUR_NAME_INPUT).get_attribute('placeholder')
        return your_name_label, your_name

    def get_mobile_email_info(self):
        mobile_email_label = self.helper.wait_for_element_visibility(self.locators.SIGN_UP_MOBILE_PHONE_LABEL).text
        mobile_email = self.helper.wait_for_element_visibility(
            self.locators.SIGN_UP_MOBILE_PHONE_INPUT).get_attribute('value')
        return mobile_email_label, mobile_email

    def get_password_info(self):
        password_label = self.helper.wait_for_element_visibility(self.locators.SIGN_UP_PASSWORD_LABEL).text
        password = self.helper.wait_for_element_visibility(
            self.locators.SIGN_UP_PASSWORD_INPUT).get_attribute('placeholder')
        return password_label, password

    def get_re_enter_password(self):
        re_enter_password_label = self.helper.wait_for_element_visibility(
            self.locators.SIGN_UP_RE_ENTER_PASSWORD_LABEL).text
        re_enter_password = self.helper.wait_for_element_visibility(
            self.locators.SIGN_UP_RE_ENTER_PASSWORD_INPUT).get_attribute('value')
        return re_enter_password_label, re_enter_password

    def get_create_account_fields(self):
        temp_dict = {}
        your_name_label, your_name = self.get_your_name_info()
        mobile_email_label, mobile_email = self.get_mobile_email_info()
        password_label, password = self.get_password_info()
        re_enter_password_label, re_enter_password = self.get_re_enter_password()
        temp_dict[your_name_label] = your_name
        temp_dict[mobile_email_label] = mobile_email
        temp_dict[password_label] = password
        temp_dict[re_enter_password_label] = re_enter_password
        return temp_dict

    def verify_signup_screen_button(self):
        return self.helper.wait_for_element_visibility(self.locators.SIGNUP_UP_BUTTON).text

    def click_signup_screen_button(self, button):
        if button in ['Continue', 'Verify email', 'Verify mobile number']:
            self.helper.wait_for_element_visibility(self.locators.SIGNUP_UP_BUTTON).click()

    def verify_signup_field_errors(self, label):
        if label == 'Your name':
            locator = self.locators.YOUR_NAME_FIELD_ERROR
        elif label == 'Mobile number or email':
            locator = self.locators.MOBILE_PHONE_FIELD_ERROR
        elif label == 'Password':
            locator = self.locators.PASSWORD_FIELD_ERROR
        else:
            locator = self.locators.CONFIRM_PASSWORD_ERROR
        return self.helper.wait_for_element_visibility(locator).text

    def fill_in_the_field(self, field, value):
        if field == 'Your name':
            locator = self.locators.SIGN_UP_YOUR_NAME_INPUT
        elif field == 'Mobile number or email':
            locator = self.locators.SIGN_UP_MOBILE_PHONE_INPUT
        elif field == 'Password':
            locator = self.locators.SIGN_UP_PASSWORD_INPUT
        else:
            locator = self.locators.SIGN_UP_RE_ENTER_PASSWORD_INPUT
        self.helper.type_text(locator, value)

    def verify_invalid_field_errors(self, field):
        locator = None
        if field == 'Mobile number or email':
            locator = self.locators.INVALID_EMAIL_ERROR
        elif field == 'Password':
            locator = self.locators.INVALID_PASSWORD_ERROR
        elif field == 'Re-enter password':
            locator = self.locators.INVALID_MISSMATCHED_ERROR
        return self.helper.wait_for_element_visibility(locator).text

    def verify_puzzle_screen_shown(self):
        return self.helper.wait_for_element_visibility(self.locators.VALIDATE_PUZZLE_TITLE).text
