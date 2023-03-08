from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Audit:


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


    def addBtn(self):
        try:
            add = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
            add.click()
            self.logger.debug("**** Add button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Add button was not clicked ****")


    def auditName(self, name):
        try:
            inputName = self.driver.find_element(By.XPATH, "//input[@id='auditName']")
            inputName.clear()
            inputName.send_keys(name)
            self.logger.debug("**** Audit name was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Audit name was not entered ****")


    def auditDescription(self, description):
        try:
            inputDescription = self.driver.find_element(By.XPATH, "//textarea[@id='auditDescription']")
            inputDescription.clear()
            inputDescription.send_keys(description)
            self.logger.debug("**** Audit description was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Audit description was not entered ****")


    def auditType(self, type):
        try:
            audType = Select(self.driver.find_element(By.XPATH, "//select[@id='auditType']"))
            audType.select_by_visible_text(type)
            self.logger.debug("**** Audit type was selected successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Audit type was not selected ****")


    def orgRequest(self, org):
        try:
            reqst = Select(self.driver.find_element(By.XPATH, "//select[@id='organizationRequiringAudit']"))
            reqst.select_by_visible_text(org)
            self.logger.debug("**** Organization requesting audit was selected successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Organization requesting audit was not selected ****")


    def auditMeasure(self, measure):
        try:
            aMesaure = Select(self.driver.find_element(By.XPATH, "//select[@id='auditMeasure']"))
            aMesaure.select_by_visible_text(measure)
            self.logger.debug("**** Audit Measure was selected successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Audit Measure was not selected ****")


    def auditCategory(self, category):
        try:
            aCategory = Select(self.driver.find_element(By.XPATH, "//select[@id='auditCategory']"))
            aCategory.select_by_visible_text(category)
            self.logger.debug("**** Audit Category was selected successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Audit Category was not selected ****")


    def raisedBy(self, person):
        try:
            inputRaised = self.driver.find_element(By.XPATH, "//input[@id='auditRaisedBy']")
            inputRaised.clear()
            inputRaised.send_keys(person)
            self.logger.debug("**** Raised by was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Raised by was not entered ****")


    def dateRaised(self, date):
        try:
            inputDate = self.driver.find_element(By.XPATH, "//input[@id='auditDate']")
            inputDate.clear()
            inputDate.send_keys(date)
            self.logger.debug("**** Date raised was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Date raised was not entered ****")


    def dateDue(self, date):
        try:
            inputDate = self.driver.find_element(By.XPATH, "//input[@id='auditDueDate']")
            inputDate.clear()
            inputDate.send_keys(date)
            self.logger.debug("**** Date due was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Date due was not entered ****")


    def assignedTo(self, prsn):
        try:
            inputPrsn = self.driver.find_element(By.XPATH, "//input[@id='auditAssignedTo']")
            inputPrsn.clear()
            inputPrsn.send_keys(prsn)
            self.logger.debug("**** Assigned to was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Assigned to was not entered ****")


    def auditStatus(self, status):
        try:
            inputStatus = Select(self.driver.find_element(By.XPATH, "//select[@id='auditStatus']"))
            inputStatus.select_by_visible_text(status)
            self.logger.debug("**** Audit Status was selected successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Audit Status was not selected ****")


    def auditNote(self, note):
        try:
            inputNote = self.driver.find_element(By.XPATH, "//textarea[@id='auditNotes']")
            inputNote.clear()
            inputNote.send_keys(note)
            self.logger.debug("**** Audit note was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Audit note was not entered ****")


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
            btn = self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[11]/button[1]")
            btn.click()
            self.logger.debug("**** Edit button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Edit button could not be found ****")


    def editSaveBtn(self):
        try:
            save = self.driver.find_element(By.XPATH, "//input[@value='update']")
            save.click()
            self.logger.debug("**** Update button was clicked successfully ****")
        except:
            self.logger.debug("**** Something went wrong. Update button was not clicked ****")



    


    


    


    