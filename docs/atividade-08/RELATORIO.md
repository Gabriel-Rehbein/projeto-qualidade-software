# Centro Universitário Senac-RS
### ADS - Análise e Desenvolvimento de Sistemas
**Unidade Curricular:** Qualidade de Software  
**Prof.:** Luciano Zanuz  
**Acadêmico:** Gabriel Menezes Rehbein

---

## 🧩 Atividade PBL – Aula 12: BDD e Automação Orientada a Comportamento

## 🔹 1. Fluxo escolhido
* **Fluxo Selecionado:** 🔎 1. Busca de restaurantes
* **O que faz:** Permite ao usuário pesquisar termos textuais ou categorias de culinária para filtrar os restaurantes disponíveis na listagem da plataforma.
* **Problema que resolve:** Elimina a necessidade de rolagem infinita por parte do usuário, otimizando o tempo de descoberta e melhorando a experiência de conversão (UX).
* **Importância:** É um fluxo de alta criticidade operacional. Se o mecanismo de busca quebrar ou trouxer dados inconsistentes, o usuário assume que a plataforma não tem opções e a abandona.

---

## 🔹 2. Escrita dos cenários BDD
Os cenários foram documentados utilizando a linguagem Gherkin, abstraindo detalhes de implementação técnica e focando estritamente na regra de negócio.

**Caminho do arquivo:** `features/busca_restaurantes.feature`
```gherkin
Feature: Busca de restaurantes
  Como um usuário com fome
  Quero pesquisar por termos ou tipos de culinária
  Para encontrar restaurantes específicos rapidamente

  Scenario: Busca por termo válido retornando resultados
    Given que o usuário está na página inicial do LocalEats
    When pesquisar pelo termo "Sabor"
    Then o sistema deve exibir os restaurantes correspondentes ao termo buscado

  Scenario: Busca por termo inexistente retornando vazio
    Given que o usuário está na página inicial do LocalEats
    When pesquisar pelo termo "RestauranteInexistenteXYZ"
    Then o sistema deve exibir uma mensagem informando que nenhum restaurante foi encontrado