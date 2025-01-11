from playwright.sync_api import expect
from conftest import handle_cookie_consent
import os
from dotenv import load_dotenv

load_dotenv()

def test_search_suggestions_appear(goto_home_page):
    """Test that search suggestions appear when typing"""
    page = goto_home_page

    # Click the "AGREE" button if it appears, or it may interrupt login
    handle_cookie_consent(page)
    
    # Find search input
    search_input = page.get_by_placeholder("Search Anime, Manga, and more...")
    expect(search_input).to_be_visible()
    
    # Type slowly to trigger suggestions
    search_input.type("Frieren", delay=1250)
    
    # Verify suggestions appear
    suggestions = page.locator(".incrementalSearchResultList")
    expect(suggestions).to_be_visible()

def test_search_keyboard_navigation(goto_home_page):
    """Test keyboard navigation through search suggestions"""
    page = goto_home_page
    handle_cookie_consent(page)
    
    # Find and click search input
    search_input = page.get_by_placeholder("Search Anime, Manga, and more...")
    search_input.click()
    search_input.type("Frieren", delay=100)
    
    # Wait for suggestions and use keyboard to navigate
    suggestions = page.locator(".incrementalSearchResultList")
    expect(suggestions).to_be_visible()
    
    # Press arrow down to highlight suggestions
    search_input.press("ArrowDown")
    
    # Verify first suggestion is highlighted
    highlighted = suggestions.locator(".focus")
    expect(highlighted).to_be_visible()


def test_search_suggestion_click(goto_home_page):
    """Test clicking a search suggestion navigates to correct page"""
    page = goto_home_page
    handle_cookie_consent(page)
    
    # Find and type in search
    search_input = page.get_by_placeholder("Search Anime, Manga, and more...")
    search_input.click()
    search_input.type("Frieren", delay=1000)
    
    # Wait for and click anime suggestion (more specific)
    suggestions = page.locator(".incrementalSearchResultList")
    anime_suggestion = suggestions.locator(".list.anime").first
    expect(anime_suggestion).to_be_visible()
    
    # Click and wait for navigation
    with page.expect_navigation():
        anime_suggestion.click()
    
    # Verify we're on the anime page
    expect(page).to_have_url(page.url)
    anime_title = page.locator(".title-name")
    expect(anime_title).to_contain_text("Frieren")


def test_search_responsive_layout(goto_home_page):
    """Test search bar responsiveness at different viewport sizes"""
    page = goto_home_page
    handle_cookie_consent(page)
    
    # Test desktop layout (1920x1080)
    page.set_viewport_size({"width": 1920, "height": 1080})
    search_input = page.get_by_placeholder("Search Anime, Manga, and more...")
    expect(search_input).to_be_visible()
    
    # Test tablet layout (768x1024)
    page.set_viewport_size({"width": 768, "height": 1024})
    expect(search_input).to_be_visible()
    
    # Test mobile layout (375x667)
    page.set_viewport_size({"width": 375, "height": 667})
    expect(search_input).to_be_visible()
    
    # Verify search still works in mobile view
    search_input.click()
    search_input.type("Frieren", delay=100)
    suggestions = page.locator(".incrementalSearchResultList")
    expect(suggestions).to_be_visible()