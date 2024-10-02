from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Go to IMDb search name page
driver.get('https://www.imdb.com/search/name/')

# Wait until the page is fully loaded and input box is available
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.ID, 'name')))
search_box.clear()

# Input data into the search box
search_box.send_keys('Leonardo DiCaprio')

# Select options from dropdowns (for demonstration, selecting 'Gender')
gender_dropdown = wait.until(EC.element_to_be_clickable((By.ID, 'gender')))
gender_dropdown.click()

# Select 'Male' from the dropdown
male_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='male']")))
male_option.click()

# Select other options if necessary (for example, select 'StarMeter range')
starmeter_min = wait.until(EC.presence_of_element_located((By.NAME, 'starMeter-min')))
starmeter_min.clear()
starmeter_min.send_keys('1')

starmeter_max = wait.until(EC.presence_of_element_located((By.NAME, 'starMeter-max')))
starmeter_max.clear()
starmeter_max.send_keys('100')

# Perform the search
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
search_button.click()

# Optionally, add additional steps to extract results or perform further actions.

# Close the browser
driver.quit()