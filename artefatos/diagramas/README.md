# 📊 Diagramas do Sistema – LocalEats

---

## 🔹 Diagrama de Casos de Uso

### Atores:
- Usuário
- Sistema

### Casos de uso:
- Realizar pedido
- Calcular total do pedido
- Aplicar desconto
- Calcular taxa de entrega
- Validar login

---

## 🔹 Diagrama de Classes

### Classes principais:

#### 📦 Pedido
- itens: lista
- valor_total: float

#### 📦 Item
- preco: float

#### 📦 Usuario
- email: string
- senha: string

#### 📦 ServicoPedido
- calcular_total_pedido()
- aplicar_desconto()
- calcular_entrega()

---

## 🔹 Diagrama de Sequência

### Fluxo: cálculo do pedido

1. Usuário envia itens
2. Sistema chama calcular_total_pedido()
3. Sistema soma valores
4. Sistema valida valor mínimo
5. Sistema retorna resultado ou erro

---

## 🔹 Diagrama de Atividades

Fluxo:

Início → Receber itens → Validar lista  
→ Lista vazia? → (Sim → Erro)  
→ Somar itens → Validar valor mínimo  
→ Abaixo do mínimo? → (Sim → Erro)  
→ Retornar total → Fim  

---

## 🎯 Objetivo dos Diagramas

- Representar a lógica do sistema  
- Facilitar entendimento técnico  
- Documentar arquitetura e fluxo  

---

## 🟢 Conclusão

Os diagramas representam corretamente o funcionamento da regra de negócio implementada, garantindo clareza e organização do projeto.