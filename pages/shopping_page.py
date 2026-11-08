from pages.base_page import BasePage
from playwright.sync_api import Locator, Page


class ShoppingPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._search_input = page.get_by_test_id("shop-search")
        self._category_select = page.get_by_test_id("shop-category")
        self._clear_filters_button = page.get_by_test_id("shop-clear-filters")
        self._results_count = page.get_by_test_id("shop-results-count")
        self._product_grid = page.get_by_test_id("shop-product-grid")
        self._product_cards = page.get_by_test_id("shop-product")
        self._empty_results_message = page.get_by_test_id("shop-empty")
        self._cart_items = page.get_by_test_id("shop-cart-item")
        self._cart_count_label = page.get_by_test_id("shop-cart-count")
        self._cart_empty_message = page.get_by_test_id("shop-cart-empty")
        self._cart_total = page.get_by_test_id("shop-cart-total")
        self._clear_cart_button = page.get_by_test_id("shop-clear-cart")
        self._checkout_button = page.get_by_test_id("shop-checkout")
        self._message = page.get_by_test_id("shop-message")


    def open(self) -> None:
        super().open("#shopping")

    def get_product_names(self) -> Locator:
        return self._product_grid.get_by_test_id("shop-product-name")

    def get_cart_message(self) -> Locator:
        return self._message

    def get_quantity_for_product(self, name: str) -> Locator:
        return self.product(name).get_by_test_id("shop-qty-value")

    def get_results_count(self) -> Locator:
        return self._results_count

    def get_product_cards(self) -> Locator:
        return self._product_cards

    def get_search_input(self) -> Locator:
        return self._search_input

    def get_cart_items(self) -> Locator:
        return self._cart_items

    def get_cart_count(self) -> Locator:
        return self._cart_count_label

    def get_cart_empty_message(self) -> Locator:
        return self._cart_empty_message

    def get_empty_results_message(self) -> Locator:
        return self._empty_results_message

    def get_cart_total(self) -> Locator:
        return self._cart_total

    def get_category_select(self) -> Locator:
        return self._category_select

    def product(self, name: str) -> Locator:
        return self._product_cards.filter(
            has=self.page.get_by_test_id("shop-product-name").get_by_text(name, exact=True)
        )

    def search_products(self, query: str) -> None:
        self._search_input.fill(query)

    def filter_by_category(self, category: str) -> None:
        self._category_select.select_option(category)

    def clear_filters(self) -> None:
        self._clear_filters_button.click()

    def search_and_filter_by_category(self, query: str, category: str) -> None:
        self.search_products(query)
        self.filter_by_category(category)

    def add_product_to_cart(self, name: str) -> None:
        self.product(name).get_by_test_id("shop-add-to-cart").click()

    def change_product_quantity(self, name: str, direction: str, times: int = 1) -> None:
        test_id = "shop-qty-increase" if direction == "increase" else "shop-qty-decrease"
        for _ in range(times):
            self.product(name).get_by_test_id(test_id).click()

    def remove_product_from_cart(self, name: str) -> None:
        self._cart_items.filter(
            has=self.page.get_by_test_id("shop-cart-item-name").get_by_text(name, exact=True)
        ).get_by_test_id("shop-cart-remove").click()

    def clear_cart(self) -> None:
        self._clear_cart_button.click()

    def checkout(self) -> None:
        self._checkout_button.click()

    def buy_product_now(self, name: str) -> None:
        self.product(name).get_by_test_id("shop-buy-now").click()

    def prepare_product_in_cart(self, name: str, quantity: int = 1) -> None:
        self.add_product_to_cart(name)
        if quantity > 1:
            self.change_product_quantity(name, "increase", quantity - 1)

    def prepare_products_in_cart(self, names: list[str]) -> None:
        for name in names:
            self.add_product_to_cart(name)
