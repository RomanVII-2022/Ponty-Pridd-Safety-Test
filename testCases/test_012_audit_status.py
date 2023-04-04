from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.auditStatusPage import AuditStatus
import time


class Test_012_status:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_add_status(self, setup):
        self.driver = setup
        status = AuditStatus(self.driver, self.logger)
        status.statusTab()
        status.addBtn()
        status.nameStatus("Revised")
        status.descriptionStatus("Revised")
        status.addStatus()
        conf = status.confirmMessage()
        if conf == "Status added successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            status.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditaddstatus.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            status.closeBtn()
            assert False


    def test_existing_status(self, setup):
        self.driver = setup
        status = AuditStatus(self.driver, self.logger)
        status.addBtn()
        status.nameStatus("Revised")
        status.descriptionStatus("Revised")
        status.addStatus()
        err = status.errormsg()
        if err == "Audit Status already exists":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            status.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditexistingstatus.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            status.closeBtn()
            assert False


    def test_noname_status(self, setup):
        self.driver = setup
        status = AuditStatus(self.driver, self.logger)
        status.addBtn()
        #status.nameStatus("Revised")
        status.descriptionStatus("Revised")
        status.addStatus()
        err = status.errormsg()
        if err == "Name is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            status.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnonamestatus.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            status.closeBtn()
            assert False


    def test_nodescription_status(self, setup):
        self.driver = setup
        status = AuditStatus(self.driver, self.logger)
        status.addBtn()
        status.nameStatus("Revised")
        #status.descriptionStatus("Revised")
        status.addStatus()
        err = status.errormsg()
        if err == "Description is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            status.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnodescstatus.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            status.closeBtn()
            assert False


    def test_edit_status(self, setup):
        self.driver = setup
        status = AuditStatus(self.driver, self.logger)
        status.editBtn()
        status.editStatus()
        conf = status.confirmMessage()
        if conf == "Status Updated successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            status.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditeditstatus.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            status.closeBtn()
            assert False