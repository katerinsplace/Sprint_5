import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from data import Urls
from locators import *
from helpers import new_email_password

@pytest.fixture
def driver():
    result = webdriver.Chrome()
    result.get(Urls.QA_DESK)
    yield result
    result.quit()

@pytest.fixture(scope='session')
def create_new_user():
    driver = webdriver.Chrome()
    driver.get(Urls.QA_DESK)

    driver.find_element(*REG_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(NO_ACC_BUTTON))
    driver.find_element(*NO_ACC_BUTTON).click()

    email, password = new_email_password()
    driver.find_element(*EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*DOUBLE_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*CREATE_ACC_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AVATAR))

    driver.find_element(*LOGOUT_BUTTON).click()
    driver.quit()
    return email, password
    