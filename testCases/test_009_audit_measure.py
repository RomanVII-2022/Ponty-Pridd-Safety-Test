from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.auditMeasurePage import AuditMeasure
import time


class Test_009_AuditMeasure:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_add_audit_measure(self, setup):
        self.driver = setup
        measure = AuditMeasure(self.driver, self.logger)
        measure.measureTab()
        measure.addBtn()
        measure.measureName("Measure")
        measure.measureDescription("Description")
        time.sleep(3)
        measure.addMeasure()
        conf = measure.confirmMessage()
        if conf == "Measure added successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
            measure.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditaddmeasure.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
            measure.closeBtn()
            assert False


    # def test_existing_audit_measure(self, setup):
    #     self.driver = setup
    #     measure = AuditMeasure(self.driver, self.logger)
    #     measure.addBtn()
    #     measure.measureName("Measure")
    #     measure.measureDescription("Description")
    #     measure.addMeasure()
    #     err = measure.errormsg()
    #     if err == "Measure already exists":
    #         assert True
    #         self.logger.debug("**** Error message matched the expected error message ****")
    #         measure.closeBtn()
    #     else:
    #         self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditexistingmeasure.png")
    #         self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
    #         measure.closeBtn()
    #         assert False


    # def test_noname_audit_measure(self, setup):
    #     self.driver = setup
    #     measure = AuditMeasure(self.driver, self.logger)
    #     measure.addBtn()
    #     #measure.measureName("Measure")
    #     measure.measureDescription("Description")
    #     measure.addMeasure()
    #     err = measure.errormsg()
    #     if err == "Name is required":
    #         assert True
    #         self.logger.debug("**** Error message matched the expected error message ****")
    #         measure.closeBtn()
    #     else:
    #         self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnonamemeasure.png")
    #         self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
    #         measure.closeBtn()
    #         assert False


    # def test_nodescription_audit_measure(self, setup):
    #     self.driver = setup
    #     measure = AuditMeasure(self.driver, self.logger)
    #     measure.addBtn()
    #     measure.measureName("Measure")
    #     #measure.measureDescription("Description")
    #     measure.addMeasure()
    #     err = measure.errormsg()
    #     if err == "Description is required":
    #         assert True
    #         self.logger.debug("**** Error message matched the expected error message ****")
    #         measure.closeBtn()
    #     else:
    #         self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditnodescriptionmeasure.png")
    #         self.logger.debug("**** Something went wrong. Error message did not match the expected error message ****")
    #         measure.closeBtn()
    #         assert False


    # def test_edit_audit_measure(self, setup):
    #     self.driver = setup
    #     measure = AuditMeasure(self.driver, self.logger)
    #     measure.editBtn()
    #     measure.editMeasure()
    #     conf = measure.confirmMessage()
    #     if conf == "Measure edited successfully":
    #         assert True
    #         self.logger.debug("**** Confirmation message matched the expected confirmation message ****")
    #         measure.closeBtn()
    #     else:
    #         self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/auditeditmeasure.png")
    #         self.logger.debug("**** Something went wrong. Confirmation message did not match the expected confirmation message ****")
    #         measure.closeBtn()
    #         assert False


    

