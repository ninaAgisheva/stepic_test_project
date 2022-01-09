from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        #breakpoint()
        assert self.browser.current_url == link


    def should_be_login_form(self):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = MainPage(self.browser, link)   
        page.open()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        

    def should_be_register_form(self):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = MainPage(self.browser, link)   
        page.open()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login register is not presented"