@shopping
Feature: Shopping page

  As a user
  I want to search products, manage the shopping cart and place orders
  So that I can practice automating an online shopping flow.

  Background:
    Given user opens shopping page

  @smoke @regression
  Scenario: User can search for a product
    When user searches products for "Wireless Headphones"
    Then shopping results contain only "Wireless Headphones"
    And shopping results count equals "Showing 1 product"

   @regression
   Scenario: User can search for a category
    When user searches products for "Home"
    Then shopping results count equals "Showing 2 products"

  @regression
  Scenario: User can filter products by category
    When user filters products by category "Electronics"
    Then shopping results count equals "Showing 4 products"

  @regression
  Scenario: User sees an empty state when no products match
    When user searches products for "nonexistent product"
    Then no shopping products are shown

  @regression
  Scenario: User can clear search and category filters
    Given user applies search "Lamp" and category "Home"
    When user clears product filters
    Then shopping filters are cleared

  @smoke @regression
  Scenario: User can add a product to the cart
    When user adds "Wireless Headphones" to cart
    Then cart contains "Wireless Headphones"
    And cart count equals "1"
    And cart total equals "$59.99"

  @regression
  Scenario: User can increase a product quantity in the cart
    Given product "Wireless Headphones" is in the cart
    When user increases quantity of "Wireless Headphones" by 2
    Then quantity of "Wireless Headphones" in cart equals "3"
    And cart count equals "3"
    And cart total equals "$179.97"

  @regression
  Scenario: Decreasing quantity to zero removes a product from the cart
    Given product "Wireless Headphones" is in the cart
    When user decreases quantity of "Wireless Headphones" by 1
    Then cart is empty
    And cart total equals "$0.00"

  @regression
  Scenario: User can remove a product from the cart
    Given product "Wireless Headphones" is in the cart
    When user removes "Wireless Headphones" from cart
    Then cart is empty
    And cart total equals "$0.00"

  @regression
  Scenario: User can clear the cart
    Given products "Wireless Headphones, USB-C Hub" are in the cart
    When user clears the cart
    Then cart is empty
    And cart total equals "$0.00"

  @regression @negative
  Scenario: User cannot check out with an empty cart
    When user checks out
    Then shopping message equals "Cart is empty. Add a product first."

  @smoke @regression
  Scenario: User can complete checkout
    Given product "Wireless Headphones" with quantity 2 is in the cart
    When user checks out
    Then shopping message equals "Checkout successful: Wireless Headphones ×2 — Total $119.98"
    And cart is empty

  @regression
  Scenario: User can buy a product immediately
    When user buys "Wireless Headphones" now
    Then shopping message equals "Order placed for Wireless Headphones ×1 — $59.99"
