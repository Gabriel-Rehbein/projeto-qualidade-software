# 🧩 Atividade PBL – Aula 9
## Testes Unitários Automatizados e TDD – LocalEats

---

## 🔹 1. Funcionalidade Escolhida

### 🍔 Cálculo do total do pedido com valor mínimo

**Descrição:**
Responsável por somar os itens do pedido e validar se o valor mínimo foi atingido.

---

### 📏 Regras de negócio

- Total = soma dos itens
- Se total < valor mínimo → erro
- Lista vazia → erro
- Preço negativo → erro

---

## 🔴 TDD – RED (Teste antes do código)

```python
import pytest
from pedido import calcular_total_pedido

def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    resultado = calcular_total_pedido(itens, 15)
    assert resultado == 30

def test_deve_lancar_erro_quando_valor_minimo_nao_atingido():
    itens = [{"preco": 5}]
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, 10)

def test_deve_lancar_erro_quando_lista_vazia():
    with pytest.raises(ValueError):
        calcular_total_pedido([], 10)