Feature: cpap.com checkout flow

    Scenario: Happy path scenario to buy a Travel sized machine

        Given The user is on the cpap.com travel sized machines page
        When The user adds the product in to the shopping cart
        Then The user should be to navigate to the checkout page and complete the purchase