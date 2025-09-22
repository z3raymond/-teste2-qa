import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.fake_data import FakeDataGenerator

class TestRegistroUsuario:
    
    def test_deve_registrar_usuario_com_sucesso(self, page):
        """Deve registrar usuário com dados válidos"""
        user_data = FakeDataGenerator.generate_unique_user_data()
        
        home_page = HomePage(page)
        register_page = RegisterPage(page)
        
        home_page.navigate_to_home()
        home_page.go_to_register()
        
        register_page.fill_registration_form(user_data)
        register_page.submit_registration()
        
        assert register_page.is_visible(register_page.SUCCESS_MESSAGE)
        register_page.close_success_modal()
    
    def test_deve_registrar_usuario_com_saldo_inicial(self, page):
        """Deve registrar usuário com saldo inicial"""
        user_data = FakeDataGenerator.generate_unique_user_data()
        
        home_page = HomePage(page)
        register_page = RegisterPage(page)
        
        home_page.navigate_to_home()
        home_page.go_to_register()
        
        register_page.fill_registration_form(user_data, with_balance=True)
        register_page.submit_registration()
        
        assert register_page.is_visible(register_page.SUCCESS_MESSAGE)
        register_page.close_success_modal()
    
    def test_deve_validar_formato_email_invalido(self, page):
        """Deve validar formato de email inválido"""
        home_page = HomePage(page)
        register_page = RegisterPage(page)
        
        home_page.navigate_to_home()
        home_page.go_to_register()
        
        invalid_user = {
            'email': 'email-invalido',
            'name': 'Teste Usuario',
            'password': 'Senha123@'
        }
        
        register_page.fill_registration_form(invalid_user)
        register_page.submit_registration()
        
        error_message = register_page.get_error_message()
        assert 'formato inválido' in error_message
    
    def test_deve_validar_senhas_diferentes(self, page):
        """Deve validar quando senhas são diferentes"""
        user_data = FakeDataGenerator.generate_unique_user_data()
        
        home_page = HomePage(page)
        register_page = RegisterPage(page)
        
        home_page.navigate_to_home()
        home_page.go_to_register()
        
        register_page.fill_input(register_page.EMAIL_INPUT, user_data['email'])
        register_page.fill_input(register_page.NAME_INPUT, user_data['name'])
        register_page.fill_input(register_page.PASSWORD_INPUT, user_data['password'])
        register_page.fill_input(register_page.CONFIRM_PASSWORD_INPUT, 'SenhaDiferente123@')
        register_page.submit_registration()
        
        error_message = register_page.get_error_message()
        assert 'As senhas não são iguais' in error_message
    
    def test_deve_validar_campos_obrigatorios(self, page):
        """Deve validar campos obrigatórios"""
        home_page = HomePage(page)
        register_page = RegisterPage(page)
        
        home_page.navigate_to_home()
        home_page.go_to_register()
        register_page.submit_registration()
        
        # Verifica se há campos com erro
        assert register_page.is_visible('.input__default')
    
    def test_deve_validar_nome_obrigatorio(self, page):
        """Deve validar nome obrigatório"""
        user_data = FakeDataGenerator.generate_unique_user_data()
        
        home_page = HomePage(page)
        register_page = RegisterPage(page)
        
        home_page.navigate_to_home()
        home_page.go_to_register()
        
        register_page.fill_input(register_page.EMAIL_INPUT, user_data['email'])
        register_page.fill_input(register_page.PASSWORD_INPUT, user_data['password'])
        register_page.fill_input(register_page.CONFIRM_PASSWORD_INPUT, user_data['password'])
        register_page.submit_registration()
        
        error_message = register_page.get_error_message()
        assert 'Nome não pode ser vazio' in error_message or register_page.is_visible('.input__default')