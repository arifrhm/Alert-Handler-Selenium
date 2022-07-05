from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def test_website():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    url = "https://demoqa.com/alerts/"
    driver.get (url)
    time.sleep(2)
    entry_content =  driver.find_element(By.ID, 'alertButton')
    print(entry_content.accessible_name)
    entry_content.click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(8)


if __name__ =="__main__" :
    test_website()