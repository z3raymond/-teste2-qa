import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.dashboard_page import DashboardPage
from utils.fake_data import FakeDataGenerator

class TestLoginUsuario:
    
    @pytest.fixture(autouse=True)
    def setup_user(self, page):
        """Cria usuário para testes de login"""
        self.user_data = FakeDataGenerator.generate_unique_user_data()
        
        home_page = HomePage(page)
        register_page = RegisterPage(page)
        
        home_page.navigate_to_home()
        home_page.go_to_register()
        register_page.fill_registration_form(self.user_data, with_balance=True)
        register_page.submit_registration()
        register_page.close_success_modal()
    
    def test_deve_fazer_login_com_credenciais_validas(self, page):
        """Deve fazer login com credenciais válidas"""
        home_page = HomePage(page)
        dashboard_page = DashboardPage(page)
        
        home_page.navigate_to_home()
        home_page.login(self.user_data['email'], self.user_data['password'])
        
        assert '/home' in page.url
        assert dashboard_page.is_dashboard_loaded()
        assert self.user_data['name'] in dashboard_page.get_user_name()
    
    def test_deve_exibir_erro_para_credenciais_invalidas(self, page):
        """Deve exibir erro para credenciais inválidas"""
        home_page = HomePage(page)
        
        home_page.navigate_to_home()
        home_page.login('email@inexistente.com', 'senhaerrada')
        
        page.wait_for_selector('text=Usuário ou senha inválido')
        assert page.is_visible('text=Usuário ou senha inválido')
        page.click('#btnCloseModal')
    
    def test_deve_validar_campos_obrigatorios_no_login(self, page):
        """Deve validar campos obrigatórios no login"""
        home_page = HomePage(page)
        
        home_page.navigate_to_home()
        page.click('button[type="submit"]:nth-child(2)')
        
        page.wait_for_selector('text=É campo obrigatório')
        assert page.is_visible('text=É campo obrigatório')
    
    def test_deve_validar_apenas_email_obrigatorio(self, page):
        """Deve validar apenas email obrigatório"""
        home_page = HomePage(page)
        
        home_page.navigate_to_home()
        home_page.fill_input('input[name="password"]:nth-child(2)', 'senha123')
        page.click('button[type="submit"]:nth-child(2)')
        
        page.wait_for_selector('text=É campo obrigatório')
        assert page.is_visible('text=É campo obrigatório')
    
    def test_deve_validar_apenas_senha_obrigatoria(self, page):
        """Deve validar apenas senha obrigatória"""
        home_page = HomePage(page)
        
        home_page.navigate_to_home()
        home_page.fill_input('input[name="email"]:nth-child(2)', 'teste@email.com')
        page.click('button[type="submit"]:nth-child(2)')
        
        page.wait_for_selector('text=É campo obrigatório')
        assert page.is_visible('text=É campo obrigatório')
    
    def test_deve_fazer_logout_com_sucesso(self, page):
        """Deve fazer logout com sucesso"""
        home_page = HomePage(page)
        dashboard_page = DashboardPage(page)
        
        home_page.navigate_to_home()
        home_page.login(self.user_data['email'], self.user_data['password'])
        
        assert '/home' in page.url
        dashboard_page.logout()
        
        assert page.url == 'https://bugbank.netlify.app/'
    
    def test_deve_manter_sessao_apos_reload(self, page):
        """Deve manter sessão após recarregar página"""
        home_page = HomePage(page)
        dashboard_page = DashboardPage(page)
        
        home_page.navigate_to_home()
        home_page.login(self.user_data['email'], self.user_data['password'])
        
        assert '/home' in page.url
        page.reload()
        
        assert '/home' in page.url
        assert dashboard_page.is_visible(dashboard_page.USER_NAME)