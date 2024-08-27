import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, email, gender, phone_number, subjects, hobbies, image_path, current_address):
        self.driver.find_element(By.XPATH, '//input[@id="firstName"]').send_keys(first_name)
        self.driver.find_element(By.XPATH, '//input[@id="lastName"]').send_keys(last_name)
        self.driver.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys(email)

        gender_xpath = {
            "Male": '//*[@id="genterWrapper"]/div[2]/div[1]',
            "Female": '//*[@id="genterWrapper"]/div[2]/div[2]',
            "Other": '//*[@id="genterWrapper"]/div[2]/div[3]',
        }
        self.driver.find_element(By.XPATH, gender_xpath[gender]).click()

        self.driver.find_element(By.XPATH, '//input[@id="userNumber"]').send_keys(phone_number)

        subject_input = self.wait.until(EC.element_to_be_clickable((By.ID, 'subjectsInput')))
        subject_input.send_keys(subjects)
        subject_input.send_keys(Keys.RETURN) 

        for hobby in hobbies:
            hobby_xpath = {
                "Sports": '//*[@id="hobbiesWrapper"]/div[2]/div[1]/label',
                "Reading": '//*[@id="hobbiesWrapper"]/div[2]/div[2]/label',
                "Music": '//*[@id="hobbiesWrapper"]/div[2]/div[3]/label',
            }
            hobby_element = self.driver.find_element(By.XPATH, hobby_xpath[hobby])

            self.driver.execute_script("arguments[0].scrollIntoView();", hobby_element)
            self.driver.execute_script("arguments[0].click();", hobby_element)

        self.driver.find_element(By.ID, 'uploadPicture').send_keys(image_path)

        self.driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]').send_keys(current_address)

    def submit_form(self):
        submit_button = self.driver.find_element(By.ID, 'submit')
        self.driver.execute_script("arguments[0].click();", submit_button)
