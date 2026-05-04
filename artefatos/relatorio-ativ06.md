# 📄 Relatório Final – Qualidade de Software
## Testes Unitários Automatizados e TDD – LocalEats

---

## 📌 1. Introdução

Este trabalho teve como objetivo aplicar conceitos de Qualidade de Software no sistema LocalEats, com foco na implementação de testes unitários automatizados e na utilização da metodologia TDD (Test-Driven Development).

A atividade buscou simular um cenário real de desenvolvimento, onde a qualidade do código é garantida por meio de validações automatizadas.

---

## 🎯 2. Objetivo

Garantir a qualidade do sistema através de:

- Testes unitários automatizados  
- Validação de regras de negócio  
- Aplicação do ciclo TDD (Red → Green → Refactor)  
- Refatoração orientada por testes  

---

## 🔧 3. Funcionalidade Implementada

### 🍔 Cálculo do total do pedido com valor mínimo

A funcionalidade desenvolvida é responsável por:

- Somar os valores dos itens do pedido  
- Validar se o valor mínimo foi atingido  
- Garantir que os dados sejam válidos  

### 📏 Regras de negócio aplicadas:

- Total = soma dos itens  
- Se total < valor mínimo → erro  
- Lista vazia → erro  
- Preço negativo → erro  

---

## 🧪 4. Testes Unitários

Foram implementados 3 testes principais:

### ✔ Teste 1 – Sucesso
Valida se o cálculo do total funciona corretamente quando o valor mínimo é atingido.

### ✔ Teste 2 – Erro (valor mínimo)
Verifica se o sistema lança erro quando o pedido não atinge o valor mínimo.

### ✔ Teste 3 – Erro (lista vazia)
Garante que o sistema não aceita pedidos sem itens.

---

## 🔁 5. Aplicação do TDD

### 🔴 RED
Os testes foram escritos antes da implementação.

Resultado:
- Todos os testes falharam (comportamento esperado)

---

### 🟢 GREEN
Foi criada uma implementação mínima para passar nos testes.

Resultado:
- Parte dos testes passou  
- Alguns erros ainda não tratados  

---

### 🔵 REFACTOR
O código foi melhorado para atender todos os cenários.

Resultado:
- Todos os testes passaram com sucesso  

---

## 🔄 6. Refatoração

Durante a etapa de refatoração, foram realizadas as seguintes melhorias:

- Validação de lista vazia  
- Tratamento de valores inválidos  
- Uso de boas práticas de código  
- Melhor organização da lógica  
- Aumento da legibilidade  

---

## 📊 7. Resultados

- Total de testes: 3  
- Testes aprovados: 3  
- Testes reprovados: 0  

### 📈 Cobertura:
- Aproximadamente 100% das regras críticas testadas  

---

## 📸 8. Evidências

As evidências incluem:

- Logs de execução dos testes  
- Resultado do pytest  
- Simulação do ciclo TDD  
- Validação de cenários reais  

---

## 💭 9. Reflexão

### Foi difícil escrever testes antes do código?
Sim, pois exige planejamento e compreensão da regra antes da implementação.

---

### O TDD ajudou no desenvolvimento?
Sim, o TDD guiou a construção da solução e evitou erros.

---

### Os testes aumentaram a confiança no código?
Sim, pois garantem que alterações futuras não quebrem o sistema.

---

### O que poderia ser melhorado?
- Adicionar mais cenários de teste  
- Implementar testes em outras funcionalidades  
- Melhorar cobertura com testes adicionais  

---

### Impacto no projeto
- Código mais seguro  
- Redução de bugs  
- Facilidade de manutenção  
- Maior qualidade geral  

---

## 🚀 10. Conclusão

A aplicação de testes unitários e TDD mostrou-se essencial para garantir a qualidade do sistema.

O desenvolvimento orientado por testes permite criar códigos mais confiáveis, organizados e preparados para evolução.

---

## 🟢 Considerações Finais

A utilização de boas práticas como TDD e testes automatizados é fundamental tanto no contexto acadêmico quanto profissional.

Este trabalho demonstra a importância de validar regras de negócio de forma contínua e automatizada.

---

## 💡 Frase Final

> “Se o código mudar amanhã, os testes garantem que nada quebre.”