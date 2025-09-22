from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://bugbank.netlify.app/"
    
    def navigate_to_home(self):
        self.page.goto(self.base_url)
    
    def wait_for_element(self, selector: str, timeout: int = 10000):
        return self.page.wait_for_selector(selector, timeout=timeout)
    
    def click_element(self, selector: str):
        self.page.click(selector)
    
    def fill_input(self, selector: str, text: str):
        self.page.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector)
    
    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)