from .base_page import BasePage

class RegisterPage(BasePage):
    # Seletores
    EMAIL_INPUT = 'input[name="email"]'
    NAME_INPUT = 'input[name="name"]'
    PASSWORD_INPUT = 'input[name="password"]:first-of-type'
    CONFIRM_PASSWORD_INPUT = 'input[name="passwordConfirmation"]'
    BALANCE_TOGGLE = '#toggleAddBalance'
    SUBMIT_BUTTON = 'button[type="submit"]'
    SUCCESS_MESSAGE = 'text=foi criada com sucesso'
    CLOSE_MODAL_BUTTON = '#btnCloseModal'
    ERROR_MESSAGE = '.kOeYBn'
    
    def fill_registration_form(self, user_data: dict, with_balance: bool = False):
        self.fill_input(self.EMAIL_INPUT, user_data['email'])
        self.fill_input(self.NAME_INPUT, user_data['name'])
        self.fill_input(self.PASSWORD_INPUT, user_data['password'])
        self.fill_input(self.CONFIRM_PASSWORD_INPUT, user_data['password'])
        
        if with_balance:
            self.click_element(self.BALANCE_TOGGLE)
    
    def submit_registration(self):
        self.click_element(self.SUBMIT_BUTTON)
    
    def close_success_modal(self):
        self.click_element(self.CLOSE_MODAL_BUTTON)
    
    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)