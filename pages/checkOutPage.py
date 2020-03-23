class CheckOutPage():

    def __init__(self,driver):
        self.driver = driver

        self.firstName_Xpath = '//*[@id="checkout-form"]/ul/li[1]/div/div[1]/input[1]'
        self.middleName_Xpath = '//*[@id="checkout-form"]/ul/li[1]/div/div[1]/div/input'
        self.lastName_Xpath = '//*[@id="checkout-form"]/ul/li[1]/div/div[1]/input[2]'
        self.phoneNo_Xpath = '//*[@id="checkout-form"]/ul/li[1]/div/div[2]/input[1]'
        self.email_Xpath = '//*[@id="checkout-form"]/ul/li[1]/div/div[2]/input[2]'
        self.ext_Xpath = '//*[@id="checkout-form"]/ul/li[1]/div/div[2]/div[1]/input'
        self.street_Xpath = '//*[@id="checkout-form"]/ul/li[1]/fieldset/div/input[1]'
        self.aptNo_Xpath = '//*[@id="checkout-form"]/ul/li[1]/fieldset/div/input[2]'
        self.city_Xpath = '//*[@id="checkout-form"]/ul/li[1]/fieldset/div/input[3]'
        self.zip_Xpath = '//*[@id="checkout-form"]/ul/li[1]/fieldset/div/input[5]'
        self.state_Xpath = "//select[@name='MState']/option[text()='Alabama']"
        self.country_Xpath = "//select[@name='MCountry']/option[text()='United States']"
        self.sendPrescription_CssSelector = "input[type='radio'][id='send-prescription-radio']"
        self.sendEmail_CssSelector = "input[type='radio'][id='rx-send-email']"
        self.sendCheque_CssSelector = "input[type='radio'][id='payment-send-check']"


    def fill_personalDetails(self,fname,mname,lname,phone,ext,email):

        self.driver.find_element_by_xpath(self.firstName_Xpath).send_keys(fname)
        self. driver.find_element_by_xpath(self.middleName_Xpath).send_keys(mname)
        self.driver.find_element_by_xpath(self.lastName_Xpath).send_keys(lname)
        self.driver.find_element_by_xpath(self.phoneNo_Xpath).send_keys(phone)
        self.driver.find_element_by_xpath(self.email_Xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.ext_Xpath).send_keys(ext)

    def fill_shippingAddressDetails(self,streetname, aptno,city,zip):

        self.driver.find_element_by_xpath(self.street_Xpath).send_keys(streetname)
        self.driver.find_element_by_xpath(self.aptNo_Xpath).send_keys(aptno)
        self.driver.find_element_by_xpath(self.city_Xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.zip_Xpath).send_keys(zip)
        self.driver.find_element_by_xpath(self.state_Xpath).click()
        self.driver.find_element_by_xpath(self.country_Xpath).click()

    def fill_otherDetails(self):
        self.driver.find_element_by_css_selector(self.sendPrescription_CssSelector).click()
        self.driver.find_element_by_css_selector(self.sendEmail_CssSelector).click()
        self.driver.find_element_by_css_selector(self.sendCheque_CssSelector).click()