import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_saucedemo_flow(setup):
    driver = setup

    login_page = LoginPage(driver)

    # Step 2: Verify SWAG LABS text
    assert login_page.is_displayed(login_page.LOGO)

    # Step 3: Login
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    # Step 4: Add item to cart
    inventory.add_item_to_cart()
    assert inventory.is_item_added()

    # Step 5: Logout
    inventory.logout()
