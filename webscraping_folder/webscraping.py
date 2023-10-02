# Web scraping
import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.allrecipes.com/")

bs = BeautifulSoup(request.content, 'html5lib')
print(bs.prettify())


# Webbot to interact with website
# import selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options = option)

# driver.get('https://www.allrecipes.com/')
# elem = driver.find_element(By.NAME, "icon icon-search ")
# elem.clear()
# elem.send_keys("chicken")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()