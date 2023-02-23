import configparser


config = configparser.RawConfigParser()
config.read("/home/vmwai/Documents/tests/PontySafety/configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_app_url():
        url = config.get('common info', 'base_url')
        return url