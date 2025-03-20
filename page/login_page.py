from page.base_page import BasePage
from utils.constants import USERNAME_SELECTOR, PASSWORD_SELECTOR, LOGIN_BUTTON_SELECTOR


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(USERNAME_SELECTOR, username)
        self.wait_for_selector_and_fill(PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(LOGIN_BUTTON_SELECTOR)
        self.assert_text_present_on_page('Products')