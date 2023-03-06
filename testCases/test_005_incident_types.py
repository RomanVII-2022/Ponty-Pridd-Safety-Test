from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.incidentTypesPage import IncidentTypes
import time


class Test_003_users:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_add_incident_type(self, setup):
        self.driver = setup
        types = IncidentTypes(self.driver, self.logger)
        types.typesTab()
        types.addIncidentType()
        types.selectCategory("Security")
        types.typeName("Security Issue")
        types.typeDescription("Security Issues")
        types.saveBtn()
        confmsg = types.confirmMessage()
        errmsg = types.errormsg()
        if confmsg == "Incident Type Added Successfully" or errmsg == "Incident type already exists":
            assert True
            self.logger.debug("**** Confirmation message matched the expected message ****")
            types.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidenttypeadd.png")
            self.logger.debug("**** Something went wrong. Corfimation message did not match the expected confirmation message ****")
            types.closeBtn()
            assert False

    def test_existing_incident_type(self, setup):
        self.driver = setup
        types = IncidentTypes(self.driver, self.logger)
        types.addIncidentType()
        types.selectCategory("Security")
        types.typeName("Security Issue")
        types.typeDescription("Security Issues")
        types.saveBtn()
        errmsg = types.errormsg()
        if errmsg == "Incident type already exists":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            types.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidenttypeexisting.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            types.closeBtn()
            assert False


    def test_nocategory_incident_type(self, setup):
        self.driver = setup
        types = IncidentTypes(self.driver, self.logger)
        types.addIncidentType()
        types.typeName("Security Issue")
        types.typeDescription("Security Issues")
        types.saveBtn()
        errmsg = types.errormsg()
        if errmsg == "Category is Required":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            types.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidenttypenocategory.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            types.closeBtn()
            assert False


    def test_noname_incident_type(self, setup):
        self.driver = setup
        types = IncidentTypes(self.driver, self.logger)
        types.addIncidentType()
        types.selectCategory("Security")
        types.typeDescription("Security Issues")
        types.saveBtn()
        errmsg = types.errormsg()
        if errmsg == "Name cannot be Empty":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            types.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidenttypenoname.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            types.closeBtn()
            assert False


    def test_nodescription_incident_type(self, setup):
        self.driver = setup
        types = IncidentTypes(self.driver, self.logger)
        types.addIncidentType()
        types.selectCategory("Security")
        types.typeName("Security Issue")
        types.saveBtn()
        errmsg = types.errormsg()
        if errmsg == "Description cannot be Empty":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            types.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidenttypenodescription.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            types.closeBtn()
            assert False


    def test_edit_incident_type(self, setup):
        self.driver = setup
        types = IncidentTypes(self.driver, self.logger)
        types.editBtn()
        types.saveBtn()
        confmsg = types.confirmMessage()
        if confmsg == "Incident Type Updated Successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected message ****")
            types.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidenttypeedit.png")
            self.logger.debug("**** Something went wrong. Corfimation message did not match the expected confirmation message ****")
            types.closeBtn()
            assert False


