import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.form_page import FormPage
from utils.driver_setup import setup_driver

@pytest.fixture
def driver():
    driver = setup_driver()
    yield driver
    driver.quit()

def test_form_submission(driver):
    form_page = FormPage(driver)
    driver.get("https://demoqa.com/automation-practice-form")
    image_path = os.path.abspath('resources/1.jpg')

    form_page.fill_form(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        gender="Male",
        phone_number="1234567890",
        subjects="Math",
        hobbies=["Reading", "Music"],
        image_path=image_path,
        current_address="123 Main St"
    )

    form_page.submit_form()

    assert "Thanks for submitting the form" in driver.page_source
