# 🚀 Qualidade de Software — 6º Semestre (Senac RS)

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?color=00F7FF&size=28&center=true&vCenter=true&width=800&lines=Qualidade+de+Software;Local+Eats;Testes+Automatizados;TDD+%7C+BDD+%7C+Testes+Funcionais;Senac+RS+-+ADS" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/SenacRS-ADS-blue?style=for-the-badge&logo=googleclassroom">
  <img src="https://img.shields.io/badge/Semestre-6º-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Disciplina-Qualidade%20de%20Software-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/PBL-Local%20Eats-purple?style=for-the-badge">
</p>

---

## 👨‍💻 Autor

**Gabriel Menezes Rehbein**  
📌 Matrícula: `842000137`

---

## 👥 Integrantes do Grupo

- Gabriel Menezes Rehbein
- Nome do integrante 2
- Nome do integrante 3

> Observação: apenas um integrante do grupo realizará o envio do link do repositório no ambiente solicitado.

---

## 🧠 Sobre o Projeto

Este repositório foi desenvolvido para a disciplina de **Qualidade de Software — 6º Semestre**, no curso de **Análise e Desenvolvimento de Sistemas — Senac RS**.

O projeto reúne as atividades do **PBL do Local Eats**, com foco em planejamento, documentação, implementação e validação de testes de software.

O objetivo principal é demonstrar a aplicação prática de técnicas de qualidade, incluindo:

- Testes unitários automatizados;
- Desenvolvimento orientado a testes, TDD;
- Testes funcionais automatizados;
- BDD, desenvolvimento orientado a comportamento;
- Planejamento e documentação de testes;
- Evidências de execução;
- Organização técnica dos artefatos.

---

## 📌 Atividades Avaliadas

As atividades avaliadas neste repositório são:

| PBL | Tema | Local no Repositório |
|---|---|---|
| PBL 6 | Testes Unitários Automatizados e TDD | `docs/atividade-06/` |
| PBL 7 | Testes Funcionais Automatizados | `docs/atividade-07/` |
| PBL 8 | BDD e automação orientada a comportamento | `docs/atividade-08/` |

---

# 🧪 PBL 6 — Testes Unitários Automatizados e TDD

O **PBL 6** tem como foco a criação de testes unitários automatizados utilizando práticas de **TDD — Test Driven Development**.

## Objetivos

- Planejar testes unitários para regras de negócio do sistema Local Eats;
- Criar testes antes ou junto da implementação da funcionalidade;
- Validar pequenas unidades do sistema de forma isolada;
- Garantir que funções, métodos e regras principais funcionem corretamente;
- Registrar evidências da execução dos testes.

## Técnicas Aplicadas

- Testes unitários;
- TDD;
- Validação de entradas;
- Verificação de resultados esperados;
- Separação entre regra de negócio e teste automatizado.

## Evidências Esperadas

- Arquivos de teste unitário;
- Prints ou registros da execução;
- Resultado dos testes aprovados;
- Documentação explicando o que foi testado.

---

# 🧪 PBL 7 — Testes Funcionais Automatizados

O **PBL 7** tem como foco a validação de funcionalidades completas do sistema Local Eats.

## Objetivos

- Testar fluxos reais de uso do sistema;
- Validar se as funcionalidades entregam o comportamento esperado;
- Automatizar cenários funcionais;
- Verificar entradas, saídas, mensagens e comportamentos do sistema;
- Registrar evidências da execução dos testes.

## Exemplos de Fluxos Testados

- Cadastro;
- Login;
- Busca de restaurantes;
- Cadastro de restaurante;
- Validação de dados obrigatórios;
- Respostas do sistema para dados válidos e inválidos.

## Técnicas Aplicadas

- Testes funcionais automatizados;
- Testes de fluxo;
- Validação de interface ou API;
- Verificação de comportamento esperado.

## Evidências Esperadas

- Scripts de testes funcionais;
- Prints da execução;
- Relatórios ou registros dos testes;
- Documentação dos cenários testados.

---

# 🧪 PBL 8 — BDD e Automação Orientada a Comportamento

O **PBL 8** tem como foco o uso de **BDD — Behavior Driven Development**, descrevendo os comportamentos esperados do sistema de forma clara e compreensível.

## Objetivos

- Criar cenários de teste usando linguagem natural;
- Descrever comportamentos do sistema com `Given`, `When` e `Then`;
- Aproximar a documentação técnica das regras de negócio;
- Automatizar cenários baseados no comportamento esperado;
- Registrar evidências dos testes BDD.

## Exemplo de Cenário BDD

```gherkin
Feature: Cadastro de restaurante no Local Eats

Scenario: Cadastro de restaurante com dados válidos
  Given que o usuário está na tela de cadastro de restaurante
  When ele preenche todos os dados obrigatórios corretamente
  Then o restaurante deve ser cadastrado com sucesso
```

