from page.base_page import BasePage
from utils.constants import *


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-one.html'

    def start_checkout(self):
        self.wait_for_selector_and_click(CHECKOUT_BUTTON_SELECTOR)
        self.assert_element_is_visible(FIRST_NAME_SELECTOR)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait_for_selector_and_type(FIRST_NAME_SELECTOR, first_name, 100)
        self.wait_for_selector_and_type(LAST_NAME_SELECTOR, last_name, 100)
        self.wait_for_selector_and_type(POSTAL_CODE_SELECTOR, postal_code, 100)
        self.assert_input_value(POSTAL_CODE_SELECTOR, postal_code)

    def complete_checkout(self):
        self.wait_for_selector_and_click(CONTINUE_BUTTON_SELECTOR)
        self.wait_for_selector_and_click(FINISH_BUTTON_SELECTOR)
        self.assert_text_present_on_page('Checkout: Complete!')

    def logout(self):
        self.wait_for_selector_and_click(BURGER_BUTTON_SELECTOR)
        self.assert_element_is_visible(LOGOUT_SELECTOR)
        self.wait_for_selector_and_click(LOGOUT_SELECTOR)
        self.assert_element_is_visible(LOGIN_BUTTON_SELECTOR)
