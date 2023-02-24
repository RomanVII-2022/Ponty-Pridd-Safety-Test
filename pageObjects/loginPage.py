from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.5, ignored_exceptions=None)

    def enterEmail(self, email):
        try:
            emailInput = self.driver.find_element(By.XPATH, "//input[@placeholder='example@example.com']")
            emailInput.clear()
            emailInput.send_keys(email)
            self.logger.debug("**** Email was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong while entering email ****")


    def enterPassword(self, password):
        try:
            passwordInput = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
            passwordInput.clear()
            passwordInput.send_keys(password)
            self.logger.debug("**** Password was entered successfully ****")
        except:
            self.logger.debug("**** Something went wrong while entering password ****")


    def clickLogin(self):
        try:
            loginBtn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
            loginBtn.click()
            self.logger.debug("**** Login button was clicked successfully ****")
        except:
            self.logger.debug("**** Login button was not found ****")

    def errorMessage(self):
        try:
            err = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='errmsg']")))
            self.logger.debug("**** Error message was found successfully ****")
            return err.text
        except:
            self.logger.debug("**** Error message was not found ****")



        