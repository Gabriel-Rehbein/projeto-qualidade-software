# 🧩 Atividade PBL – Aula 9
## Testes Unitários Automatizados e TDD – LocalEats

**Instituição:** Centro Universitário Senac-RS  
**Curso:** ADS - Análise e Desenvolvimento de Sistemas / SPI - Sistemas para Internet  
**Disciplina:** Qualidade de Software  
**Professor:** Luciano Zanuz  

---

## 📌 Contexto

Após planejar, especificar e executar testes de forma estruturada, a equipe de Qualidade do sistema LocalEats precisa evoluir sua abordagem de QA:

👉 Sair de testes manuais e documentais para testes automatizados no código.

### Situação atual:
- Testes foram planejados e descritos  
- Execução manual ou simulada  

### Novo desafio:
👉 Garantir qualidade diretamente no código, de forma automatizada  

### Problemas do sistema:
- Regras de negócio inconsistentes  
- Falhas após alterações no código (regressões)  
- Dificuldade em validar rapidamente mudanças  
- Código difícil de manter e evoluir  

### Objetivo técnico:
Garantir que:
> “As regras de negócio sejam validadas automaticamente e continuamente.”

### Abordagem:
- Testes unitários automatizados  
- TDD (Test-Driven Development)  

🔗 Sistema: https://local-eats-unisenac.vercel.app/

---

## 🎯 Objetivo da Atividade

Aplicar, de forma prática e orientada ao desenvolvimento:

- Escrita de testes unitários automatizados  
- Validação de regras de negócio  
- Aplicação do ciclo TDD (Red → Green → Refactor)  
- Refatoração orientada por testes  

---

## ⚠️ Importante

- É necessário implementar código  
- Foco em funções e regras de negócio (backend ou lógica pura)  
- Não testar interface gráfica (frontend)  
- Utilizar a linguagem/stack do projeto  
- Caso não tenha sistema pronto, criar funções simuladas  
- O foco é o raciocínio e aplicação do TDD  

---

## 📝 Tarefas

---

### 🔹 1. Funcionalidade Escolhida

Selecionar uma regra de negócio por integrante.

👉 Cada integrante deve escolher uma funcionalidade diferente.

📌 Sugestões:

---

#### 🍔 1. Cálculo do total do pedido com valor mínimo

**O que faz:**
- Soma valores dos itens  
- Verifica valor mínimo  

**Problema:**
- Evita pedidos inválidos  

**Importância:**
- Regra central do sistema  

**Regras:**
- Total = soma dos itens  
- Se total < mínimo → erro  
- Caso contrário → válido  

```python
def calcular_total_pedido(itens, valor_minimo):
    total = sum(item["preco"] for item in itens)

    if total < valor_minimo:
        raise ValueError("Valor mínimo do pedido não atingido")

    return total