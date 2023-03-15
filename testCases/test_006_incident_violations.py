from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.incidentViolationsPage import IncidentTypes
import time


class Test_006_Incident_Violations:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_add_violation(self, setup):
        self.driver = setup
        violations = IncidentTypes(self.driver, self.logger)
        violations.tabVilotation()
        violations.addViolation()
        violations.violationName("Over Speeding Update")
        violations.violationDescription("Over 100km/hr")
        violations.proposedAction("Suspend")
        violations.saveBtn()
        confmsg = violations.confirmMessage()
        if confmsg == "Violation Added Succesfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            violations.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentviolationadd.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            violations.closeBtn()
            assert False
    

    def test_existing_violation(self, setup):
        self.driver = setup
        violations = IncidentTypes(self.driver, self.logger)
        violations.addViolation()
        violations.violationName("Violation")
        violations.violationDescription("Violation Description")
        violations.proposedAction("Exile")
        violations.saveBtn()
        errmsg = violations.errormsg()
        if errmsg == "Request failed with status code 400":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            violations.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentviolationexisting.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            violations.closeBtn()
            assert False


    def test_noname_violation(self, setup):
        self.driver = setup
        violations = IncidentTypes(self.driver, self.logger)
        violations.addViolation()
        violations.violationDescription("Violation Description")
        violations.proposedAction("Exile")
        violations.saveBtn()
        errmsg = violations.errormsg()
        if errmsg == "Name cannot be Empty":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            violations.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentviolationnoname.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            violations.closeBtn()
            assert False


    def test_nodescription_violation(self, setup):
        self.driver = setup
        violations = IncidentTypes(self.driver, self.logger)
        violations.addViolation()
        violations.violationName("Violation")
        violations.proposedAction("Exile")
        violations.saveBtn()
        errmsg = violations.errormsg()
        if errmsg == "Description cannot be Empty":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            violations.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentviolationnodescription.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            violations.closeBtn()
            assert False


    def test_noaction_violation(self, setup):
        self.driver = setup
        violations = IncidentTypes(self.driver, self.logger)
        violations.addViolation()
        violations.violationName("Violation")
        violations.violationDescription("Violation Description")
        violations.saveBtn()
        errmsg = violations.errormsg()
        if errmsg == "Action cannot be Empty":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            violations.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentviolationnoaction.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            violations.closeBtn()
            assert False


    def test_edit_violation(self, setup):
        self.driver = setup
        violations = IncidentTypes(self.driver, self.logger)
        violations.editBtn()
        violations.saveBtn()
        confmsg = violations.confirmMessage()
        if confmsg == "Violation Edited Succesfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            violations.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentviolationadd.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            violations.closeBtn()
            assert False


    
