from seleniumbase import BaseCase
BaseCase.main(__name__, __file__, "--rs", "--chs", "--sjw", "--pls=none")


def test_1(sb):
    sb.open("https://www.saucedemo.com")
    print(sb.get_current_url())


def test_2(sb):
    sb.open("https://material.angular.io")
    print(sb.get_current_url())


def test_3(sb):
    sb.open("https://www.openstreetmap.org/help")
    print(sb.get_current_url())
