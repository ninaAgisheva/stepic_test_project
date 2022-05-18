from selenium.webdriver.common.by import By


#class MainPageLocators():
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn-lg:nth-child(3)")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")
    NAME_PRODUCT_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_PRODUCT_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    ALERT_SUCCESS = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2)")
    BUTTON_BASKET_PRODUCT = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    MESSAGE_EMPTY = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")