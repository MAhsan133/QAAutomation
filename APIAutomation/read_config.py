import os
import configparser


class ReadConfigFile(object):
    def __init__(self):
        current_file_path = os.path.dirname(__file__)
        abs_file_path = os.path.join(current_file_path, 'defaults.cfg')
        self.config = configparser.ConfigParser()
        self.config.read_file(open(abs_file_path))

    def get_user_credentails(self):
        base_url, refresh_token, app_key = "", "", ""
        try:
            base_url = self.config['DEFAULT']['BASE_URL']
            refresh_token = self.config['DEFAULT']['API_REFRESH_TOKEN']
            app_key = self.config['DEFAULT']['API_APP_KEY']
        except KeyError:
            pass
        return base_url, refresh_token, app_key
