from pages.cart import CartPage
from pages.checkout import CheckoutPage
from pages.inventory import InventoryPage
from pages.login import LoginPage


def test_full_purchase_flow(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")
    assert inventory.cart_count() == 2
    inventory.open_cart()

    cart = CartPage(driver)
    assert cart.items_count() == 2
    cart.go_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_info("Leo", "Test", "12345")
    checkout.finish()
    assert "Thank you for your order!" in checkout.confirmation_message()
