from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.auditActionPage import AuditActions
import time


class Test_013_action:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()


    def test_add_action(self, setup):
        self.driver = setup
        audit = AuditActions(self.driver, self.logger)
        audit.navAudit()
        audit.viewBtn()
        audit.addAction()
        audit.nameAction('Escalated to KBL')
        audit.descriptionAction('Escalated to KBL and 5why done by Pontypridd')
        audit.raisedBy("EABL")
        audit.dateRaised("03/21/2023")
        audit.assignedTo("Pontypridd")
        audit.dateDue("03/22/2023")
        audit.auditStatus("Open")
        audit.saveClose()
        succ = audit.confirmMessage()
        if succ == "Action Added Successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/actionadd.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            audit.closeBtn()
            assert False


    def test_existing_action(self, setup):
        self.driver = setup
        audit = AuditActions(self.driver, self.logger)
        audit.addAction()
        audit.nameAction('Escalated to KBL')
        audit.descriptionAction('Escalated to KBL and 5why done by Pontypridd')
        audit.raisedBy("EABL")
        audit.dateRaised("03/21/2023")
        audit.assignedTo("Pontypridd")
        audit.dateDue("03/22/2023")
        audit.auditStatus("Open")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Action already exists":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/actionexisting.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_noname_action(self, setup):
        self.driver = setup
        audit = AuditActions(self.driver, self.logger)
        audit.addAction()
        #audit.nameAction('Escalated to KBL')
        audit.descriptionAction('Escalated to KBL and 5why done by Pontypridd')
        audit.raisedBy("EABL")
        audit.dateRaised("03/21/2023")
        audit.assignedTo("Pontypridd")
        audit.dateDue("03/22/2023")
        audit.auditStatus("Open")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Action name is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/actionnoname.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_nodescription_action(self, setup):
        self.driver = setup
        audit = AuditActions(self.driver, self.logger)
        audit.addAction()
        audit.nameAction('Escalated to KBL')
        #audit.descriptionAction('Escalated to KBL and 5why done by Pontypridd')
        audit.raisedBy("EABL")
        audit.dateRaised("03/21/2023")
        audit.assignedTo("Pontypridd")
        audit.dateDue("03/22/2023")
        audit.auditStatus("Open")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Description is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/actionnodescription.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_noraisedby_action(self, setup):
        self.driver = setup
        audit = AuditActions(self.driver, self.logger)
        audit.addAction()
        audit.nameAction('Escalated to KBL')
        audit.descriptionAction('Escalated to KBL and 5why done by Pontypridd')
        #audit.raisedBy("EABL")
        audit.dateRaised("03/21/2023")
        audit.assignedTo("Pontypridd")
        audit.dateDue("03/22/2023")
        audit.auditStatus("Open")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Raised by is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/actionnoraisedby.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_nodateraised_action(self, setup):
        self.driver = setup
        audit = AuditActions(self.driver, self.logger)
        audit.addAction()
        audit.nameAction('Escalated to KBL')
        audit.descriptionAction('Escalated to KBL and 5why done by Pontypridd')
        audit.raisedBy("EABL")
        #audit.dateRaised("03/21/2023")
        audit.assignedTo("Pontypridd")
        audit.dateDue("03/22/2023")
        audit.auditStatus("Open")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Date raised is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/actionnodateraised.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_noresponsible_action(self, setup):
        self.driver = setup
        audit = AuditActions(self.driver, self.logger)
        audit.addAction()
        audit.nameAction('Escalated to KBL')
        audit.descriptionAction('Escalated to KBL and 5why done by Pontypridd')
        audit.raisedBy("EABL")
        audit.dateRaised("03/21/2023")
        #audit.assignedTo("Pontypridd")
        audit.dateDue("03/22/2023")
        audit.auditStatus("Open")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Assigned to is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/actionnoresponsible.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_noduedate_action(self, setup):
        self.driver = setup
        audit = AuditActions(self.driver, self.logger)
        audit.addAction()
        audit.nameAction('Escalated to KBL')
        audit.descriptionAction('Escalated to KBL and 5why done by Pontypridd')
        audit.raisedBy("EABL")
        audit.dateRaised("03/21/2023")
        audit.assignedTo("Pontypridd")
        #audit.dateDue("03/22/2023")
        audit.auditStatus("Open")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Due date is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/actionnoduedate.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_nostatus_action(self, setup):
        self.driver = setup
        audit = AuditActions(self.driver, self.logger)
        audit.addAction()
        audit.nameAction('Escalated to KBL')
        audit.descriptionAction('Escalated to KBL and 5why done by Pontypridd')
        audit.raisedBy("EABL")
        audit.dateRaised("03/21/2023")
        audit.assignedTo("Pontypridd")
        audit.dateDue("03/22/2023")
        #audit.auditStatus("Open")
        audit.saveClose()
        err = audit.errormsg()
        if err == "Status is required is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/actionnostatus.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            audit.closeBtn()
            assert False


    def test_edit_action(self, setup):
        self.driver = setup
        audit = AuditActions(self.driver, self.logger)
        audit.editBtn()
        audit.editSaveBtn()
        succ = audit.confirmMessage()
        if succ == "Action Edited Successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            audit.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/actionedit.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            audit.closeBtn()
            assert False