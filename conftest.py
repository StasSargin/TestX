import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):
    url = 'https://demo.opencart.com/'
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get(url)
    request.addfinalizer(driver.close)
    return driver
