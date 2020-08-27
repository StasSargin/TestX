from page_objects import BasePage, HeaderPage, MainPage, ProductPage


def test_smoke(browser):
    MainPage(browser)\
        .click_item()
