from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time


class Users:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # def __init__(self, driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)):
    #     self.driver = driver

    def login(self):
        self.driver.get("https://dev.safety.pontypriddholdings.com/")
        self.driver.maximize_window()
        emailInput = self.driver.find_element(By.XPATH, "//input[@placeholder='example@example.com']")
        emailInput.clear()
        emailInput.send_keys("admin@pontypriddholdings.com")
        passwordInput = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        passwordInput.clear()
        passwordInput.send_keys("123456")
        loginBtn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        loginBtn.click()
        time.sleep(5)

    def adduser(self):
        navuser = self.driver.find_element(By.XPATH, "//a[normalize-space()='Users']")
        navuser.click()
        addbtn = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
        addbtn.click()


users = Users()
users.adduser()