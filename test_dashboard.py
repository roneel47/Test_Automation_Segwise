from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--allow-running-insecure-content")
    
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://ua.segwise.ai/qa_assignment")
wait = WebDriverWait(driver, 15)
        
# email
email_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[autocomplete='email']")))
email_field.send_keys("qa@segwise.ai")
        
# password
password_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[autocomplete='current-password']")))
password_field.click()
password_field.send_keys("segwise_test")
        
# Login
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(5)

# Switch App button
switch_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Switch App']")))
switch_button.click()
time.sleep(6)

cost_per_install = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Cost Per Install')]")))
print("Cost Per Install chart found!")
time.sleep(5)
          
d1_roas = driver.find_element(By.XPATH, "//*[contains(text(), 'D1 ROAS')]")
print("D1 ROAS chart found!")
time.sleep(5)
        
d7_roas = driver.find_element(By.XPATH, "//*[contains(text(), 'D7 ROAS')]")
print("D7 ROAS chart found!")
time.sleep(5)
