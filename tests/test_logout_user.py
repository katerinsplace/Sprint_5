from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

def test_logout_user_positive(main_page, new_email, new_password):
    driver = main_page
    driver.find_element(*REG_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(NO_ACC_BUTTON))
    driver.find_element(*NO_ACC_BUTTON).click()

    driver.find_element(*EMAIL_INPUT).send_keys(new_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(new_password)
    driver.find_element(*DOUBLE_PASSWORD_INPUT).send_keys(new_password)
    driver.find_element(*CREATE_ACC_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AVATAR))

    driver.find_element(*LOGOUT_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(REG_BUTTON))

    assert driver.find_elements(*AVATAR) == []
    assert driver.find_elements(*NAME_USER) == []
    

