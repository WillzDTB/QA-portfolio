from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import helpers


class Page:
    LOCATOR = (By.ID, 'x')
    LOCATOR = (By.XPATH, 'x')
    LOCATOR = (By.CLASS, 'x')
    