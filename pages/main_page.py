from .base_page import BasePage
#from .locators import MainPageLocators
from .locators import LoginPageLocators 
from .locators import ProductPageLocators

from selenium.webdriver.common.by import By

#class MainPage(BasePage):
    
#    def go_to_login_page(self):

#        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#        login_link.click() 
#        return LoginPage(browser=self.browser, url=self.browser.current_url) 

#    def should_be_login_link(self):

#        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


    def message_empty_cart(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET_PRODUCT)
        button.click()
        assert self.is_element_present(*ProductPageLocators.MESSAGE_EMPTY)