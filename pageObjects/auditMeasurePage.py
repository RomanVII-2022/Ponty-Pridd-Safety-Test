from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class AuditMeasure:


    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def measureTab(self):
        try:
            measure = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Measure'])[1]")
            measure.click()
            self.logger.debug("**** Measure tab was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Measure tab was not clicked ****")


    def addBtn(self):
        try:
            add = self.driver.find_element(By.XPATH, "(//button[@class='btn btn-secondary my-1'][normalize-space()='Add'])[2]")
            add.click()
            self.logger.debug("**** Add button was added successfully ****")
        except:
            self.logger.debug("**** Smething went wrong. Add button was not clicked ****")

        
    def measureName(self, name):
        try:
            measure = self.driver.find_element(By.XPATH, "//input[@placeholder='Audit measure']")
            measure.clear()
            measure.send_keys(name)
            self.logger.debug("**** Measure name was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Measure name was not entered ****")


    def measureDescription(self, description):
        try:
            desc = self.driver.find_element(By.XPATH, "//input[@placeholder='Description']")
            desc.clear()
            desc.send_keys(description)
            self.logger.debug("**** Measure description was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Measure description was not entered ****")


    def addMeasure(self):
        try:
            addcategory = self.driver.find_element(By.XPATH, "//input[@value='add']")
            action = ActionChains(self.driver)
            action.move_to_element(addcategory)
            action.click(addcategory)
            action.perform()
            addcategory.click()
            self.logger.debug("**** Add measure button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Add measure button was not clicked ****")

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
            btn = self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/button[1]")
            btn.click()
            self.logger.debug("**** Edit button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Edit button could not be found ****")


    def closeBtn(self):
        try:
            closebtn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Close']")
            closebtn.click()
            self.logger.debug("**** Close button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Close button was not clicked ****")


    def editMeasure(self):
        try:
            editcategory = self.driver.find_element(By.XPATH, "//input[@value='edit']")
            action = ActionChains(self.driver)
            action.move_to_element(editcategory)
            action.click(editcategory)
            action.perform()
            editcategory.click()
            self.logger.debug("**** Edit measure button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Edit measure button was not clicked ****")