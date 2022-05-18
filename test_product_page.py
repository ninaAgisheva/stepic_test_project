import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
from .pages.locators import LoginPageLocators

#@pytest.mark.parametrize('number', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])
#def test_guest_can_add_product_to_basket(browser, number):

    #link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{number}'
    #page = ProductPage(browser, link)
    #page.open()
    #page.prodyct_to_basket(link)
    #page.solve_quiz_and_get_code()
    #breakpoint()

    #name_produkt = browser.find_element(*ProductPageLocators.NAME_PRODUCT)
    #name_produkt_text = name_produkt.text

    #name_produkt_basket = browser.find_element(*ProductPageLocators.NAME_PRODUCT_BASKET)
    #name_produkt_basket_text = name_produkt_basket.text

    #price_produkt = browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
    #price_produkt_text = price_produkt.text

    #price_produkt_basket = browser.find_element(*ProductPageLocators.PRICE_PRODUCT_BASKET)
    #price_produkt_basket_text = price_produkt_basket.text

    #assert name_produkt_text == name_produkt_basket_text

    #assert price_produkt_text == price_produkt_basket_text

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):

    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.prodyct_to_basket(link)
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):

    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.message_empty_cart()


class TestUserAddToBasketFromProductPage():

    def test_user_cant_see_success_message(browser):

        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_disappeared_after_adding_product_to_basket(browser):

        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.prodyct_to_basket(link)
        page.should_not_be_success_message_too()



