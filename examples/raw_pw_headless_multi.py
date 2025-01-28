"""
Note:
pytest-playwright and seleniumbase cannot be installed together.
(They have overlapping pytest args)
Pick one to install, and uninstall the other.

(This script uses pytest-playwright)
"""
import pytest

if __name__ == "__main__":
    pytest.main([__file__])


def test_1(page):
    page.goto("https://www.saucedemo.com")
    print(page.url)


def test_2(page):
    page.goto("https://material.angular.io")
    print(page.url)


def test_3(page):
    page.goto("https://www.openstreetmap.org/help")
    print(page.url)
