from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.loginPage import Login
from pageObjects.userPage import Users
from selenium.webdriver.common.by import By
import time


class Test_002_users:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_ponty_dashboard(self, setup):
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
        users.fullNames("Osman Osman")
        users.email("osman.osman@pontypriddholdings.com")
        users.phoneNumber("782333346")
        users.jobTitle("Quality Assuarance")
        users.password("tuesday")
        users.selectRole("User")
        users.selectStatus("Active")
        users.saveBtn()
        time.sleep(3)
        msg = users.errorMessage()
        if msg == "No error":
            self.logger.debug("**** User was added successfully ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/addusererror.png")
            self.logger.debug("**** Something went wrong. An error occurred while adding user ****")
            users.closeBtn()
            assert False
    


    def test_add_user_noname(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.addUser()
        users.fullNames("")
        users.email("osman.osman@pontypriddholdings.com")
        users.phoneNumber("782333346")
        users.jobTitle("Quality Assuarance")
        users.password("tuesday")
        users.selectRole("User")
        users.selectStatus("Active")
        users.saveBtn()
        time.sleep(3)
        msg = users.errorMessage()
        if msg == "Name cannot be Empty":
            self.logger.debug("**** Expected error message matched ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/noname.png")
            self.logger.debug("**** Something went wrong. Expected error did not match ****")
            users.closeBtn()
            assert False



    def test_add_user_noemail(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.addUser()
        users.fullNames("Osman Osman")
        users.email("")
        users.phoneNumber("782333346")
        users.jobTitle("Quality Assuarance")
        users.password("tuesday")
        users.selectRole("User")
        users.selectStatus("Active")
        users.saveBtn()
        time.sleep(3)
        msg = users.errorMessage()
        if msg == "Email is Invalid":
            self.logger.debug("**** Expected error message matched ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/noemail.png")
            self.logger.debug("**** Something went wrong. Expected error did not match ****")
            users.closeBtn()
            assert False



    def test_add_user_invalidemail(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.addUser()
        users.fullNames("Osman Osman")
        users.email("osman.gmail.com")
        users.phoneNumber("782333346")
        users.jobTitle("Quality Assuarance")
        users.password("tuesday")
        users.selectRole("User")
        users.selectStatus("Active")
        users.saveBtn()
        time.sleep(3)
        msg = users.errorMessage()
        if msg == "Email is Invalid":
            self.logger.debug("**** Expected error message matched ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/invalidemail.png")
            self.logger.debug("**** Something went wrong. Expected error did not match ****")
            users.closeBtn()
            assert False


    def test_add_user_existingemail(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.addUser()
        users.fullNames("Osman Osman")
        users.email("osman.osman@pontypriddholdings.com")
        users.phoneNumber("782333346")
        users.jobTitle("Quality Assuarance")
        users.password("tuesday")
        users.selectRole("User")
        users.selectStatus("Active")
        users.saveBtn()
        time.sleep(3)
        msg = users.errorMessage()
        if msg == "User with Email Address already Exists":
            self.logger.debug("**** Expected error message matched ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/existingemail.png")
            self.logger.debug("**** Something went wrong. Expected error did not match ****")
            users.closeBtn()
            assert False


    def test_add_user_nonumber(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.addUser()
        users.fullNames("Osman Osman")
        users.email("osman@pontypriddholdings.com")
        users.phoneNumber("")
        users.jobTitle("Quality Assuarance")
        users.password("tuesday")
        users.selectRole("User")
        users.selectStatus("Active")
        users.saveBtn()
        time.sleep(3)
        msg = users.errorMessage()
        if msg == "Request failed with status code 500":
            self.logger.debug("**** Expected error message matched ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/nonumber.png")
            self.logger.debug("**** Something went wrong. Expected error did not match ****")
            users.closeBtn()
            assert False


    def test_add_user_existingnumber(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.addUser()
        users.fullNames("Osman Osman")
        users.email("osman@pontypriddholdings.com")
        users.phoneNumber("782333346")
        users.jobTitle("Quality Assuarance")
        users.password("tuesday")
        users.selectRole("User")
        users.selectStatus("Active")
        users.saveBtn()
        time.sleep(3)
        msg = users.errorMessage()
        if msg == "User with Phone Number already Exists":
            self.logger.debug("**** Expected error message matched ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/existingnumber.png")
            self.logger.debug("**** Something went wrong. Expected error did not match ****")
            users.closeBtn()
            assert False


    def test_add_user_nojob(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.addUser()
        users.fullNames("Osman Osman")
        users.email("osman@pontypriddholdings.com")
        users.phoneNumber("782333346")
        users.jobTitle("")
        users.password("tuesday")
        users.selectRole("User")
        users.selectStatus("Active")
        users.saveBtn()
        time.sleep(3)
        msg = users.errorMessage()
        if msg == "Job Title cannot be Empty":
            self.logger.debug("**** Expected error message matched ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/nojob.png")
            self.logger.debug("**** Something went wrong. Expected error did not match ****")
            users.closeBtn()
            assert False


    def test_add_user_nopassword(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.addUser()
        users.fullNames("Osman Osman")
        users.email("osman@pontypriddholdings.com")
        users.phoneNumber("782333346")
        users.jobTitle("Operations")
        users.password("")
        users.selectRole("User")
        users.selectStatus("Active")
        users.saveBtn()
        time.sleep(3)
        msg = users.errorMessage()
        if msg == "Password cannot be Empty":
            self.logger.debug("**** Expected error message matched ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/nopassword.png")
            self.logger.debug("**** Something went wrong. Expected error did not match ****")
            users.closeBtn()
            assert False


    def test_add_user_norole(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.addUser()
        users.fullNames("Osman Osman")
        users.email("osman@pontypriddholdings.com")
        users.phoneNumber("782333346")
        users.jobTitle("Operations")
        users.password("tuesday")
        users.selectRole("")
        users.selectStatus("Active")
        users.saveBtn()
        time.sleep(3)
        msg = users.errorMessage()
        if msg == "Role is Required":
            self.logger.debug("**** Expected error message matched ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/norole.png")
            self.logger.debug("**** Something went wrong. Expected error did not match ****")
            users.closeBtn()
            assert False


    def test_add_user_nostatus(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.addUser()
        users.fullNames("Osman Osman")
        users.email("osman@pontypriddholdings.com")
        users.phoneNumber("782333346")
        users.jobTitle("Operations")
        users.password("tuesday")
        users.selectRole("Admin")
        users.selectStatus("")
        users.saveBtn()
        time.sleep(3)
        msg = users.errorMessage()
        if msg == "Status is Required":
            self.logger.debug("**** Expected error message matched ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/nostatus.png")
            self.logger.debug("**** Something went wrong. Expected error did not match ****")
            users.closeBtn()
            assert False


    def test_adit_user(self, setup):
        self.driver = setup
        users = Users(self.driver, self.logger)
        users.editBtn()
        users.fullNames("updated")
        users.editSaveBtn()
        time.sleep(3)
        confmsg = users.confirmationMsg()
        if confmsg == "User Updated Successfully":
            self.logger.debug("**** Expected error message matched ****")
            assert True
            users.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/edituser.png")
            self.logger.debug("**** Something went wrong. Expected error did not match ****")
            users.closeBtn()
            assert False



    

