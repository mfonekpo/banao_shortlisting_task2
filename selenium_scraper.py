from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url="https://x.com"
# url = "https://twitter.com/GTNUK1"
driver.get(url)

# time.sleep(3)

# page_source = driver.page_source
# soup = bs(page_source, 'html.parser')

print(driver.find_element(By.CLASS_NAME, "css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3"))

