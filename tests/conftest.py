import pytest
from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@pytest.fixture(scope="function")
def goto_home_page(page: Page):
    """Navigate to homepage before each test"""
    page.goto("https://myanimelist.net")
    yield page

@pytest.fixture(scope="function")
def goto_login_page(page: Page):
    """Navigate to login page before each test"""
    page.goto("https://myanimelist.net/login.php")
    yield page

@pytest.fixture
def perform_login(goto_login_page):
   def _perform_login(username, password):
       page = goto_login_page
       
       if agree_button := page.query_selector('button:has-text("AGREE")'):
           agree_button.click(timeout=10000)
           
       username_field = page.locator("#loginUserName")
       password_field = page.locator("#login-password")
       username_field.fill(username)
       password_field.fill(password)
       page.locator("input[type='submit'][value='Login']").click(force=True)
       return page
   return _perform_login

def handle_cookie_consent(page):
    agree_button = page.query_selector('button:has-text("AGREE")')
    if agree_button:
        agree_button.click(timeout=10000)