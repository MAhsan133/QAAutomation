from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from WebAutomation.common.EnvironmentHelper import EnvironementSetup


class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.
    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class CreateBrowser(object):

    def initiate_instance(self):
        env_obj = EnvironementSetup()
        driver_path = self.get_driver_path(env_obj)
        browser_options = Options()
        browser_options.add_argument("--start-maximized")
        browser_options.add_argument('--headless')
        browser_options.add_argument('--no-sandbox')
        browser_options.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(executable_path=driver_path, options=browser_options)
        return browser, env_obj.get_base_url()

    @staticmethod
    def get_driver_path(env_obj):
        driver_path = None
        current_path = os.getcwd()
        browser = env_obj.get_browser()
        if browser == 'chrome':
            driver_path = os.path.join(current_path, "WebAutomation", "drivers", "chromedriver")
        elif browser == 'firefox':
            driver_path = os.path.join(current_path, "WebAutomation", "drivers", "geckodriver")
        return driver_path
