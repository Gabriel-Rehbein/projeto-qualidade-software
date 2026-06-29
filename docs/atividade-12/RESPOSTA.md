# Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos - LocalEats

## 1. Repositório da Atividade

| Item | Descrição |
|---|---|
| Nome do repositório | projeto-qualidade-software |
| Link do repositório | https://github.com/Gabriel-Rehbein/projeto-qualidade-software |

### Estrutura de diretórios utilizada

```text
projeto-qualidade-software/
+-- .github/
|   +-- workflows/
|       +-- quality.yml
+-- docs/
|   +-- atividade-12/
|       +-- ENUNCIADO.md
|       +-- REFERENCIAS.md
|       +-- RESPOSTA.md
|       +-- order.py
|       +-- requirements.txt
|       +-- tests/
|           +-- test_order_total.py
+-- README.md
```

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|---|---|
| Título da Issue | Calcular total do pedido com taxa de entrega |
| Objetivo da funcionalidade | Implementar uma função simples para calcular o valor total de um pedido do LocalEats, somando o preço dos itens, suas quantidades e a taxa de entrega. |
| Link da Issue | Issue simulada para fins da atividade: `#1 - Calcular total do pedido com taxa de entrega` |

## 3. Teste Automatizado

| Item | Descrição |
|---|---|
| Tipo de teste | Unitário |
| Objetivo do teste | Verificar se o cálculo do total do pedido considera corretamente os preços, as quantidades e a taxa de entrega. |
| Link para o arquivo do teste | https://github.com/Gabriel-Rehbein/projeto-qualidade-software/blob/main/docs/atividade-12/tests/test_order_total.py |

### Código do teste criado

```python
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
```

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|---|---|
| Nome do workflow | Quality Checks |
| Evento que dispara a execução | `push` e `pull_request` na branch `main` |
| Link para o arquivo do workflow | https://github.com/Gabriel-Rehbein/projeto-qualidade-software/blob/main/.github/workflows/quality.yml |
| Link de uma execução do workflow | Após o push para o GitHub, a execução ficará disponível em: https://github.com/Gabriel-Rehbein/projeto-qualidade-software/actions |

### Código do workflow

```yaml
name: Quality Checks

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r docs/atividade-12/requirements.txt

      - name: Run tests
        run: pytest docs/atividade-12/tests
```

## 5. Indicadores de Qualidade

| Indicador | Valor |
|---|---|
| Quantidade de testes executados | 1 |
| Quantidade de testes aprovados | 1 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Aprovado na execução local; pendente de execução no GitHub Actions após push |

### Evidência da execução local

```text
collected 1 item

docs\atividade-12\tests\test_order_total.py . [100%]

1 passed
```

## 6. Registro de Defeito

| Item | Descrição |
|---|---|
| Título do defeito | Total do pedido não considerava a taxa de entrega |
| Severidade | Média |
| Link da Issue | Issue simulada para fins da atividade: `#2 - Total do pedido não considerava a taxa de entrega` |

O defeito simulado foi a ausência da taxa de entrega no cálculo final do pedido.  
Ele foi identificado por meio do teste unitário, que esperava a soma dos itens com a taxa.  
A correção foi feita ajustando a função `calcular_total_pedido` para somar `taxa_entrega` ao total dos itens.  
Depois da correção, o teste automatizado foi executado novamente e passou com sucesso.  
Esse fluxo demonstra o uso de teste automatizado para prevenir regressões.
