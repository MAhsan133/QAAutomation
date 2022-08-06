from selenium.webdriver.common.by import By


class UserLoginLocators:
    SIGN_IN_NAV_LINK = (By.ID, "nav-link-accountList")
    SIGN_IN_BUTTON = (By.ID, "nav-flyout-ya-signin")
    REGISTER_BUTTON = (By.XPATH, "//*[@id='nav-flyout-ya-newCust']/a")
    SIGN_IN_SCREEN_TITLE = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/h1')
    SIGN_IN_EMAIL_MOBILE_LABEL = (By.XPATH,
                                  '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/label')
    SIGN_IN_EMAIL_MOBILE_INPUT = (By.ID, "ap_email")
    SIGN_IN_CONTINUE_BUTTON = (By.ID, "continue")
    SIGN_IN_EMAIL_FIELD_ERROR = (
        By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/div/div/div')
    SIGN_IN_SCREEN_ERROR = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/ul/li/span')
    SIGN_IN_CREATE_AMAZON_bUTTON = (By.ID, "createAccountSubmit")
    SIGN_IN_PASSWORD_LABEL = (
        By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/div[1]/div[1]/label')
    SIGN_IN_PASSWORD_INPUT = (By.ID, "ap_password")
    SIGN_IN_PASSWORD_FIELD_ERROR = (
        By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/div[2]/div/div')
    SIGN_IN_SIGNIN_BUTTON = (By.ID, "signInSubmit")
