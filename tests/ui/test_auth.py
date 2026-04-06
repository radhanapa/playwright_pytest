from playwright.sync_api import expect
import pytest
import allure


@pytest.mark.ui
@pytest.mark.smoke
@allure.feature("Authentication")
def test_valid_login(login_page, page):
    """Verifies that a user can log in with valid credentials."""
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_invalid_login_error(login_page):
    """Verifies that an error message appears for wrong credentials."""
    login_page.navigate()
    login_page.login("wrong_user", "wrong_password")

    # Assuming you added error_message locator to LoginPage
    expect(login_page.error_message).to_be_visible()
