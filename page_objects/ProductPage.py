from locators import Product


class ProductPage(BasePage):

    def add_product_to_cart(self):
        self._click(selector=Product.product_buttons)
        return ProductPage(self.driver)

    def click_cart_total(self):
        self._click(selector=Product.cart_total)
        return ProductPage(self.driver)

    def click_view_cart(self):
        self._click(selector=Product.view_cart)
        return CartPage(self.driver)
