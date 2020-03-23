class shoppingCartPage():

    def __init__(self, driver):
        self.driver = driver
        self.secureCheckOut_Xpath = '//*[@id="shopping-cart"]/section/div[2]/div/a'
        self.continueAsGuest_CssSelector = "#checkout-login > div.sixcol.last.mobile-hide > p > a"

    def go_to_checkoutPage(self):
        self.driver.find_element_by_xpath(self.secureCheckOut_Xpath).click()
        self.driver.switch_to.active_element
        self.driver.find_element_by_css_selector(self.continueAsGuest_CssSelector).click()
