# pages/login_page.py
from playwright.sync_api import Page, Locator

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://local-eats-unisenac.vercel.app/static/login.html"
        # Seletores mapeados e limpos a partir do seu Codegen
        self.campo_email = page.get_by_role("textbox", name="teste@teste.com")
        self.campo_senha = page.get_by_role("textbox", name="Sua senha secreta")
        self.botao_entrar = page.locator("#loginForm").get_by_role("button", name="Entrar")
        self.mensagem_boas_vindas = page.get_by_role("link", name="Explorar")

    def acessar(self):
        self.page.goto(self.url)

    def realizar_login(self, email: str, senha: str):
        self.campo_email.fill(email)
        self.campo_senha.fill(senha)
        self.botao_entrar.click()