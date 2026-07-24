from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

class TestLoginUser:

    def test_login_user_positive(self, driver, create_new_user):
        email, password = create_new_user

        #WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(REG_BUTTON))

        driver.find_element(*REG_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(NO_ACC_BUTTON))

        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        #проверка аватара
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AVATAR))

        #проверка имени
        name = driver.find_element(*NAME_USER)
        assert name.text == "User."



