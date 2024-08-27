from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find_element(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def find_elements(self, by, value):
        return self.wait.until(EC.visibility_of_all_elements_located((by, value)))
