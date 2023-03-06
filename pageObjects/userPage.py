from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Users:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger


    def navusers(self):
        try:
            navUsers = self.driver.find_element(By.XPATH, "//a[normalize-space()='Users']")
            navUsers.click()
            self.logger.debug("**** Users button on the navigation bar was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Users on the navigation bar was not found ****")


    def addUser(self):
        try:
            addbtn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
            addbtn.click()
            self.logger.debug("**** User add button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. User add button was not found ****")

    
    def fullNames(self, name):
        try:
            nameInput = self.driver.find_element(By.XPATH, "//input[@placeholder='Names']")
            nameInput.send_keys(name)
            self.logger.debug("**** Full Names were entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Full Names input field was not found ****")


    def email(self, email):
        try:
            emailInput = self.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
            emailInput.clear()
            emailInput.send_keys(email)
            self.logger.debug("**** Email was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Email could not be entered ****")

    def phoneNumber(self, number):
        try:
            numberInput = self.driver.find_element(By.XPATH, "//input[@placeholder='1 (702) 123-4567']")
            numberInput.clear()
            numberInput.send_keys(number)
            self.logger.debug("**** Phone number was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Phone number was not entered. ****")

    def jobTitle(self, title):
        try:
            jobInput = self.driver.find_element(By.XPATH, "//input[@placeholder='e.g hr']")
            jobInput.clear()
            jobInput.send_keys(title)
            self.logger.debug("**** Job title was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Job title was not added ****")


    def password(self, passwrd):
        try:
            passInput = self.driver.find_element(By.XPATH, "//input[@placeholder='password']")
            passInput.clear()
            passInput.send_keys(passwrd)
            self.logger.debug("**** Password was entered sucessfully ****")
        except:
            self.logger.debug("**** Something went wrong. Password was not entered ****")

    
    def selectRole(self, name):
        try:
            role = Select(self.driver.find_element(By.XPATH, "//select[@name='role']"))
            role.select_by_visible_text(name)
            self.logger.debug("**** Role was selected successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Role was not selected ****")


    def selectStatus(self, name):
        try:
            status = Select(self.driver.find_element(By.XPATH, "//select[@name='status']"))
            status.select_by_visible_text(name)
            self.logger.debug("**** Status was selected successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Status was not selected ****")


    def saveBtn(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//button[@id='close']")
            btn.click()
            self.logger.debug("**** Save and Close button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Save and Close button was not clicked ****")


    def errorMessage(self):
        try:
            msg = self.driver.find_element(By.XPATH, "//div[@class='errmsg']").text
            return msg
        except:
            return "No error"


    def closeBtn(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Close']")
            btn.click()
            self.logger.debug("**** Close button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Close button could not be found ****")


    def editBtn(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[9]/button")
            btn.click()
            self.logger.debug("**** Edit button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Edit button could not be found ****")


    def editSaveBtn(self):
        try:
            save = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
            save.click()
            self.logger.debug("**** Save button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Save button was not found ****")


    def confirmationMsg(self):
        try:
            confmsg = self.driver.find_element(By.XPATH, "//div[@class='confmsg']")
            return confmsg.text
        except:
            self.logger.debug("**** Something went wrong. Confirmation message was not found ****")

    
            

