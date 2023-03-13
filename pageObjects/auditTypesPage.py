from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class AuditTypes:


    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger


    def typesTab(self):
        try:
            types = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Types'])[1]")
            types.click()
            self.logger.debug("**** Types tab button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Types tab was not clicked ****")


    def addBtn(self):
        try:
            add = self.driver.find_element(By.XPATH, "(//button[@class='btn btn-warning my-2'][normalize-space()='Add'])[4]")
            add.click()
            self.logger.debug("**** Add button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Add button was not clicked ****")


    def nameType(self, name):
        try:
            nameInput = self.driver.find_element(By.XPATH, "//input[@placeholder='Audit type']")
            nameInput.clear()
            nameInput.send_keys(name)
            self.logger.debug("**** Type name was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Type name was not added ****")


    def descriptionType(self, description):
        try:
            descInput = self.driver.find_element(By.XPATH, "//input[@placeholder='Description']")
            descInput.clear()
            descInput.send_keys(description)
            self.logger.debug("**** Description was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Description was not entered ****")


    def addType(self):
        try:
            addcategory = self.driver.find_element(By.XPATH, "//input[@value='add']")
            action = ActionChains(self.driver)
            action.move_to_element(addcategory)
            action.click(addcategory)
            action.perform()
            addcategory.click()
            self.logger.debug("**** Add type button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Add type button was not clicked ****")

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
            btn = self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/button[1]")
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


    def editType(self):
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
