from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class IncidentTypes:


    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger


    def tabVilotation(self):
        try:
            violation = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Violations'])[1]")
            violation.click()
            self.logger.debug("**** Violations tab was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Violations tab was not clicked ****")


    def addViolation(self):
        try:
            btn = self.driver.find_element(By.XPATH, "(//button[@class='btn btn-secondary mb-1'][normalize-space()='Add'])[3]")
            btn.click()
            self.logger.debug("**** Add Violation button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Add Violation button was not clicked ****")


    def violationName(self, name):
        try:
            nameInput = self.driver.find_element(By.XPATH, "//input[@name='name']")
            nameInput.clear()
            nameInput.send_keys(name)
            self.logger.debug("**** Violation name was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Violation name was not added ****")


    def violationDescription(self, description):
        try:
            descriptionInput = self.driver.find_element(By.XPATH, "//input[@name='description']")
            descriptionInput.clear()
            descriptionInput.send_keys(description)
            self.logger.debug("**** Description was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Description was not added ****")


    def proposedAction(self, action):
        try:
            actionInput = self.driver.find_element(By.XPATH, "//input[@name='action']")
            actionInput.clear()
            actionInput.send_keys(action)
            self.logger.debug("**** Proposed action was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Proposed action was not entered ****")


    def saveBtn(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
            btn.click()
            self.logger.debug("**** Save button was clicked succcessfully ****")
        except:
            self.logger.debug("**** Something went wrong. Save button was not clicked ****")


    def closeBtn(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Close']")
            btn.click()
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
            btn = self.driver.find_element(By.XPATH, "(//button[@data-toggle='modal'])[5]")
            btn.click()
            self.logger.debug("**** Edit button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Edit button could not be found ****")