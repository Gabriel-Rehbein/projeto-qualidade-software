# tests/test_busca_restaurantes.py
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect

# Vincula o arquivo de feature aos cenários de teste do pytest
scenarios('../features/busca_restaurantes.feature')

@given('que o usuário está na página inicial do LocalEats')
def acessar_pagina_inicial(page: Page):
    page.goto('https://local-eats-unisenac.vercel.app/')
    # Garante que a página carregou verificando a seção principal
    expect(page.get_by_role('heading', name='Restaurantes')).to_be_visible()

@when(parsers.parse('pesquisar pelo termo "{termo}"'))
def pesquisar_termo(page: Page, termo: str):
    # Localiza o input de busca utilizando um seletor acessível por placeholder
    campo_busca = page.get_by_placeholder('Buscar restaurante ou culinária...')
    campo_busca.fill(termo)
    campo_busca.press('Enter')

@then('o sistema deve exibir os restaurantes correspondentes ao termo buscado')
def validar_resultados_existentes(page: Page):
    # Valida que pelo menos um card de restaurante permaneceu visível na listagem
    card_restaurante = page.locator('.restaurant-card, [class*="card"]').first
    expect(card_restaurante).to_be_visible()

@then('o sistema deve exibir uma mensagem informando que nenhum restaurante foi encontrado')
def validar_busca_vazia(page: Page):
    # Procura por uma mensagem textual indicando ausência de dados
    mensagem_vazio = page.get_by_text('Nenhum restaurante encontrado')
    expect(mensagem_vazio).to_be_visible()