from selenium.webdriver.common.by import By

REG_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
NO_ACC_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
EMAIL_INPUT = (By.NAME, 'email')
PASSWORD_INPUT = (By.NAME, 'password')
DOUBLE_PASSWORD_INPUT = (By.NAME, 'submitPassword')
CREATE_ACC_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
AVATAR = (By.CLASS_NAME, "svgSmall")
NAME_USER = (By.CSS_SELECTOR, "h3.profileText.name")

TEXT_ERROR = (By.XPATH, ".//span[text()='Ошибка']")
PARENT_EMAIL = (By.XPATH, ".//*[@name = 'email']/parent::*")
ALL_ERRORS = (By.XPATH, './/*[@class="input_inputError__fLUP9"]')

LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

CREATE_AD_BUTTON = (By.XPATH, ".//button[text()='Разместить объявление']")
MODAL_WINDOW_TO_LOGIN = (By.XPATH, "//*[contains(@class, 'homePage_modal')]//h1[text()='Чтобы разместить объявление, авторизуйтесь']")

NEW_AD_NAME = (By.CSS_SELECTOR, "input[placeholder='Название']")
NEW_AD_DESCRIPTION = (By.CSS_SELECTOR, "textarea[placeholder='Описание товара']")
NEW_AD_PRICE = (By.CSS_SELECTOR, "input[placeholder='Стоимость']")

CHOOSE_CITY_BUTTON = (By.XPATH, ".//*[@name='city']/parent::*/button")
CHOOSE_SPB = (By.XPATH, ".//span[text()='Санкт-Петербург']/parent::button")

CHOOSE_CATEGORY_BUTTON = (By.XPATH, ".//input[@name='category']/parent::*/button")
CHOOSE_CATEGORY_BOOKS = (By.XPATH, ".//span[text()='Книги']/parent::button")

CONDITION_RABIOBUTTON = (By.XPATH, ".//label[text()='Б/У']")
PUBLISH_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")
PROFILE_BUTTON = (By.XPATH, ".//button[@class='circleSmall']")
SEARCH_LINE = (By.XPATH, ".//input[@placeholder='Я хочу купить...']/parent::*/button")
FIND_AD = (By.XPATH, ".//h2[text()='Великий Гэтсби']")