## Técnicas Aplicadas

- BDD;
- Escrita de cenários em Gherkin;
- Automação orientada a comportamento;
- Validação de regras de negócio por cenário.

## Evidências Esperadas

- Arquivos `.feature`;
- Cenários BDD documentados;
- Scripts de automação;
- Registros de execução dos testes.

---

        
    📁 Estrutura do Projeto
    PROJETO-QUALIDADE-SOFTWARE/
    │
    ├── README.md
    ├── LICENSE
    │
    ├── artefatos/
    │   ├── diagramas/
    │   ├── evidencias/
    │   └── relatorios/
    │
    ├── docs/
    │   ├── atividade-01/
    │   ├── atividade-02/
    │   ├── atividade-03/
    │   ├── atividade-04/
    │   ├── atividade-05/
    │   ├── atividade-06/
    │   ├── atividade-07/
    │   ├── atividade-08/
    │   └── entregas-finais/
    │
    ├── referencias/
    │
    └── src/
    
🧩 Organização das Pastas
📂 docs/

Responsável por armazenar as atividades desenvolvidas ao longo do semestre.

Contém:

Atividades organizadas por número;
Documentações dos PBLs;
Respostas das atividades;
Materiais complementares;
Entregas finais.
📂 artefatos/

Responsável por armazenar os materiais técnicos do projeto.

Contém:

diagramas/ — modelagens, fluxos e representações técnicas;
evidencias/ — prints, registros e comprovações dos testes;
relatorios/ — documentos técnicos e relatórios estruturados.
📂 referencias/

Responsável por armazenar materiais de apoio utilizados durante o desenvolvimento das atividades.

Pode conter:

Links;
Materiais acadêmicos;
Referências sobre testes;
Conteúdos de apoio da disciplina.
📂 src/

Diretório reservado para implementação de código, quando aplicável ao projeto.

Pode conter:

Código-fonte do sistema;
Scripts de teste;
Funções testadas;
Implementações usadas nos PBLs.
⚙️ Como Executar o Projeto

Clone o repositório:

git clone https://github.com/Gabriel-Rehbein/projeto-qualidade-software.git

Acesse a pasta do projeto:

cd projeto-qualidade-software

Instale as dependências, caso o projeto possua ambiente Node.js:

npm install
🧪 Como Executar os Testes
Executar todos os testes
npm test
Executar testes unitários
npm run test:unit
Executar testes funcionais
npm run test:functional
Executar testes BDD
npm run test:bdd

Observação: os comandos podem variar conforme a configuração final do projeto e das ferramentas utilizadas.

📦 Entregas

As entregas estão organizadas em:

docs/atividade-06/
docs/atividade-07/
docs/atividade-08/
docs/entregas-finais/

Incluindo:

Documentação;
Evidências;
Imagens;
Prints;
Respostas;
Cenários de teste;
Relatórios de execução.
🧠 Metodologia
<p align="center"> <img src="https://img.shields.io/badge/PBL-Problem%20Based%20Learning-purple?style=for-the-badge"> </p>

O projeto segue a abordagem PBL — Problem Based Learning, com foco na resolução de problemas práticos por meio da aplicação de conceitos de qualidade de software.

A metodologia utilizada valoriza:

Resolução de problemas reais;
Testes e validação contínua;
Documentação estruturada;
Aplicação prática de qualidade de software;
Desenvolvimento incremental;
Evidências técnicas da aprendizagem.
🔥 Diferenciais do Repositório
Estrutura organizada e profissional;
Separação clara entre documentação, artefatos e código;
Evidências de testes;
Documentação voltada para avaliação por competências;
Relação direta com os elementos EC4 e EC5;
Aplicação de testes unitários, funcionais e BDD;
Preparado para avaliação acadêmica.
🧾 Versionamento

Padrão utilizado nos commits:

feat: nova funcionalidade
fix: correção de erro
docs: documentação
test: criação ou alteração de testes
refactor: melhoria de código
📌 Observação Final

Este repositório foi desenvolvido com foco em:

Clareza;
Organização;
Qualidade técnica;
Documentação acadêmica;
Evidências de testes;
Aplicação prática de qualidade de software.

O objetivo é demonstrar o atendimento às atividades do PBL do Local Eats, especialmente:

PBL 6 — Testes Unitários Automatizados e TDD;
PBL 7 — Testes Funcionais Automatizados;
PBL 8 — BDD e automação orientada a comportamento;
EC4 — Planejar e projetar testes selecionando técnicas adequadas;
EC5 — Implementar testes manuais e automatizados, incluindo TDD e BDD.
<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00F7FF,100:007CF0&height=120&section=footer"/> </p> ```