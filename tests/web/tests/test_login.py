from pages.login import LoginPage


def test_login_with_valid_credentials(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "/inventory.html" in driver.current_url


def test_login_with_locked_user_shows_error(driver):
    page = LoginPage(driver)
    page.open()
    page.login("locked_out_user", "secret_sauce")
    assert "locked out" in page.error_message().lower()
