from playwright.sync_api import expect


def test_products_page_displays_items(login_page, products_page):
    """Verifies that the product list is loaded after login."""
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Assert that there is more than one product visible
    count = products_page.inventory_items.count()
    assert count > 0


def test_add_to_cart_updates_badge(login_page, products_page):
    """Verifies that clicking 'Add to Cart' updates the header badge."""
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_first_item_to_cart()

    expect(products_page.cart_badge).to_have_text("1")
