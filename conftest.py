import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.api_client import APIClient

# Load variables from .env file at the start of the session
load_dotenv()

# ==========================================
# UI FIXTURES
# ==========================================


@pytest.fixture(scope="function", autouse=True)
def set_default_timeout(page):
    # Set timeout to 60 seconds for all actions on this page
    page.set_default_timeout(60000)
    yield


@pytest.fixture
def login_page(page):
    """Provides LoginPage instance. Uses URL from .env if needed."""
    return LoginPage(page)


@pytest.fixture
def products_page(page):
    """Provides ProductsPage instance."""
    return ProductsPage(page)


# ==========================================
# API FIXTURES
# ==========================================


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright):
    """
    Creates a global API request context.
    Reads 'BASE_API_URL' from the .env file.
    """
    base_url = os.getenv("BASE_API_URL", "https://jsonplaceholder.typicode.com")

    request_context = playwright.request.new_context(
        base_url=base_url,
        extra_http_headers={
            "Content-type": "application/json; charset=UTF-8",
        },
    )
    yield request_context
    request_context.dispose()


@pytest.fixture
def api_client(api_request_context):
    """Injects the APIClient Page Object into tests."""
    return APIClient(api_request_context)


# ==========================================
# GLOBAL CONFIGURATION
# ==========================================


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Sets global browser launch arguments."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }
