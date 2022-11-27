import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def br_size():
    browser.config.window_width = 800
    browser.config.window_height = 600


@pytest.fixture()
def br_size1():
    browser.config.window_width = 1000
    browser.config.window_height = 600
