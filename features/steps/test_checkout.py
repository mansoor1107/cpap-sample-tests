from behave import *
import time
from pages.landingPage import LandingPage
from pages.shoppingCartPage import shoppingCartPage
from pages.checkOutPage import CheckOutPage
from browser.browser import make_browser

use_step_matcher("re")


class CPAPCheckout():

    @given("The user is on the cpap\.com travel sized machines page")
    def step_impl(context):
        context.driver = make_browser()
        context.driver.get("https://www.cpap.com/cpap-machines/travel-sized-cpap-machine")
        context.driver.implicitly_wait(10)
        context.driver.maximize_window()
        landingpage = LandingPage(context.driver)
        landingpage.go_to_shopping_cart()

    @when("The user adds the product in to the shopping cart")
    def step_impl(context):
        shoppingCart = shoppingCartPage(context.driver)
        shoppingCart.go_to_checkoutPage()

    @then("The user should be to navigate to the checkout page and complete the purchase")
    def step_impl(context):
        checkoutFlow = CheckOutPage(context.driver)
        checkoutFlow.fill_personalDetails("firstname", "middlename", "lastname", "1234567891", "12345",
                                          "testcpap@gmail.com")
        checkoutFlow.fill_shippingAddressDetails("Test street", "183", "Test city", "12345")
        checkoutFlow.fill_otherDetails()
        time.sleep(2)
        context.driver.close()
        context.driver.quit()
        print("Test completed")
