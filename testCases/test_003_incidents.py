from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.loginPage import Login
from pageObjects.incidentsPage import Incident
import time


class Test_003_users:
    base_url = ReadConfig.get_app_url()
    logger = LogGen().log_gen()

    def test_incidents_landing_page(self, setup):
        self.driver = setup
        # self.driver.get(self.base_url)
        # login = Login(self.driver, self.logger)
        # login.enterEmail("admin@pontypriddholdings.com")
        # login.enterPassword("123456")
        # login.clickLogin()
        # self.logger.debug("**** Login was successful ****")
        #time.sleep(3)
        incident = Incident(self.driver, self.logger)
        incident.navIncidents()
        url = self.driver.current_url
        if url == "https://dev.safety.pontypriddholdings.com/incidents":
            assert True
            self.logger.debug("**** Incidents landing page was accessed successfully ****")
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentslandingpage.png")
            self.logger.debug("**** Something went wrong. Incidents landing page was not accessed ****")
            assert False

    def test_add_incident(self, setup):
        self.driver = setup
        incident = Incident(self.driver, self.logger)
        incident.addBtn()
        incident.vehicleInput("KAA293B")
        incident.driverInput("Francis Muniu")
        incident.incidentSelect("Fraud")
        incident.descriptionInput("Anything")
        incident.actionInput("Suspend")
        incident.locationInput("Nairobi")
        incident.violationSelect("PPE")
        incident.dateInput("03/02/2023")
        incident.saveBtn()
        confmsg = incident.confirmMessage()
        errmsg = incident.errormsg()
        if confmsg == "Incident Added Successfully" or errmsg == "Incident Already Exists":
            assert True
            self.logger.debug("**** Confirmation message matched the expected message ****")
            incident.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/addincident.png")
            self.logger.debug("**** Something went wrong. Corfimation message did not match the expected confirmation message ****")
            incident.closeBtn()
            assert False
        

    def test_missing_vehicle(self, setup):
        self.driver = setup
        incident = Incident(self.driver, self.logger)
        incident.addBtn()
        incident.driverInput("Francis Muniu")
        incident.incidentSelect("Fraud")
        incident.descriptionInput("Anything")
        incident.actionInput("Suspend")
        incident.locationInput("Nairobi")
        incident.violationSelect("PPE")
        incident.dateInput("03/02/2023")
        incident.saveBtn()
        errmsg = incident.errormsg()
        if errmsg == "Select vehicle from List":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            incident.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentmissingvehicle.png")
            self.logger.debug("**** Something went wrong. Error message did not match with the expected error ****")
            incident.closeBtn()
            assert False


    def test_missing_driver(self, setup):
        self.driver = setup
        incident = Incident(self.driver, self.logger)
        incident.addBtn()
        incident.vehicleInput("KAA293B")
        incident.incidentSelect("Fraud")
        incident.descriptionInput("Anything")
        incident.actionInput("Suspend")
        incident.locationInput("Nairobi")
        incident.violationSelect("PPE")
        incident.dateInput("03/02/2023")
        incident.saveBtn()
        errmsg = incident.errormsg()
        if errmsg == "Select Driver from List":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            incident.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentmissingdriver.png")
            self.logger.debug("**** Something went wrong. Error message did not match with the expected error ****")
            incident.closeBtn()
            assert False


    def test_missing_incident(self, setup):
        self.driver = setup
        incident = Incident(self.driver, self.logger)
        incident.addBtn()
        incident.vehicleInput("KAA293B")
        incident.driverInput("Francis Muniu")
        incident.descriptionInput("Anything")
        incident.actionInput("Suspend")
        incident.locationInput("Nairobi")
        incident.violationSelect("PPE")
        incident.dateInput("03/02/2023")
        incident.saveBtn()
        errmsg = incident.errormsg()
        if errmsg == "Incident cannot be Empty":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            incident.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentmissingincident.png")
            self.logger.debug("**** Something went wrong. Error message did not match with the expected error ****")
            incident.closeBtn()
            assert False


    def test_missing_description(self, setup):
        self.driver = setup
        incident = Incident(self.driver, self.logger)
        incident.addBtn()
        incident.vehicleInput("KAA293B")
        incident.driverInput("Francis Muniu")
        incident.incidentSelect("Fraud")
        incident.actionInput("Suspend")
        incident.locationInput("Nairobi")
        incident.violationSelect("PPE")
        incident.dateInput("03/02/2023")
        incident.saveBtn()
        errmsg = incident.errormsg()
        if errmsg == "Description cannot be Empty":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            incident.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentmissingdescription.png")
            self.logger.debug("**** Something went wrong. Error message did not match with the expected error ****")
            incident.closeBtn()
            assert False


    def test_missing_action(self, setup):
        self.driver = setup
        incident = Incident(self.driver, self.logger)
        incident.addBtn()
        incident.vehicleInput("KAA293B")
        incident.driverInput("Francis Muniu")
        incident.incidentSelect("Fraud")
        incident.descriptionInput("Anything")
        incident.locationInput("Nairobi")
        incident.violationSelect("PPE")
        incident.dateInput("03/02/2023")
        incident.saveBtn()
        errmsg = incident.errormsg()
        if errmsg == "Action cannot be Empty":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            incident.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentmissingaction.png")
            self.logger.debug("**** Something went wrong. Error message did not match with the expected error ****")
            incident.closeBtn()
            assert False


    def test_missing_location(self, setup):
        self.driver = setup
        incident = Incident(self.driver, self.logger)
        incident.addBtn()
        incident.vehicleInput("KAA293B")
        incident.driverInput("Francis Muniu")
        incident.incidentSelect("Fraud")
        incident.descriptionInput("Anything")
        incident.actionInput("Suspend")
        incident.violationSelect("PPE")
        incident.dateInput("03/02/2023")
        incident.saveBtn()
        errmsg = incident.errormsg()
        if errmsg == "Location cannot be Empty":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            incident.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentmissinglocation.png")
            self.logger.debug("**** Something went wrong. Error message did not match with the expected error ****")
            incident.closeBtn()
            assert False


    def test_missing_violation(self, setup):
        self.driver = setup
        incident = Incident(self.driver, self.logger)
        incident.addBtn()
        incident.vehicleInput("KAA293B")
        incident.driverInput("Francis Muniu")
        incident.incidentSelect("Fraud")
        incident.descriptionInput("Anything")
        incident.actionInput("Suspend")
        incident.locationInput("Nairobi")
        incident.dateInput("03/02/2023")
        incident.saveBtn()
        errmsg = incident.errormsg()
        confmsg = incident.confirmMessage()
        if confmsg == "Incident Added Successfully" or errmsg == "Incident Already Exists":
            assert True
            self.logger.debug("**** Confirmation message matched the expected message ****")
            incident.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentmissingviolation.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match with the expected error ****")
            incident.closeBtn()
            assert False


    def test_missing_date(self, setup):
        self.driver = setup
        incident = Incident(self.driver, self.logger)
        incident.addBtn()
        incident.vehicleInput("KAA293B")
        incident.driverInput("Francis Muniu")
        incident.incidentSelect("Fraud")
        incident.descriptionInput("Anything")
        incident.actionInput("Suspend")
        incident.locationInput("Nairobi")
        incident.violationSelect("PPE")
        incident.saveBtn()
        errmsg = incident.errormsg()
        if errmsg == "Date cannot be Empty":
            assert True
            self.logger.debug("**** Error message matched the expected message ****")
            incident.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentmissingdate.png")
            self.logger.debug("**** Something went wrong. Error message did not match with the expected error ****")
            incident.closeBtn()
            assert False


    def test_edit_incident(self, setup):
        self.driver = setup
        incident = Incident(self.driver, self.logger)
        incident.editBtn()
        incident.actionInput("Suspend edited")
        incident.locationInput("Nairobi edited")
        incident.editSaveBtn()
        confmsg = incident.confirmMessage()
        if confmsg == "Incident Updated Successfully":
            assert True
            self.logger.debug("**** Confirmation message matched the expected message ****")
            incident.closeBtn()
        else:
            self.driver.save_screenshot("/home/vmwai/Documents/tests/PontySafety/screenshots/incidentedit.png")
            self.logger.debug("**** Something went wrong. Confirmation message did not match with the expected error ****")
            incident.closeBtn()
            assert False



    




    