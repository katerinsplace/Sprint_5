from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import name_of_book, description_of_book, price_of_book
from locators import *

class TestAdCreation:

    def test_create_ad_by_unauthorized_user(self, driver):
        driver.find_element(*CREATE_AD_BUTTON).click()
        modal_header = driver.find_element(*MODAL_WINDOW_TO_LOGIN)
        assert modal_header is not None

    def test_create_ad_by_authorized_user(self, driver, create_new_user):
        email, password = create_new_user
        driver.find_element(*REG_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(NO_ACC_BUTTON))

        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AVATAR))

        driver.find_element(*CREATE_AD_BUTTON).click()

        driver.find_element(*NEW_AD_NAME).send_keys(name_of_book)
        driver.find_element(*NEW_AD_DESCRIPTION).send_keys(description_of_book)
        driver.find_element(*NEW_AD_PRICE).send_keys(price_of_book)

        driver.find_element(*CHOOSE_CATEGORY_BUTTON).click()
        driver.find_element(*CHOOSE_CATEGORY_BOOKS).click()
        driver.find_element(*CHOOSE_CITY_BUTTON).click()
        driver.find_element(*CHOOSE_SPB).click()

        driver.find_element(*CONDITION_RABIOBUTTON).click()
        driver.find_element(*PUBLISH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(SEARCH_LINE))
        driver.find_element(*PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(FIND_AD))
        assert driver.find_element(*FIND_AD).text is not None

