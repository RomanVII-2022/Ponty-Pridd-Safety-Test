from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

class AuditActions:


    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger


    def navAudit(self):
        try:
            audit = self.driver.find_element(By.XPATH, "//a[normalize-space()='Audit']")
            audit.click()
            self.logger.debug("**** Audit button on the navigation bar was clicked ****")
        except:
            self.logger.debug("**** Something went wrong. Audit button on the navigation bar was not clicked ****")


    def viewBtn(self):
        try:
            view = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[10]/button[1]")
            view.click()
            self.logger.debug("**** View button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. View button was not clicked. ****")


    def addAction(self):
        try:
            add = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add Action']")
            add.click()
            self.logger.debug("**** Add action button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Add action button was not clicked ****")

        
    def nameAction(self, name):
        try:
            nameInput = self.driver.find_element(By.XPATH, "//input[@id='actionName']")
            nameInput.clear()
            nameInput.send_keys(name)
            self.logger.debug("**** Action name was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Action name was not entered ****")


    def descriptionAction(self, description):
        try:
            descInput = self.driver.find_element(By.XPATH, "//textarea[@id='actionDescription']")
            descInput.clear()
            descInput.send_keys(description)
            self.logger.debug("**** Description was added successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Description was not entered ****")


    def raisedBy(self, person):
        try:
            inputRaised = self.driver.find_element(By.XPATH, "//input[@id='actionRaisedBy']")
            inputRaised.clear()
            inputRaised.send_keys(person)
            self.logger.debug("**** Raised by was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Raised by was not entered ****")


    def dateRaised(self, date):
        try:
            inputDate = self.driver.find_element(By.XPATH, "//input[@id='actionDateRaised']")
            inputDate.clear()
            inputDate.send_keys(date)
            self.logger.debug("**** Date raised was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Date raised was not entered ****")


    def assignedTo(self, prsn):
        try:
            inputPrsn = self.driver.find_element(By.XPATH, "//input[@id='actionAssignedTo']")
            inputPrsn.clear()
            inputPrsn.send_keys(prsn)
            self.logger.debug("**** Responsible was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Responsible was not entered ****")


    def dateDue(self, date):
        try:
            inputDate = self.driver.find_element(By.XPATH, "//input[@id='actionDueDate']")
            inputDate.clear()
            inputDate.send_keys(date)
            self.logger.debug("**** Date due was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Date due was not entered ****")


    def auditStatus(self, status):
        try:
            inputStatus = Select(self.driver.find_element(By.XPATH, "//select[@id='actionStatus']"))
            inputStatus.select_by_visible_text(status)
            self.logger.debug("**** Audit Status was selected successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Audit Status was not selected ****")


    def saveClose(self):
        try:
            btn = self.driver.find_element(By.XPATH, "//button[@id='submitClose']")
            btn.click()
            self.logger.debug("**** Save and Close button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Save and Close button was not clicked ****")


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
            btn = self.driver.find_element(By.XPATH, "(//button[@type='button'])[2]")
            btn.click()
            self.logger.debug("**** Edit button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Edit button could not be found ****")


    def editSaveBtn(self):
        try:
            savebtn = self.driver.find_element(By.XPATH, "//input[@value='Edit']")
            action = ActionChains(self.driver)
            action.move_to_element(savebtn)
            action.click(savebtn)
            action.perform()
            self.logger.debug("**** Edit button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Edit button was not clicked ****")