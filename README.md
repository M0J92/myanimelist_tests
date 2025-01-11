MyAnimeList Test Automation Project
Overview
This project demonstrates automated testing of MyAnimeList.net using:

Python
Pytest
Playwright
Environment variables for secure credential management

Project Structure
Copymyanimelist_tests/
├── tests/
│   ├── conftest.py              # Shared fixtures and utilities
│   ├── test_authentication.py   # Login/logout tests
│   ├── test_search.py          # Search functionality tests
│   ├── test_network.py         # API and network tests
│   └── test_navigation.py      # Navigation and responsive tests
├── .env                        # Environment variables (not in git)
├── requirements.txt            # Project dependencies
├── test_requirements.md        # Test coverage documentation
└── README.md                   # Project documentation
Setup

Install Python 3.8 or higher
Create virtual environment:

bashCopypython -m venv venv
venv\Scripts\activate  # On Windows

Install dependencies:

bashCopypip install -r requirements.txt
playwright install

Create .env file with credentials:

CopyVALID_USERNAME="your_username"
VALID_PASSWORD="your_password"
INVALID_USERNAME="wrong_username"
git
Running Tests
Run all tests:
bashCopypytest
Run specific test file:
bashCopypytest tests/test_authentication.py
Run tests with visible browser:
bashCopypytest --headed
Test Coverage

Authentication flows
Search functionality
Network requests
Responsive design
Error handling

Features Demonstrated

Page object interactions
Network request monitoring
Form handling
API testing
Responsive design testing
Environment variable usage
Test fixtures and utilities