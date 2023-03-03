from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class IncidentCategories:


    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger


    def manageBtn(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Manage']")
            btn.click()
            self.logger.debug("**** Manage button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Manage button could not be found ****")


    def addIncidentCategory(self):
        try:
            addbtn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Incident Category']")
            addbtn.click()
            self.logger.debug("**** Add Incident Category button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Add Incident Button could not be found. ****")


    def categoryName(self, name):
        try:
            nameInput = self.driver.find_element(By.XPATH, "//input[@name='name']")
            nameInput.clear()
            nameInput.send_keys(name)
            self.logger.debug("**** Category name was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Category was not entered ****")


    def categoryDescription(self, description):
        try:
            descr = self.driver.find_element(By.XPATH, "//input[@name='description']")
            descr.clear()
            descr.send_keys(description)
            self.logger.debug("**** Description was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Description was not entered ****")


    def saveBtn(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
            btn.click()
            self.logger.debug("**** Save button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Save button was not clicked ****")


    def closeBtn(self):
        try:
            closebtn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Close']")
            closebtn.click()
            self.logger.debug("**** Close button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Close button was not clicked ****")


    def errormsg(self):
        try:
            msg = self.driver.find_element(By.XPATH, "//div[@class='errmsg']")
            return msg.text
        except:
            return "No error"


    def confirmMessage(self):
        try:
            confmsg = self.driver.find_element(By.XPATH, "//div[@class='confmsg']")
            return confmsg.text
        except:
            return "No confirmation message"


    def editBtn(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[4]/button[1]")
            btn.click()
            self.logger.debug("**** Edit button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Edit button could not be found ****")



