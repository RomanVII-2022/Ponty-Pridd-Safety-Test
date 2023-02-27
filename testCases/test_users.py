from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.loginPage import Login
import time


class Test_002_users:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_users_url(self, setup):
        pass