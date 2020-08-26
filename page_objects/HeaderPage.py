from locators import Header
from .BasePage import BasePage
from .ProductPage import ProductPage


class HeaderPage(BasePage):

    def click_category(self):
        self._click(selector=Header.categories)
        return HeaderPage(self.driver)

    def click_product(self):
        self._click(selector=Header.products, index=1)
        return ProductPage(self.driver)




