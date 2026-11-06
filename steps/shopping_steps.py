import pytest
from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when
from pages.shopping_page import ShoppingPage

scenarios("../features/shopping.feature")


@pytest.fixture
def shopping_page(page) -> ShoppingPage:
    return ShoppingPage(page)


@given("user opens shopping page")
def open_shopping_page(shopping_page: ShoppingPage) -> None:
    shopping_page.open()

@given(parsers.parse('user applies search "{query}" and category "{category}"'))
def apply_search_and_category(
    shopping_page: ShoppingPage,
    query: str,
    category: str,
) -> None:
    shopping_page.search_and_filter_by_category(query, category)

@given(parsers.parse('product "{name}" is in the cart'))
def product_is_in_cart(shopping_page: ShoppingPage, name: str) -> None:
    shopping_page.prepare_product_in_cart(name)

@given(parsers.parse('product "{name}" with quantity {quantity:d} is in the cart'))
def product_with_quantity_is_in_cart(
    shopping_page: ShoppingPage,
    name: str,
    quantity: int,
) -> None:
    shopping_page.prepare_product_in_cart(name, quantity)

@given(parsers.parse('products "{names}" are in the cart'))
def products_are_in_cart(shopping_page: ShoppingPage, names: str) -> None:
    shopping_page.prepare_products_in_cart([name.strip() for name in names.split(",")])

@when(parsers.parse('user searches products for "{query}"'))
def search_products(shopping_page: ShoppingPage, query: str) -> None:
    shopping_page.search_products(query)

@when(parsers.parse('user filters products by category "{category}"'))
def filter_products_by_category(shopping_page: ShoppingPage, category: str) -> None:
    shopping_page.filter_by_category(category)

@when("user clears product filters")
def clear_product_filters(shopping_page: ShoppingPage) -> None:
    shopping_page.clear_filters()

@when(parsers.parse('user adds "{name}" to cart'))
def add_product_to_cart(shopping_page: ShoppingPage, name: str) -> None:
    shopping_page.add_product_to_cart(name)

@when(parsers.parse('user increases quantity of "{name}" by {times:d}'))
def increase_product_quantity(
    shopping_page: ShoppingPage,
    name: str,
    times: int,
) -> None:
    shopping_page.change_product_quantity(name, "increase", times)

@when(parsers.parse('user decreases quantity of "{name}" by {times:d}'))
def decrease_product_quantity(
    shopping_page: ShoppingPage,
    name: str,
    times: int,
) -> None:
    shopping_page.change_product_quantity(name, "decrease", times)

@when(parsers.parse('user removes "{name}" from cart'))
def remove_product_from_cart(shopping_page: ShoppingPage, name: str) -> None:
    shopping_page.remove_product_from_cart(name)

@when("user clears the cart")
def clear_cart(shopping_page: ShoppingPage) -> None:
    shopping_page.clear_cart()

@when("user checks out")
def checkout(shopping_page: ShoppingPage) -> None:
    shopping_page.checkout()

@when(parsers.parse('user buys "{name}" now'))
def buy_product_now(shopping_page: ShoppingPage, name: str) -> None:
    shopping_page.buy_product_now(name)

@then(parsers.parse('shopping results count equals "{count}"'))
def shopping_results_count_equals(shopping_page: ShoppingPage, count: str) -> None:
    expect(shopping_page.results_count).to_have_text(count)

@then(parsers.parse('shopping results contain only "{name}"'))
def shopping_results_contain_only(shopping_page: ShoppingPage, name: str) -> None:
    expect(shopping_page.get_product_names()).to_have_text([name])

@then("no shopping products are shown")
def no_shopping_products_are_shown(shopping_page: ShoppingPage) -> None:
    expect(shopping_page.product_cards).to_have_count(0)
    expect(shopping_page.empty_results_message).to_be_visible()

@then("shopping filters are cleared")
def shopping_filters_are_cleared(shopping_page: ShoppingPage) -> None:
    expect(shopping_page.search_input).to_have_value("")
    expect(shopping_page.category_select).to_have_value("all")
    expect(shopping_page.results_count).to_have_text("Showing 8 products")

@then(parsers.parse('cart count equals "{count}"'))
def cart_count_equals(shopping_page: ShoppingPage, count: str) -> None:
    expect(shopping_page.cart_count).to_have_text(count)

@then(parsers.parse('cart total equals "{total}"'))
def cart_total_equals(shopping_page: ShoppingPage, total: str) -> None:
    expect(shopping_page.cart_total).to_have_text(total)

@then(parsers.parse('quantity of "{name}" in cart equals "{quantity}"'))
def quantity_of_product_in_cart_equals(
    shopping_page: ShoppingPage,
    name: str,
    quantity: str,
) -> None:
    expect(shopping_page.get_quantity_for_product(name)).to_have_text(quantity)

@then(parsers.parse('cart contains "{name}"'))
def cart_contains_product(shopping_page: ShoppingPage, name: str) -> None:
    expect(
        shopping_page.cart_items.get_by_test_id("shop-cart-item-name")
    ).to_contain_text(name)

@then("cart is empty")
def cart_is_empty(shopping_page: ShoppingPage) -> None:
    expect(shopping_page.cart_empty_message).to_be_visible()
    expect(shopping_page.cart_items).to_have_count(0)

@then(parsers.parse('shopping message equals "{message}"'))
def shopping_message_equals(shopping_page: ShoppingPage, message: str) -> None:
    expect(shopping_page.get_cart_message()).to_be_visible()
    expect(shopping_page.get_cart_message()).to_have_text(message)
