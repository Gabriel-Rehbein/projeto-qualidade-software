import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from order import calcular_total_pedido


def test_calcular_total_pedido_com_taxa_de_entrega():
    itens = [
        {"nome": "Hamburguer", "preco": 24.90, "quantidade": 2},
        {"nome": "Suco", "preco": 8.50, "quantidade": 1},
    ]

    total = calcular_total_pedido(itens, taxa_entrega=6.00)

    assert total == 64.30
