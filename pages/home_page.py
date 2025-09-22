from .base_page import BasePage

class HomePage(BasePage):
    # Seletores
    EMAIL_INPUT = 'input[name="email"]:nth-child(2)'
    PASSWORD_INPUT = 'input[name="password"]:nth-child(2)'
    LOGIN_BUTTON = 'button[type="submit"]:nth-child(2)'
    REGISTER_BUTTON = '.ihdmxA'
    
    def login(self, email: str, password: str):
        self.fill_input(self.EMAIL_INPUT, email)
        self.fill_input(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
    
    def go_to_register(self):
        self.click_element(self.REGISTER_BUTTON)