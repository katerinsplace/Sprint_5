import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from random import choices
from string import ascii_lowercase, digits

symbols = ascii_lowercase + digits


@pytest.fixture
def main_page():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.education-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture
def new_email():
    random_name = ''.join(choices(symbols, k=10))
    return f"{random_name}@yandex.ru"

@pytest.fixture
def new_password():
    return ''.join(choices(symbols, k=8))