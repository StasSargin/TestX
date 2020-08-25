from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Header
from .BasePage import BasePage
from .ProductPage import ProductPage


class HeaderPage:

    def __init__(self, driver):
        self.driver = driver

    def __element(self, selector: dict, index: int, link_text: str = None):
        by = None
        if link_text:
            by = By.PARTIAL_LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)[index]

    def _click(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def click_category(self):
        self._click(selector=Header.categories)
        return HeaderPage(self.driver)

    def click_product(self):
        self._click(selector=Header.products, index=1)
        return ProductPage(self.driver)




