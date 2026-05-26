# features/busca_restaurantes.feature
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