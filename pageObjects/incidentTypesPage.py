from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class IncidentTypes:


    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger


    def typesTab(self):
        try:
            types = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Types'])[1]")
            types.click()
            self.logger.debug("**** Types tab was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Types tab was not clicked ****")


    def addIncidentType(self):
        try:
            addBtn = self.driver.find_element(By.XPATH, "(//button[@class='btn btn-secondary mb-1'][normalize-space()='Add'])[2]")
            addBtn.click()
            self.logger.debug("**** Add Incident Type button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Add Incident Type was not clicked ****")


    def selectCategory(self, category):
        try:
            cat = Select(self.driver.find_element(By.XPATH, "//select[@name='typeCategory']"))
            cat.select_by_visible_text(category)
            self.logger.debug("**** Incident category was selected successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Incident category was not selected ****")


    def typeName(self, name):
        try:
            nameInput = self.driver.find_element(By.XPATH, "//input[@name='typeName']")
            nameInput.send_keys(name)
            self.logger.debug("**** Type name was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Type name was not entered ****")


    def typeDescription(self, description):
        try:
            descriptionInput = self.driver.find_element(By.XPATH, "//input[@name='typeDescription']")
            descriptionInput.send_keys(description)
            self.logger.debug("**** Type description was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Type description was not entered ****")


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
            btn = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/button[1]")
            btn.click()
            self.logger.debug("**** Edit button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Edit button could not be found ****")