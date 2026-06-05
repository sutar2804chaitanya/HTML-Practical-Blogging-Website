from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1️⃣ Open Google Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 2️⃣ Open Google website
driver.get("https://www.google.com")
time.sleep(3)

# 3️⃣ Open Gmail website
driver.get("https://mail.google.com")

wait = WebDriverWait(driver, 20)

# 4️⃣ Login to Gmail (for learning/demo)
email = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
email.send_keys("your_email@gmail.com")
email.send_keys(Keys.ENTER)

password = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
password.send_keys("your_password")
password.send_keys(Keys.ENTER)

time.sleep(5)

# 5️⃣ Logout from Gmail
profile_icon = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'SignOutOptions')]"))
)
profile_icon.click()

time.sleep(2)

logout = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Sign out']"))
)
logout.click()

time.sleep(3)

# Close browser
driver.quit()
