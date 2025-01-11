from playwright.sync_api import expect
from conftest import handle_cookie_consent  


def test_search_api_request(goto_home_page):
    """Test API requests made during search interaction"""
    page = goto_home_page
    handle_cookie_consent(page)
    
    # Listen for the specific search API request and its response
    with page.expect_request("**/search/prefix.json?**") as request_info, \
         page.expect_response("**/search/prefix.json?**") as response_info:
        search = page.get_by_placeholder("Search Anime, Manga, and more...")
        search.type("Frieren", delay=100)
    
    # Analyze the request
    request = request_info.value
    assert request.method == "GET", f"Expected GET request, got {request.method}"
    assert "keyword=Frieren" in request.url, "Search term not found in request URL"
    
    # Analyze the response
    response = response_info.value
    assert response.ok, "Response was not successful"
    assert response.status == 200, f"Expected status 200, got {response.status}"

def test_search_response_content(goto_home_page):
    """Test search API response content"""
    page = goto_home_page
    handle_cookie_consent(page)
    
    # Listen for the response
    with page.expect_response("**/search/prefix.json?**") as response_info:
        search = page.get_by_placeholder("Search Anime, Manga, and more...")
        search.type("Frieren", delay=100)
    
    # Analyze the response content
    response = response_info.value
    data = response.json()  # Get JSON response
    
    # Verify response structure and content
    assert "categories" in data, "Response missing 'categories' field"
    assert data.get("categories"), "Categories should not be empty"

def test_search_edge_cases(goto_home_page):
    """Test search API with special characters and empty string"""
    page = goto_home_page
    handle_cookie_consent(page)
    
    # Test with special characters
    with page.expect_response("**/search/prefix.json?**") as response_info:
        search = page.get_by_placeholder("Search Anime, Manga, and more...")
        search.fill("")  # Clear any existing text
        search.type("!@#$%", delay=100)
    
    response = response_info.value
    assert response.status == 200, "Search with special characters should still return 200"
    data = response.json()
    assert isinstance(data["categories"], list), "Response should have categories list even for invalid search"