from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LandingPage():

    def __init__(self, driver):
        self.driver = driver
        self.addToCart_button_Xpath = '//*[@id="product-listing-comparison-form"]/ul/li[1]/div/div[2]/div[5]/div/div/a'
        self.proceedToCheckout_LinkText = "Proceed to Cart"

    def go_to_shopping_cart(self):
        self.driver.find_element_by_xpath(self.addToCart_button_Xpath).click()
        #self.driver.implicitly_wait(10)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, self.proceedToCheckout_LinkText)))
        element.click()
       # self.driver.find_element_by_link_text(self.proceedToCheckout_LinkText).click()
