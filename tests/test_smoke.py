from page_objects import BasePage, HeaderPage, MainPage, ProductPage


def test_smoke(browser):
    HeaderPage(browser)\
        .click_category()\
        .click_product()
    # header_page = HeaderPage(browser)
    # header_page.click_product()
