from playwright.sync_api import expect
from conftest import handle_cookie_consent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_login_link_visible(goto_home_page):
    """Test that verifies the login link is visible"""
    page = goto_home_page
    login_link = page.locator("#header-menu").get_by_role("link", name="Login")
    expect(login_link).to_be_visible()

def test_login_form(goto_login_page):
    page = goto_login_page
    
    # Wait for form to be loaded
    page.wait_for_selector("#login-password")
    
    # Check password field
    password_field = page.locator("#login-password")
    expect(password_field).to_be_visible()
    expect(password_field).to_be_editable()
    
    # Check username field
    username_field = page.locator("#loginUserName")
    expect(username_field).to_be_visible()
    expect(username_field).to_be_editable()

def test_invalid_login(goto_login_page):
    """Test login with invalid credentials"""
    page = goto_login_page
    
    # Click the "AGREE" button if it appears, or it may interrupt login
    handle_cookie_consent(page)
    
    # Fill in invalid credentials
    username_field = page.locator("#loginUserName")
    password_field = page.locator("#login-password")
    username_field.fill(os.getenv('INVALID_USERNAME'))
    password_field.fill(os.getenv('INVALID_PASSWORD'))
    
    # Click login
    page.locator("input[type='submit'][value='Login']").click(force=True)

    # Verify error message appears
    error_message = page.get_by_text("Your username or password is incorrect.")
    expect(error_message).to_be_visible()
    
def test_valid_login(perform_login):
    page = perform_login(os.getenv('VALID_USERNAME'), os.getenv('VALID_PASSWORD'))
    
    profile_link = page.locator(".header-profile-link")
    expect(profile_link).to_be_visible()
    profile_link.click()
   

def test_logout_functionality(perform_login):
    page = perform_login(os.getenv('VALID_USERNAME'), os.getenv('VALID_PASSWORD'))
    
    # Open profile dropdown
    profile_link = page.locator(".header-profile-link")
    profile_link.click()
    
    # Click logout
    logout_link = page.locator("a").filter(has_text="Logout")
    logout_link.click()
    
    # Verify logged out by checking for login button
    login_button = page.locator("#malLogin").first
    expect(login_button).to_be_visible()

def test_empty_fields_validation(goto_login_page):
    page = goto_login_page
    
    # Click the "AGREE" button if it appears, or it may interrupt login
    handle_cookie_consent(page)
    

     # Click login
    page.locator("input[type='submit'][value='Login']").click(force=True)

    # Verify error message appears (MAL uses incorrect error for empty field entry)
    error_message = page.get_by_text("Your username or password is incorrect.")
    expect(error_message).to_be_visible()

