from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.auditTypesPage import AuditTypes
import time


class Test_011_Types:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_add_types(self, setup):
        self.driver = setup
        types = AuditTypes(self.driver, self.logger)
        types.typesTab()
        types.addBtn()
        types.nameType("Internal")
        types.descriptionType("Internal")
        types.addType()
        conf = types.confirmMessage()
        if conf == "Type added successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            types.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditaddtypes.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            types.closeBtn()
            assert False


    def test_existing_types(self, setup):
        self.driver = setup
        types = AuditTypes(self.driver, self.logger)
        types.addBtn()
        types.nameType("Internal")
        types.descriptionType("Internal")
        types.addType()
        err = types.errormsg()
        if err == "Audit Type already exists":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            types.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditexistingtypes.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            types.closeBtn()
            assert False


    def test_noname_types(self, setup):
        self.driver = setup
        types = AuditTypes(self.driver, self.logger)
        types.addBtn()
        #types.nameType("Internal")
        types.descriptionType("Internal")
        types.addType()
        err = types.errormsg()
        if err == "Name is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            types.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnonametypes.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            types.closeBtn()
            assert False


    def test_nodescription_types(self, setup):
        self.driver = setup
        types = AuditTypes(self.driver, self.logger)
        types.addBtn()
        types.nameType("Internal")
        #types.descriptionType("Internal")
        types.addType()
        err = types.errormsg()
        if err == "Description is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            types.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnodescriptiontypes.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            types.closeBtn()
            assert False


    def test_edit_types(self, setup):
        self.driver = setup
        types = AuditTypes(self.driver, self.logger)
        types.editBtn()
        types.editType()
        conf = types.confirmMessage()
        if conf == "Type edited successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            types.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditaddtypes.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            types.closeBtn()
            assert False
