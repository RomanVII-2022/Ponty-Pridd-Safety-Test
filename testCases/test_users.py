from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.loginPage import Login
from pageObjects.userPage import Users
import time


class Test_002_users:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def ponty_dashboard(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        login = Login(self.driver, self.logger)
        login.enterEmail("admin@pontypriddholdings.com")
        login.enterPassword("123456")
        login.clickLogin()
        self.logger.debug("**** Login was successful ****")

    def test_users_landing_page(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.navusers()
        self.logger.debug("**** Users landing page was accessed successfully ****")
    
    def test_add_user(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.addUser()
        users.fullNames("Martin Kariuki")
        users.email("martin.kariuki@pontypriddholdings.com")
        users.phoneNumber("782394446")
        users.jobTitle("Quality Assuarance")
        users.password("tuesday")
        users.selectRole("User")
        users.selectStatus("Active")
        users.saveBtn()
        errmsg = users.errorMessage()
        if errmsg == "No error":
            self.logger.debug("**** User was added successfully ****")
            assert True
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/homepageTitle.png")
            self.logger.debug("**** Something went wrong. An error occurred while adding user ****")
            assert False


    

