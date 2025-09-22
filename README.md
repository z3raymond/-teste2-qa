# BugBank Playwright Automation

Automação de testes E2E para o sistema BugBank usando Playwright com Python com foco em **registro** e **login** de usuários.

## 🚀 Funcionalidades Testadas

- **Registro de Usuário**: Criação de conta com e sem saldo, validações de email e senha
- **Login de Usuário**: Autenticação, validações e logout



## 🛠️ Instalação e Execução

```bash
# Instalar dependências Python
pip install -r requirements.txt

# Instalar browsers do Playwright
playwright install

# Executar todos os testes
pytest

# Executar teste específico
pytest tests/test_registro_usuario.py
pytest tests/test_login_usuario.py

# Executar com relatório detalhado
pytest -v --tb=short
```


## 🎯 Cenários de Teste

### Registro de Usuário
- ✅ Registro com dados válidos
- ✅ Registro com saldo inicial
- ✅ Validação de email inválido
- ✅ Validação de senhas diferentes
- ✅ Validação de campos obrigatórios
- ✅ Validação de nome obrigatório

### Login de Usuário
- ✅ Login com credenciais válidas
- ✅ Erro para credenciais inválidas
- ✅ Validação de campos obrigatórios
- ✅ Validação individual de email/senha
- ✅ Logout funcional
- ✅ Manutenção de sessão após reload

## 🔧 Tecnologias Utilizadas

- **Playwright** - Framework de automação web
- **Python** - Linguagem de programação
- **Pytest** - Framework de testes
- **Faker** - Geração de dados de teste
- **BugBank** - Sistema web de testes



