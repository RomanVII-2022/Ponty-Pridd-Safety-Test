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
        login.enterEmail("admin@quatrixglobal.com")
        login.enterPassword("123456")
        login.clickLogin()
        time.sleep(3)
        Url = self.driver.current_url
        if Url == self.base_url + 'home':
            self.logger.debug("**** Login was successfull ****")
            assert True
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/login.png")
            self.logger.debug("**** Something went wrong while logging in ****")
            assert False

    def test_login_wrong_email(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        login = Login(self.driver, self.logger)
        login.enterEmail("abc@pontypriddholdings.com")
        login.enterPassword("123456")
        login.clickLogin()
        errormsg = login.errorMessage()
        if errormsg == "Account with Email not Found":
            assert True
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/wrongemail.png")
            self.logger.debug("**** Error messsage shown did not match ****")
            assert False

    def test_login_wrong_password(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        login = Login(self.driver, self.logger)
        login.enterEmail("admin@quatrixglobal.com")
        login.enterPassword("1234")
        login.clickLogin()
        errormsg = login.errorMessage()
        if errormsg == "Email and Password do not Match":
            assert True
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/wrongpassword.png")
            self.logger.debug("**** Error messsage shown did not match ****")
            assert False

    def test_login_wrong_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        login = Login(self.driver, self.logger)
        login.enterEmail("abc@pontypriddholdings.com")
        login.enterPassword("1234")
        login.clickLogin()
        errormsg = login.errorMessage()
        if errormsg == "Account with Email not Found":
            assert True
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/wrongcredentials.png")
            self.logger.debug("**** Error messsage shown did not match ****")
            assert False


    def test_password_reset(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        login = Login(self.driver, self.logger)
        login.forgotPassword()
        login.forgotEmail("admin@quatrixglobal.com")
        login.resetBtn()
        msg = login.passwordResetEmail()
        if msg == "An email with the reset link has been sent":
            self.logger.debug("**** The two alert messages matched ****")
            assert True
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/passwordreset.png")
            self.logger.debug("**** The two alert messages did not match ****")
            assert False


    def test_unregistered_email_password_reset(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        login = Login(self.driver, self.logger)
        login.forgotPassword()
        login.forgotEmail("nodejs@pontypriddholdings.com")
        login.resetBtn()
        msg = login.textDanger()
        if msg == "Account does not exist":
            self.logger.debug("**** Password reset link was not sent ****")
            assert True
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/unregisteredemailreset.png")
            self.logger.debug("**** Password reset link was sent and user email is not registered ****")
            assert False



