import pytest

if __name__ == "__main__":
    pytest.main([__file__, "--rs", "--chs", "--pls=none"])


def test_1(sb):
    sb.driver.get("https://www.saucedemo.com")
    print(sb.driver.current_url)


def test_2(sb):
    sb.driver.get("https://material.angular.io")
    print(sb.driver.current_url)


def test_3(sb):
    sb.driver.get("https://www.openstreetmap.org/help")
    print(sb.driver.current_url)
