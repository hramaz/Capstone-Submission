from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")

    def add_item_to_cart(self):
        self.click(self.ADD_TO_CART)

    def is_item_added(self):
        return self.is_displayed(self.CART_ICON)

    def logout(self):
        self.click(self.MENU_BTN)
        self.click(self.LOGOUT_BTN)
