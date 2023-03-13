from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.auditOrganizationPage import Organization
import time


class Test_010_Organization:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_add_organization(self, setup):
        self.driver = setup
        organization = Organization(self.driver, self.logger)
        organization.tabOrganization()
        organization.addBtn()
        organization.nameOrganization("Quatrix Global")
        organization.descriptionOrganization("Quatrix Global")
        organization.addOrg()
        conf = organization.confirmMessage()
        if conf == "Organization added successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            organization.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditaddorganization.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            organization.closeBtn()
            assert False


    def test_existing_organization(self, setup):
        self.driver = setup
        organization = Organization(self.driver, self.logger)
        organization.addBtn()
        organization.nameOrganization("EABL")
        organization.descriptionOrganization("EABL")
        organization.addOrg()
        err = organization.errormsg()
        if err == "Organization already exists":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            organization.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditexistingorganization.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            organization.closeBtn()
            assert False


    def test_noname_organization(self, setup):
        self.driver = setup
        organization = Organization(self.driver, self.logger)
        organization.addBtn()
        #organization.nameOrganization("Quatrix Global")
        organization.descriptionOrganization("Quatrix Global")
        organization.addOrg()
        err = organization.errormsg()
        if err == "Name is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            organization.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnonameorganization.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            organization.closeBtn()
            assert False


    def test_nodescription_organization(self, setup):
        self.driver = setup
        organization = Organization(self.driver, self.logger)
        organization.addBtn()
        organization.nameOrganization("Quatrix Global")
        #organization.descriptionOrganization("Quatrix Global")
        organization.addOrg()
        err = organization.errormsg()
        if err == "Description is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            organization.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnodescriptionorganization.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            organization.closeBtn()
            assert False


    def test_edit_organization(self, setup):
        self.driver = setup
        organization = Organization(self.driver, self.logger)
        organization.editBtn()
        organization.editOrg()
        conf = organization.confirmMessage()
        if conf == "Organization edited successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            organization.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditeditorganization.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            organization.closeBtn()
            assert False
