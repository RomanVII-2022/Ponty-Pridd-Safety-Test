from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Incident:


    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger


    def navIncidents(self):
        try:
            incidentBtn = self.driver.find_element(By.XPATH, "//a[normalize-space()='Incidents']")
            incidentBtn.click()
            self.logger.debug("**** Incidents button on the navigation bar was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Incident button on the navigation bar was not found ****")

    def addBtn(self):
        try:
            Btn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
            Btn.click()
            self.logger.debug("**** Add Incident button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Add incident button was not found ****")


    def vehicleInput(self, plate):
        try:
            vehicle = self.driver.find_element(By.XPATH, "//input[@id='car']")
            vehicle.clear()
            vehicle.send_keys(plate)
            option = self.driver.find_element(By.XPATH, "//div[@class='wrapper'][1]/ul/li[1]")
            option.click()
            self.logger.debug("**** Vehicle was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Vehicle was not entered ****")


    def driverInput(self, name):
        try:
            driver = self.driver.find_element(By.XPATH, "//input[@id='search']")
            driver.clear()
            driver.send_keys(name)
            option = self.driver.find_element(By.XPATH, "//div[@class='wrapper'][2]/ul/li[1]")
            option.click()
            self.logger.debug("**** Driver was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Driver was not entered ****")


    def incidentSelect(self, incidnt):
        try:
            incident = Select(self.driver.find_element(By.XPATH, "//select[@placeholder='Incident']"))
            incident.select_by_visible_text(incidnt)
            self.logger.debug("**** Incident was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Incident was not selected ****")


    def descriptionInput(self, dspt):
        try:
            description = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Description']")
            description.clear()
            description.send_keys(dspt)
            self.logger.debug("**** Description was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Description was not entered ****")

    
    def actionInput(self, act):
        try:
            action = self.driver.find_element(By.XPATH, "//input[@placeholder='Action']")
            action.clear()
            action.send_keys(act)
            self.logger.debug("**** Action was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Action was not entered")


    def locationInput(self, where):
        try:
            location = self.driver.find_element(By.XPATH, "//input[@placeholder='Where']")
            location.clear()
            location.send_keys(where)
            self.logger.debug("**** Location was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Location was not entered ****")


    def violationSelect(self, txt):
        try:
            violation = Select(self.driver.find_element(By.XPATH, "//select[@placeholder='Violation']"))
            violation.select_by_visible_text(txt)
            self.logger.debug("**** Violation was selected successfully. ****")
        except:
            self.logger.debug("**** Something went wrong. Violation was not selected ****")

    def dateInput(self, dt):
        try:
            date = self.driver.find_element(By.XPATH, "//input[@placeholder='Select Date']")
            date.send_keys(dt)
            self.logger.debug("**** Incident date was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Incident date was not entered ****")


    def saveBtn(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//button[@id='close']")
            btn.click()
            self.logger.debug("**** Save and Close button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Save and Close button was not clicked ****")

    def errormsg(self):
        try:
            msg = self.driver.find_element(By.XPATH, "//div[@class='errmsg']")
            return msg.text
        except:
            return "No error"

    def closeBtn(self):
        try:
            closebtn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Close']")
            closebtn.click()
            self.logger.debug("**** Close button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Close button was not clicked ****")


    def confirmMessage(self):
        try:
            confmsg = self.driver.find_element(By.XPATH, "//div[@class='confmsg']")
            return confmsg.text
        except:
            return "No confirmation message"


    def editBtn(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[11]/button")
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