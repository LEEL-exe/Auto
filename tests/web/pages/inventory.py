from selenium.webdriver.common.by import By

from pages.base import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, product_id):
        self.click((By.ID, f"add-to-cart-{product_id}"))
        self.find((By.ID, f"remove-{product_id}"))

    def cart_count(self):
        return int(self.text_of(self.CART_BADGE))

    def open_cart(self):
        self.click(self.CART_LINK)
        self.find((By.CLASS_NAME, "cart_list"))
