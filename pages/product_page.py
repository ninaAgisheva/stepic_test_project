from .main_page import MainPage
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(MainPage):


    def should_be_basket_page(self):

        self.prodyct_to_basket()


    def prodyct_to_basket(self, link):

        #link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = MainPage(self.browser, link)
        page.open()
        button = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button.click()
        #breakpoint()


    def should_not_be_success_message(self):
        
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), \
           "Success message is presented, but should not be"


    def should_not_be_success_message_too(self):
        
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), \
            "Success message is presented, but should not be"


    def message_empty_cart(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET_PRODUCT)
        button.click()
        assert self.is_element_present(*ProductPageLocators.MESSAGE_EMPTY)