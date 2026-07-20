from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


def test_registration_positive(main_page, new_email, new_password):
    driver = main_page
    driver.find_element(*REG_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(NO_ACC_BUTTON))
    driver.find_element(*NO_ACC_BUTTON).click()

    driver.find_element(*EMAIL_INPUT).send_keys(new_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(new_password)
    driver.find_element(*DOUBLE_PASSWORD_INPUT).send_keys(new_password)
    driver.find_element(*CREATE_ACC_BUTTON).click()

    #проверка аватара
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AVATAR))

    #проверка имени
    name = driver.find_element(*NAME_USER)
    assert name.text == "User."


def test_registration_invalid_email(main_page):
    driver = main_page
    driver.find_element(*REG_BUTTON).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(NO_ACC_BUTTON))
    
    driver.find_element(*NO_ACC_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys('invalid_email_without_at_and_dot')
    driver.find_element(*CREATE_ACC_BUTTON).click()

    #проверка текста "Ошибка"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TEXT_ERROR))

    #проверка ошибки поля email
    parent_of_email = driver.find_element(*PARENT_EMAIL)
    assert parent_of_email.get_attribute('class') == "input_inputError__fLUP9"
    
    #проверка ошибок в трех полях
    assert len(driver.find_elements(*ALL_ERRORS)) == 3

def test_registration_existing_user(main_page, new_email, new_password):
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

    #повторная попытка регистрации
    driver.find_element(*REG_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(NO_ACC_BUTTON))
    driver.find_element(*NO_ACC_BUTTON).click()
    driver.find_element(*EMAIL_INPUT).send_keys(new_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(new_password)
    driver.find_element(*DOUBLE_PASSWORD_INPUT).send_keys(new_password)
    driver.find_element(*CREATE_ACC_BUTTON).click()

    #проверка текста "Ошибка"
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TEXT_ERROR))

    #проверка ошибки поля email
    parent_of_email = driver.find_element(*PARENT_EMAIL)
    assert parent_of_email.get_attribute('class') == "input_inputError__fLUP9"
    
    #проверка ошибок в трех полях
    assert len(driver.find_elements(*ALL_ERRORS)) == 3
