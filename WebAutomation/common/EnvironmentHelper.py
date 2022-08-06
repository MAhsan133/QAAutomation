import os


class EnvironementSetup:

    @staticmethod
    def get_browser():
        browser = "chrome"
        try:
            browser = os.environ['BROWSER']
        except KeyError:
            pass
        return browser

    @staticmethod
    def get_base_url():
        base_url = "localhost"
        try:
            base_url = os.environ['BASE_URL']
        except KeyError:
            pass
        return base_url
