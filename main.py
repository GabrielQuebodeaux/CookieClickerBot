from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def wait_for_element(by, key):
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((by, key)))


def click(by, key):
    wait_for_element(by, key)
    driver.find_element(by, key).click()


# Returns current number of cookies
def get_cookies():
    return driver.execute_script("return Game.cookies")


# Returns the cps of a specified product
def get_product_cps(product: str):
    return driver.execute_script(f'return Game.Objects["{product}"].storedCps')


# Returns the price of a specified product
def get_product_price(product: str):
    return driver.execute_script(f'return Game.Objects["{product}"].price')


# Returns the cps increase per cookie spent of a specified product
def get_product_value_factor(product: str):
    return get_product_cps(product) / get_product_price(product)


def get_optimal_product():
    max_value_factor = -1
    optimal_product = None
    for product in products:
        value_factor = get_product_value_factor(product)
        if value_factor > max_value_factor:
            max_value_factor = value_factor
            optimal_product = product
        elif value_factor == max_value_factor:
            if get_product_price(product) < get_product_price(optimal_product):
                optimal_product = product


# Buys the specified product
def purchase_product(product: str):
    index = products.index(product)
    product_id = f"product{index}"
    click(By.ID, product_id)


# Attempts to purchase an upgrade and returns True if the upgrade was purchased
def purchase_upgrade() -> bool:
    upgrades_available = (
        driver.execute_script("return Game.UpgradesInStore.length") != 0
    )
    if upgrades_available:
        click(By.ID, "upgrade0")
        return True
    return False


def main_loop():
    while True:
        click(By.ID, "bigCookie")
        if get_cookies() >= get_product_price(product):
            purchase_product(product)


# Webdriver Variables and setup
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
time.sleep(1)

# Language Select
wait_for_element(By.ID, "langSelect-EN")
driver.find_element(By.ID, "langSelect-EN").click()

products = [
    "Cursor",
    "Grandma",
    "Farm",
    "Mine",
    "Factory",
    "Bank",
    "Temple",
    "Wizard tower",
    "Shipment",
    "Alchemy lab",
    "Portal",
    "Time machine",
    "Antimatter condenser",
    "Prism",
    "Chancemaker",
    "Fractal engine",
    "Javascript console",
    "Idleverse",
    "Cortex baker",
    "You",
]

main_loop()

driver.quit()
