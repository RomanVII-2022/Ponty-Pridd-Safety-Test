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
        self.driver.get(self.base_url)
        login = Login(self.driver, self.logger)
        login.enterEmail("admin@pontypriddholdings.com")
        login.enterPassword("123456")
        login.clickLogin()
        self.logger.debug("**** Login was successful ****")
        time.sleep(3)
        incident = Incident(self.driver, self.logger)
        incident.navIncidents()
        url = self.driver.current_url
        if url == "https://dev.safety.pontypriddholdings.com/incidents":
            assert True
            self.logger.debug("**** Incidents landing page was accessed successfully ****")
        else:
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
        



    