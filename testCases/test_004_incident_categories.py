from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.incidentCategoriesPage import IncidentCategories
from pageObjects.incidentsPage import Incident
import time


class Test_004_Incident_Category:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_add_incident_category(self, setup):
        self.driver = setup
        categories = IncidentCategories(self.driver, self.logger)
        categories.manageBtn()
        categories.addIncidentCategory()
        categories.categoryName("Stealing")
        categories.categoryDescription("Stealing Description")
        categories.saveBtn()
        confmsg = categories.confirmMessage()
        if confmsg == "Category Added Successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected message ****")
            categories.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentcategoryadd.png")
            self.logger.debug("**** Something went wrong. Corfimation message did not match the expected confirmation message ****")
            categories.closeBtn()
            assert False

    def test_existing_incident_category(self, setup):
        self.driver = setup
        categories = IncidentCategories(self.driver, self.logger)
        categories.addIncidentCategory()
        categories.categoryName("Stealing")
        categories.categoryDescription("Stealing Description")
        categories.saveBtn()
        errmsg = categories.errormsg()
        if errmsg == "Category already exists":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            categories.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentcategoryexisting.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            categories.closeBtn()
            assert False


    def test_noname_incident_category(self, setup):
        self.driver = setup
        categories = IncidentCategories(self.driver, self.logger)
        categories.addIncidentCategory()
        categories.categoryDescription("Stealing Description")
        categories.saveBtn()
        errmsg = categories.errormsg()
        print(errmsg)
        if errmsg == "Category Name cannot be Empty":
            assert True
            self.logger.debug("**** Confirmation message matched the expected message ****")
            categories.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentcategorynoname.png")
            self.logger.debug("**** Something went wrong. Corfimation message did not match the expected confirmation message ****")
            categories.closeBtn()
            assert False


    def test_nodescription_incident_category(self, setup):
        self.driver = setup
        categories = IncidentCategories(self.driver, self.logger)
        categories.addIncidentCategory()
        categories.categoryName("Stealing")
        categories.saveBtn()
        errmsg = categories.errormsg()
        if errmsg == "Category Description cannot be Empty":
            assert True
            self.logger.debug("**** Confirmation message matched the expected message ****")
            categories.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentcategorynodescription.png")
            self.logger.debug("**** Something went wrong. Corfimation message did not match the expected confirmation message ****")
            categories.closeBtn()
            assert False


    def test_edit_incident_category(self, setup):
        self.driver = setup
        categories = IncidentCategories(self.driver, self.logger)
        categories.editBtn()
        categories.saveBtn()
        confmsg = categories.confirmMessage()
        if confmsg == "Incident Category Updated Successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected message ****")
            categories.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentcategoryedit.png")
            self.logger.debug("**** Something went wrong. Corfimation message did not match the expected confirmation message ****")
            categories.closeBtn()
            assert False

    

