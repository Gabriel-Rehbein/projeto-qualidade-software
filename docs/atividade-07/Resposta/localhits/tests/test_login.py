# tests/test_login.py
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login_com_sucesso(page: Page):
    login_page = LoginPage(page)
    
    # Executa o fluxo de login baseado na sua gravação
    login_page.acessar()
    login_page.realizar_login("gabrielmr0812@gmail.com", "12345678")
    
    # Asserção funcional: Garante que após o login, o botão/link "Explorar" fica visível
    expect(login_page.mensagem_boas_vindas).to_be_visible()