# Centro Universitário Senac-RS
### ADS - Análise e Desenvolvimento de Sistemas
**Unidade Curricular:** Qualidade de Software  
**Prof.:** Luciano Zanuz  
**Acadêmico:** Gabriel Menezes Rehbein

---

## 🧩 Atividade PBL – Aula 10: Testes Funcionais Automatizados

### 1. Fluxo funcional escolhido
- **Fluxo selecionado:** 🔐 Login de usuário
- **O que faz:** Autentica um usuário válido na plataforma LocalEats
- **Problema que resolve:** Garante controle de acesso e persistência de sessão para continuar o processo de compra
- **Importância:** É a porta de entrada do sistema; sem login, o usuário não avança
- **Resultado esperado:** Usuário válido é direcionado à tela “Explorar” e elementos autenticados ficam visíveis

---

## 🔹 2. Teste automatizado com Codegen
- **Comando utilizado:** `playwright codegen https://local-eats-unisenac.vercel.app/`
- **Observação:** O Playwright gravou a sequência de login e navegação inicial até o pedido

#### Código gerado automaticamente
```python
import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("[https://local-eats-unisenac.vercel.app/static/login.html](https://local-eats-unisenac.vercel.app/static/login.html)")
    page.get_by_role("textbox", name="teste@teste.com").dblclick()
    page.get_by_role("textbox", name="teste@teste.com").fill("gabrielmr0812@gmail.com")
    page.get_by_role("textbox", name="Sua senha secreta").dblclick()
    page.get_by_role("textbox", name="Sua senha secreta").fill("12345678")
    page.get_by_role("textbox", name="Sua senha secreta").press("Enter")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    page.get_by_role("button", name="Japonesa").click()
    page.get_by_role("link", name="Restaurante Sabor 1 Restaurante Sabor 1 $$  Japonesa  Centro Um ótimo lugar").dblclick()
    page.get_by_role("button", name="Cardápio").click()
    page.get_by_role("button", name="Cardápio").click()
    page.get_by_role("button", name=" Adicionar").first.click()
    page.get_by_role("link", name="Explorar").click()
    page.get_by_role("link", name="Restaurante Sabor 0").dblclick()
    page.get_by_role("button", name=" Adicionar").first.click()
    page.get_by_text("Seu Pedido 1 itens").click()
    page.get_by_text("LocalEats Explorar Meus").dblclick()
    page.get_by_text("Explorar Meus Favoritos Meus").click()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

---

### 3. Observações principais
- O fluxo capturado mostra autenticação e navegação até o pedido.
- O código gerado contém seletores automáticos e cliques repetidos que podem ser simplificados.
- É recomendável validar explicitamente a presença do elemento “Explorar” após o login.

---

### 4. Recomendações de melhoria
- Separar o teste de login em um caso específico.
- Usar seletores mais estáveis, como IDs ou nomes de campos claros.
- Tornar o teste mais robusto com assertivas funcionais em vez de apenas cliques.
- Organizar a automação em Page Objects e etapas claras para facilitar manutenção.