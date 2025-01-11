# MyAnimeList Test Automation Project

This project demonstrates automated testing of MyAnimeList.net using:
- Python
- Pytest
- Playwright
- Environment variables for secure credential management

## Project Structure
myanimelist_tests/

├── tests/

│   ├── conftest.py          # Shared fixtures and utilities

│   ├── test_authentication.py   # Login/logout tests

│   ├── test_search.py      # Search functionality tests

│   ├── test_network.py     # API and network tests

│   └── test_navigation.py  # Navigation and responsive tests

├── .env                    # Environment variables (not in git)

├── requirements.txt        # Project dependencies

├── test_requirements.md    # Test coverage documentation

└── README.md              # Project documentation

## Setup

1. Install Python 3.8 or higher.

2. Create a virtual environment:

   >python -m venv venv
   >venv\Scripts\activate  # On Windows

3. Install dependencies:

   >pip install -r requirements.txt
   >playwright install

4. Create .env file with credentials:

  >VALID_USERNAME="your_username"

  >VALID_PASSWORD="your_password"

  >INVALID_USERNAME="wrong_username"

  >INVALID_PASSWORD="wrong_password"


## Running Tests

Running all tests 
>pytest
>
Running specific test file
>pytest tests/test_authentication.py

Running tests with visible browser
>pytest --headed


## Test Coverage
Authentication Testing

- Login link visibility
- Login form elements verification
- Valid login with credentials
- Invalid login handling
- Empty fields validation
- Logout functionality

Search Functionality

- Search suggestions appearance
- Keyboard navigation through suggestions
- Search suggestion clicking

Network Requests

- Search API request verification
- Response content validation
- Search with edge cases

Navigation & Responsive Design

- Anime dropdown menu interaction
- Mobile view testing
- Responsive design verification

Features Demonstrated

- Page object interactions
- Network request monitoring
- Form handling
- API testing
- Responsive design testing
- Environment variable usage
- Test fixtures and utilities
