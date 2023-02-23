from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.loginPage import Login
import time

class Test_001_Login:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.logger.debug("**** Website accessed successfully ****")
        actual_title = self.driver.title
        if actual_title == "Ponty Safety":
            self.logger.debug("**** Website title matches ****")
            assert True
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/homepageTitle.png")
            self.logger.debug("**** Website title does not match ****")
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        login = Login(self.driver, self.logger)
        login.enterEmail(input("Enter email: "))
        login.enterPassword(input("Enter password: "))
        login.clickLogin()
        time.sleep(3)
        Url = self.driver.current_url
        if Url == "https://dev.safety.pontypriddholdings.com/home":
            self.logger.debug("**** Login was successfull ****")
            assert True
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/login.png")
            self.logger.debug("**** Something went wrong while logging in ****")
            assert False





