from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

class TestLogOutUser:

    def test_logout_user_positive(self, driver, create_new_user):
        email, password = create_new_user
        driver.find_element(*REG_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(NO_ACC_BUTTON))

        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AVATAR))

        driver.find_element(*LOGOUT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(REG_BUTTON))

        assert driver.find_elements(*AVATAR) == []
        assert driver.find_elements(*NAME_USER) == []
    

