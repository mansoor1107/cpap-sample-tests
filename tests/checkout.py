from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/mansoor.aleep/downloads/chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.cpap.com/cpap-machines/travel-sized-cpap-machine")

driver.find_element_by_xpath('//*[@id="product-listing-comparison-form"]/ul/li[1]/div/div[2]/div[5]/div/div/a').click()
driver.find_element_by_link_text("Proceed to Cart").click()

driver.find_element_by_xpath('//*[@id="shopping-cart"]/section/div[2]/div/a').click()
driver.switch_to.active_element
driver.find_element_by_css_selector("#checkout-login > div.sixcol.last.mobile-hide > p > a").click()

driver.find_element_by_xpath('//*[@id="checkout-form"]/ul/li[1]/div/div[1]/input[1]').send_keys("Test name")
driver.find_element_by_xpath('//*[@id="checkout-form"]/ul/li[1]/div/div[1]/div/input').send_keys("Test middle name")
driver.find_element_by_xpath('//*[@id="checkout-form"]/ul/li[1]/div/div[1]/input[2]').send_keys("Test last name")
driver.find_element_by_xpath('//*[@id="checkout-form"]/ul/li[1]/div/div[2]/input[1]').send_keys("12345678910")
driver.find_element_by_xpath('//*[@id="checkout-form"]/ul/li[1]/div/div[2]/input[2]').send_keys("testcpap@gmail.com")
driver.find_element_by_xpath('//*[@id="checkout-form"]/ul/li[1]/div/div[2]/div[1]/input').send_keys("1234")
driver.find_element_by_xpath('//*[@id="checkout-form"]/ul/li[1]/fieldset/div/input[1]').send_keys("test street")
driver.find_element_by_xpath('//*[@id="checkout-form"]/ul/li[1]/fieldset/div/input[2]').send_keys("183")
driver.find_element_by_xpath('//*[@id="checkout-form"]/ul/li[1]/fieldset/div/input[3]').send_keys("Test City")
driver.find_element_by_xpath('//*[@id="checkout-form"]/ul/li[1]/fieldset/div/input[5]').send_keys("12345")
driver.find_element_by_xpath("//select[@name='MState']/option[text()='Alabama']").click()
driver.find_element_by_xpath("//select[@name='MCountry']/option[text()='United States']").click()
driver.find_element_by_css_selector("input[type='radio'][id='send-prescription-radio']").click()
driver.find_element_by_css_selector("input[type='radio'][id='rx-send-email']").click()
driver.find_element_by_css_selector("input[type='radio'][id='payment-send-check']").click()

time.sleep(2)
driver.close()
driver.quit()
print("Test completed")
