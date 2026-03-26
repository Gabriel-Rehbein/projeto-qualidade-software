# Estratégia Inicial de Testes - LocalEats



## 1. Funcionalidades Principais
Para a estabilização da plataforma, foram mapeadas as seguintes funcionalidades críticas:
* **Mecanismo de Busca e Filtros:** Localização, tipo de culinária e faixa de preço.
* **Exibição de Conteúdo:** Cardápios, fotos e informações dos restaurantes.
* **Sistema de Avaliações:** Persistência de notas, comentários e média de satisfação.
* **Sincronização de Perfil:** Favoritos e dados de conta integrados entre Web e Mobile.

## 2. Níveis de Teste
A abordagem será segmentada para atacar a causa raiz dos problemas reportados:

* **Teste Unitário:** Focar na lógica de filtragem e funções de tratamento de dados. 
    * *Por que:* Garantir que a lógica de busca retorne resultados coerentes e sem erros de script.
* **Teste de Integração:** Validar a comunicação entre as APIs do App/Web e o Banco de Dados. 
    * *Por que:* Resolver a falha onde avaliações desaparecem e garantir que o backend receba as fotos corretamente.
* **Teste de Sistema:** Validar fluxos ponta a ponta (E2E) em diferentes dispositivos. 
    * *Por que:* Corrigir a inconsistência de dados entre a versão web e mobile e falhas em smartphones específicos.
* **Teste de Aceitação:** Validar se os fluxos de usuário (ex: favoritar restaurante) são concluídos. 
    * *Por que:* Confirmar se a interface parou de ser "confusa" e se as ações simples foram simplificadas.

## 3. Prioridades e Riscos
As funcionalidades foram priorizadas com base no impacto direto ao negócio:

1.  **Prioridade 1: Disponibilidade e Performance (Busca):** A lentidão em horários de pico e resultados incorretos tornam o app inutilizável. É o maior risco de abandono da plataforma.
2.  **Prioridade 2: Integridade de Dados (Avaliações):** O desaparecimento de dados quebra a confiança da associação de comerciantes e dos usuários.
3.  **Prioridade 3: Experiência Omnichannel (Sincronia):** A divergência entre Web e Mobile gera suporte técnico e ruído operacional, mas é secundária à funcionalidade básica de busca.

## 4. Pirâmide de Testes
A estratégia de automação seguirá a seguinte distribuição:

* **Base (Testes Unitários/API - 70%):** Maior volume aqui para garantir estabilidade do código e velocidade na execução. É mais barato e resolve o problema de lógica da busca rapidamente.
* **Meio (Testes de Integração - 20%):** Foco em garantir que as camadas de dados e serviços estejam conectadas. Crucial para resolver o problema de persistência (avaliações).
* **Topo (Testes de UI/E2E - 10%):** Menor volume devido ao alto custo de manutenção. Focado apenas nos fluxos críticos (login e conclusão de busca) para validar a usabilidade.

## 5. Testes em Produção
O uso de testes em produção é indispensável para o cenário da LocalEats:

* **Situações:** Validação de carga (stress test) e compatibilidade em hardware real (smartphones variados).
* **Justificativa:** Como o sistema já está em produção e apresenta falhas sob demanda (picos), precisamos de monitoramento sintético e *feature flags* para validar correções em tempo real sem afetar toda a base de usuários simultaneamente.

---