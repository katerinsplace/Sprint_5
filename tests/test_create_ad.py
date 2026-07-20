from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

def test_create_ad_by_unauthorized_user(main_page):
    driver = main_page
    driver.find_element(*CREATE_AD_BUTTON).click()
    modal_header = driver.find_element(*MODAL_WINDOW_TO_LOGIN)
    assert modal_header is not None

def test_create_ad_by_authorized_user(main_page, new_email, new_password):
    driver = main_page
    driver.find_element(*REG_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(NO_ACC_BUTTON))
    driver.find_element(*NO_ACC_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))

    driver.find_element(*EMAIL_INPUT).send_keys(new_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(new_password)
    driver.find_element(*DOUBLE_PASSWORD_INPUT).send_keys(new_password)
    driver.find_element(*CREATE_ACC_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AVATAR))
    driver.find_element(*CREATE_AD_BUTTON).click()

    name_of_book = "Великий Гэтсби"
    description_of_book = "«Великий Гэтсби» — это история о загадочном миллионере Джее Гэтсби, который закатывает роскошные вечеринки ради одной цели: вернуть свою прошлую любовь, Дэйзи Бьюкенен. Роман показывает крах иллюзий и американской мечты в циничном мире богачей 1920-х годов."
    price_of_book = 500

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

