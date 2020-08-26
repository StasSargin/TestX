from page_objects import BasePage, HeaderPage, MainPage, ProductPage


def test_smoke(browser):
    HeaderPage(browser)\
        .click_category()\
        .click_product()
    # ProductPage(browser)\
    #     .add_product_to_cart()\
    #     .click_cart_total()\
    #     .click_view_cart()
