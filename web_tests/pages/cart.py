from selenium.webdriver.common.by import By

from pages.base import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def go_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
