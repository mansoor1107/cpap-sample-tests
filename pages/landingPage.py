class LandingPage():

    def __init__(self, driver):
        self.driver = driver
        self.addToCart_button_Xpath = '//*[@id="product-listing-comparison-form"]/ul/li[1]/div/div[2]/div[5]/div/div/a'
        self.proceedToCheckout_LinkText = "Proceed to Cart"

    def go_to_shopping_cart(self):
        self.driver.find_element_by_xpath(self.addToCart_button_Xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text(self.proceedToCheckout_LinkText).click()
