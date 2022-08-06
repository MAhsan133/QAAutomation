from selenium.webdriver.common.by import By


class UserRegistrationLocators:
    SIGN_UP_SCREEN_TITLE = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/h1')
    SIGN_UP_YOUR_NAME_LABEL = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/label")
    SIGN_UP_YOUR_NAME_INPUT = (By.ID, "ap_customer_name")
    SIGN_UP_MOBILE_PHONE_LABEL = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/label")
    SIGN_UP_MOBILE_PHONE_INPUT = (By.ID, "ap_email")
    SIGN_UP_PASSWORD_LABEL = (
        By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[3]/div[1]/label')
    SIGN_UP_PASSWORD_INPUT = (By.ID, "ap_password")
    SIGN_UP_RE_ENTER_PASSWORD_LABEL = (
        By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[3]/div[2]/label')
    SIGN_UP_RE_ENTER_PASSWORD_INPUT = (By.ID, "ap_password_check")
    SIGNUP_UP_BUTTON = (By.ID, "auth-continue")
    YOUR_NAME_FIELD_ERROR = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/div/div/div')
    MOBILE_PHONE_FIELD_ERROR = (By.XPATH,
                                '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[2]/div[3]/div/div')
    PASSWORD_FIELD_ERROR = (By.XPATH,
                            '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[3]/div[1]/div[2]/div/div')
    CONFIRM_PASSWORD_ERROR = (
        By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[3]/div[2]/div[1]/div/div')
    INVALID_EMAIL_ERROR = (By.XPATH, '//*[@id="auth-email-invalid-claim-alert"]')
    INVALID_PASSWORD_ERROR = (By.XPATH, '//*[@id="auth-password-invalid-password-alert"]')
    INVALID_MISSMATCHED_ERROR = (By.XPATH, '//*[@id="auth-password-mismatch-alert"]')
    VALIDATE_PUZZLE_TITLE = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div/div/div[1]/span')
