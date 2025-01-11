from playwright.sync_api import expect
from conftest import handle_cookie_consent

def test_anime_dropdown_interaction(goto_home_page):
    """Test anime dropdown menu interaction and visibility"""
    page = goto_home_page
    handle_cookie_consent(page)
    
    # Find and hover over Anime menu using the non-link class
    anime_menu = page.locator("a.non-link").get_by_text("Anime", exact=True)
    expect(anime_menu).to_be_visible()
    
    anime_menu.hover()
    
    # Verify dropdown appears with specific menu items
    expect(page.get_by_role("link", name="Top Anime")).to_be_visible()
    expect(page.get_by_role("link", name="Seasonal Anime")).to_be_visible()

def test_mobile_redirection(goto_home_page):
    """Test website behavior with mobile user agent"""
    page = goto_home_page
    
    # Store current URL
    desktop_url = page.url
    
    # Set mobile user agent and viewport
    page.set_viewport_size({"width": 375, "height": 667})
    page.set_extra_http_headers({
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
    })
    
    # Reload page with mobile settings
    page.reload()
    mobile_url = page.url
    
    # Verify we can still use core functionality
    search = page.get_by_placeholder("Search Anime, Manga, and more...")
    assert search.is_visible(), "Search should be accessible on mobile"
    
    # Take screenshots for visual comparison
    page.screenshot(path="mobile_view.png")
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.screenshot(path="desktop_view.png")