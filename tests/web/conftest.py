import pytest

from utils.driver import create_driver


@pytest.fixture
def driver():
    drv = create_driver()
    drv.implicitly_wait(5)
    yield drv
    drv.quit()
