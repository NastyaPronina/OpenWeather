import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



def test_open_page(driver):
    driver.get("https://openweathermap.org/")
    driver.maximize_window()
    assert "openweathermap" in driver.current_url
    print(driver.current_url)


def test_check_page_title(driver):
    driver.get("https://openweathermap.org/")
    assert driver.title == "Сurrent weather and forecast - OpenWeatherMap"


def test_fill_search_city_field(driver):
    driver.get("https://openweathermap.org/")
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('New York')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
    search_option.click()
    expected_city = 'New York City, US'
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city


def test_switch_unit_of_measurement(driver):
    driver.get("https://openweathermap.org/")
    button_f = driver.find_element(By.XPATH, '//*[@id="weather-widget"]/div[1]/div/div/div[1]/div[2]')
    time.sleep(10)
    move = ActionChains(driver)
    move.click_and_hold(button_f).move_by_offset(80, 0).release().perform()
    # ActionChains(driver).drag_and_drop_by_offset(button_f, 72, 2).perform()
    time.sleep(10)



# as a user I want to be able to open Pricing page, so that I can see "Pricing" title at the top of the page
# verify if title of the opened page is "Pricing" and it's visible
# verify if there is a "Detailed pricing" button on the "Pricing" page
# Precondition
# Navigate to Main page https://openweathermap.org/
# Steps:
# Go to Pricing page using Pricing button in the top toolbar
# Verify title of the opened page
# Expected result:
# The title of the Pricing page is visible and matches expected text (Pricing)
def test_open_pricing(driver):
    driver.get("https://openweathermap.org/")
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    button_pricing = driver.find_element(By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
    button_pricing.click()
    expected_title = "Pricing"
    displayed_title = driver.find_element(By.CSS_SELECTOR, 'h1.breadcrumb-title').text
    assert displayed_title == expected_title


