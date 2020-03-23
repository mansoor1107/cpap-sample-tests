
from selenium import webdriver

def make_browser():
  driver = webdriver.Chrome(executable_path="/Users/mansoor.aleep/downloads/chromedriver")
  return driver