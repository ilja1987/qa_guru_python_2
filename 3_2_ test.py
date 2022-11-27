import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture()
def br_size():
    browser.config.window_width = 800
    browser.config.window_height = 600
@pytest.fixture()
def br_size1():
    browser.config.window_width = 1000
    browser.config.window_height = 600


def test_sl1(br_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_sl2(br_size1):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('selenoid: User-oriented Web UI browser tests in Python'))
