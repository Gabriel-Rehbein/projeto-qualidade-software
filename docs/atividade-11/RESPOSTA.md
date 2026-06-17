# Qualidade em Metodologias Ágeis – LocalEats

## 1. Análise de Práticas Ágeis no Processo

Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada?
--- | --- | --- | ---
Planejamento iterativo | Parcial | A equipe organiza tarefas em ciclos curtos quando há tempo, mas não há sprints formais definidos. | Sim
Priorização de funcionalidades | Parcial | As funcionalidades são escolhidas conforme a necessidade percebida, mas não há critérios claros de priorização. | Sim
Entregas incrementais | Sim | O projeto é desenvolvido em partes que vão sendo entregues conforme são implementadas. | Sim
Feedback frequente | Parcial | Há alguns retornos entre integrantes, mas o feedback não é formalizado em revisões ou demos regulares. | Sim
Trabalho colaborativo | Sim | O grupo divide atividades e compartilha tarefas, mas ainda falta colaboração estruturada em pares ou reuniões diárias. | Sim
Controle visual das atividades | Parcial | Os itens estão no repositório e há organização básica, mas não existe um quadro Kanban ou similar bem mantido. | Sim
Melhoria contínua | Parcial | A equipe reflete informalmente sobre o desenvolvimento, mas não realiza retrospectivas regulares com registros de melhorias. | Sim

### Conclusão
O processo do LocalEats já utiliza elementos ágeis como entregas incrementais e colaboração entre integrantes, mas ainda falta disciplina em suas práticas. A priorização e o planejamento iterativo existem de forma improvisada, e a falta de controle visual e retrospectivas reduz a visibilidade do progresso. Formalizar reuniões curtas, critérios de prontidão e conclusão, e incorporar feedback contínuo tornaria o desenvolvimento mais ágil e previsível.

## 2. Propostas de Melhoria Ágil

Melhoria Proposta | Metodologia Relacionada | Benefício Esperado
--- | --- | ---
Adotar um quadro Kanban para acompanhar tarefas | Kanban | Mais visibilidade e controle do fluxo de trabalho, facilitando identificar bloqueios.
Realizar planejamentos curtos e revisões de backlog | Scrum | Maior clareza sobre prioridades e melhor organização das entregas.
Estabelecer reuniões rápidas de alinhamento diário | Scrum | Reduz mal-entendidos, aumenta a sincronização e acelera a resolução de impedimentos.
Praticar retrospectivas ao fim de cada ciclo | Lean/XP | Permite identificar lições aprendidas e melhorar continuamente o processo.
Implementar pares em revisão ou programação conjunta | XP | Aumenta a qualidade do código e compartilha conhecimento entre membros do time.

## 3. Definition of Ready (DoR)

- O requisito possui descrição clara e critérios de aceitação definidos.
- A funcionalidade está priorizada no backlog e alinhada com os objetivos do projeto.
- A tarefa tem dependências identificadas e bloqueios conhecidos foram removidos.
- Os dados, layouts e regras de negócio necessários estão documentados.
- O escopo da funcionalidade pode ser entregue em um ciclo curto e é pequeno o suficiente para ser implementado com confiança.
- Todas as dúvidas foram esclarecidas com a equipe ou o responsável pelo produto.

## 4. Definition of Done (DoD)

- A funcionalidade foi implementada e está funcionando conforme os critérios de aceitação.
- Os testes relevantes foram criados e executados com sucesso (unitários, de integração ou manuais).
- O código foi revisado por outro integrante e eventuais ajustes foram aplicados.
- A documentação mínima necessária foi atualizada (README, comentários, instruções de uso).
- Não existem erros conhecidos críticos ou bloqueadores antes da entrega.
- O código foi versionado no repositório e o commit contém mensagem clara sobre a entrega.
