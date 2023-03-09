from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.auditsPage import Audit
import time


class Test_003_users:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_add_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.navAudit()
        audit.addBtn()
        audit.auditName("Forex Audit")
        audit.auditDescription("Forex Audit")
        audit.auditType("External")
        audit.orgRequest("EABL")
        audit.auditMeasure("Safety")
        audit.auditCategory("Organization")
        audit.raisedBy("Admin")
        audit.dateRaised("03/08/2023")
        audit.dateDue("03/07/2023")
        audit.assignedTo("User")
        audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        succ = audit.confirmMessage()
        if succ == "Audit Added Successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditadd.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            audit.closeBtn()
            assert False


    def test_noname_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.addBtn()
        audit.auditDescription("Forex Audit")
        audit.auditType("External")
        audit.orgRequest("EABL")
        audit.auditMeasure("Safety")
        audit.auditCategory("Organization")
        audit.raisedBy("Admin")
        audit.dateRaised("03/08/2023")
        audit.dateDue("03/07/2023")
        audit.assignedTo("User")
        audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Audit name is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnoname.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False

    def test_nodescription_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.addBtn()
        audit.auditName("Forex Audit")
        audit.auditType("External")
        audit.orgRequest("EABL")
        audit.auditMeasure("Safety")
        audit.auditCategory("Organization")
        audit.raisedBy("Admin")
        audit.dateRaised("03/08/2023")
        audit.dateDue("03/07/2023")
        audit.assignedTo("User")
        audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Audit description is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnodescription.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_notype_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.addBtn()
        audit.auditName("Forex Audit")
        audit.auditDescription("Forex Audit")
        audit.orgRequest("EABL")
        audit.auditMeasure("Safety")
        audit.auditCategory("Organization")
        audit.raisedBy("Admin")
        audit.dateRaised("03/08/2023")
        audit.dateDue("03/07/2023")
        audit.assignedTo("User")
        audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Audit type is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnotype.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_noorganization_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.addBtn()
        audit.auditName("Forex Audit")
        audit.auditDescription("Forex Audit")
        audit.auditType("External")
        audit.auditMeasure("Safety")
        audit.auditCategory("Organization")
        audit.raisedBy("Admin")
        audit.dateRaised("03/08/2023")
        audit.dateDue("03/07/2023")
        audit.assignedTo("User")
        audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Audit organization is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnoorganization.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_nomeasure_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.addBtn()
        audit.auditName("Forex Audit")
        audit.auditDescription("Forex Audit")
        audit.auditType("External")
        audit.orgRequest("EABL")
        audit.auditCategory("Organization")
        audit.raisedBy("Admin")
        audit.dateRaised("03/08/2023")
        audit.dateDue("03/07/2023")
        audit.assignedTo("User")
        audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Audit measure is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnomeasure.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_nocategory_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.addBtn()
        audit.auditName("Forex Audit")
        audit.auditDescription("Forex Audit")
        audit.auditType("External")
        audit.orgRequest("EABL")
        audit.auditMeasure("Safety")
        #audit.auditCategory("Organization")
        audit.raisedBy("Admin")
        audit.dateRaised("03/08/2023")
        audit.dateDue("03/07/2023")
        audit.assignedTo("User")
        audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Audit category is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnocategory.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_noraisedby_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.addBtn()
        audit.auditName("Forex Audit")
        audit.auditDescription("Forex Audit")
        audit.auditType("External")
        audit.orgRequest("EABL")
        audit.auditMeasure("Safety")
        audit.auditCategory("Organization")
        #audit.raisedBy("Admin")
        audit.dateRaised("03/08/2023")
        audit.dateDue("03/07/2023")
        audit.assignedTo("User")
        audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Audit raised by is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnoraisedby.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_nodateraised_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.addBtn()
        audit.auditName("Forex Audit")
        audit.auditDescription("Forex Audit")
        audit.auditType("External")
        audit.orgRequest("EABL")
        audit.auditMeasure("Safety")
        audit.auditCategory("Organization")
        audit.raisedBy("Admin")
        #audit.dateRaised("03/08/2023")
        audit.dateDue("03/07/2023")
        audit.assignedTo("User")
        audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Audit date is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnodateraised.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_nodatedue_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.addBtn()
        audit.auditName("Forex Audit")
        audit.auditDescription("Forex Audit")
        audit.auditType("External")
        audit.orgRequest("EABL")
        audit.auditMeasure("Safety")
        audit.auditCategory("Organization")
        audit.raisedBy("Admin")
        audit.dateRaised("03/08/2023")
        #audit.dateDue("03/07/2023")
        audit.assignedTo("User")
        audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Audit due date is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnodatedue.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_assignedto_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.addBtn()
        audit.auditName("Forex Audit")
        audit.auditDescription("Forex Audit")
        audit.auditType("External")
        audit.orgRequest("EABL")
        audit.auditMeasure("Safety")
        audit.auditCategory("Organization")
        audit.raisedBy("Admin")
        audit.dateRaised("03/08/2023")
        audit.dateDue("03/07/2023")
        #audit.assignedTo("User")
        audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Audit Assigned to is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnoassignedto.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_nostatus_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.addBtn()
        audit.auditName("Forex Audit")
        audit.auditDescription("Forex Audit")
        audit.auditType("External")
        audit.orgRequest("EABL")
        audit.auditMeasure("Safety")
        audit.auditCategory("Organization")
        audit.raisedBy("Admin")
        audit.dateRaised("03/08/2023")
        audit.dateDue("03/07/2023")
        audit.assignedTo("User")
        #audit.auditStatus("Open")
        audit.auditNote("Noted")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Audit status is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnostatus.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_edit_audit(self, setup):
        self.driver = setup
        audit = Audit(self.driver, self.logger)
        audit.editBtn()
        audit.editSaveBtn()
        conf = audit.confirmMessage()
        if conf == "Audit Updated Successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditedit.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            audit.closeBtn()
            assert False

