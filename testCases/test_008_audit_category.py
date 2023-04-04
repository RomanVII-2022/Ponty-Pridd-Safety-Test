from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.auditCategoryPage import AuditCategory
import time


class Test_008_Audit_Category:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_add_audit_category(self, setup):
        self.driver = setup
        aCategory = AuditCategory(self.driver, self.logger)
        aCategory.manageBtn()
        aCategory.addBtn()
        aCategory.auditCategory("Management")
        aCategory.auditDescription("Management")
        aCategory.addCategory()
        succ = aCategory.confirmMessage()
        if succ == "Category added successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            aCategory.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditaddcategory.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            aCategory.closeBtn()
            assert False


    def test_existing_audit_category(self, setup):
        self.driver = setup
        aCategory = AuditCategory(self.driver, self.logger)
        aCategory.manageBtn()
        aCategory.addBtn()
        aCategory.auditCategory("Health")
        aCategory.auditDescription("Health")
        aCategory.addCategory()
        err = aCategory.errormsg()
        if err == "Category already exists":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            aCategory.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditexistingcategory.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            aCategory.closeBtn()
            assert False


    def test_noname_audit_category(self, setup):
        self.driver = setup
        aCategory = AuditCategory(self.driver, self.logger)
        aCategory.manageBtn()
        aCategory.addBtn()
        #aCategory.auditCategory("Health")
        aCategory.auditDescription("Health")
        aCategory.addCategory()
        err = aCategory.errormsg()
        if err == "Name is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            aCategory.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnonamecategory.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            aCategory.closeBtn()
            assert False


    def test_nodescription_audit_category(self, setup):
        self.driver = setup
        aCategory = AuditCategory(self.driver, self.logger)
        aCategory.manageBtn()
        aCategory.addBtn()
        aCategory.auditCategory("Health")
        #aCategory.auditDescription("Health")
        aCategory.addCategory()
        err = aCategory.errormsg()
        if err == "Description is required":
            assert True
            self.logger.debug("**** Error message matched the expected error message ****")
            aCategory.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnodescriptioncategory.png")
            self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
            aCategory.closeBtn()
            assert False


    def test_edit_audit_category(self, setup):
        self.driver = setup
        aCategory = AuditCategory(self.driver, self.logger)
        aCategory.editBtn()
        aCategory.editCategory()
        succ = aCategory.confirmMessage()
        if succ == "Category Updated successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            aCategory.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditeditcategory.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            aCategory.closeBtn()
            assert False