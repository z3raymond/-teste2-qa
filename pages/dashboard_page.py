from .base_page import BasePage

class DashboardPage(BasePage):
    # Seletores
    USER_NAME = '#textName'
    ACCOUNT_NUMBER = '#textAccountNumber'
    BALANCE = '#textBalance'
    LOGOUT_BUTTON = '#btnExit'
    
    def get_user_name(self) -> str:
        return self.get_text(self.USER_NAME)
    
    def get_account_number(self) -> str:
        return self.get_text(self.ACCOUNT_NUMBER)
    
    def get_balance(self) -> str:
        return self.get_text(self.BALANCE)
    
    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)
    
    def is_dashboard_loaded(self) -> bool:
        return self.is_visible(self.USER_NAME) and self.is_visible(self.ACCOUNT_NUMBER)