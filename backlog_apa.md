# 📋 Sistema de Agendamento de Atividades — Backlog

> **Disciplina:** Análise e Projeto de Algoritmos (APA)
> **Instituição:** Universidade Federal da Bahia · Instituto de Computação
> **Professora (PO):** Dra. Larissa Barbosa Leôncio Pinheiro
> **Documento gerado por:** João Kishimoto e Ivan Souza

---

## 🎯 ÉPICO

**[EPIC-01] Sistema de Agendamento de Atividades com Comparação entre Algoritmo Guloso e Programação Dinâmica**

Desenvolver um sistema em Python (ou C) que permita cadastrar atividades, organizá-las com Merge Sort, selecionar o conjunto ótimo de atividades sem conflito de horário usando duas abordagens (Guloso Clássico e Programação Dinâmica com pesos), e comparar o desempenho entre elas.

### Critérios de Aceite do Épico

- [ ] Sistema compila/executa sem erros
- [ ] Implementa Merge Sort, Guloso e PD
- [ ] Testa com 3 conjuntos (pequeno, médio, grande)
- [ ] Entrega: código + slides + documento + .zip

---

## 📚 STORIES e TASKS

### 🟦 STORY 1 — Modelagem de Dados e Cadastro de Atividades

> Como usuário, quero cadastrar atividades com seus atributos para que o sistema possa processá-las.

| ID | Task | Descrição | Estimativa |
|------|------|-----------|------------|
| T1.1 | Criar classe/struct `Atividade` | Campos: código, nome, início, fim, prioridade, participantes | 1h |
| T1.2 | Implementar função de cadastro manual | Input via terminal ou função `adicionar()` | 1h |
| T1.3 | Implementar carga de atividades via lista/arquivo | Para os 3 conjuntos de teste | 2h |
| T1.4 | Validação de dados | Fim > início, prioridade ≥ 0, etc. | 1h |

---

### 🟦 STORY 2 — Ordenação com Merge Sort

> Como sistema, preciso ordenar atividades por diferentes critérios usando Merge Sort.

| ID | Task | Descrição | Estimativa |
|------|------|-----------|------------|
| T2.1 | Implementar Merge Sort genérico | Receber lista + função de comparação (key) | 2h |
| T2.2 | Ordenação por horário de início | Wrapper sobre o Merge Sort | 0.5h |
| T2.3 | Ordenação por horário de término | **Crítico para o Guloso** | 0.5h |
| T2.4 | Ordenação por prioridade | Wrapper sobre o Merge Sort | 0.5h |
| T2.5 | Testes unitários do Merge Sort | Validar estabilidade e correção | 1h |

> ⚠️ **Atenção:** A ordenação por horário de **término** é a chave do algoritmo guloso clássico. Não pode usar `sorted()` do Python — tem que ser Merge Sort feito à mão.

---

### 🟦 STORY 3 — Algoritmo Guloso Clássico

> Como sistema, quero selecionar o maior número de atividades sem conflito usando estratégia gulosa.

| ID | Task | Descrição | Estimativa |
|------|------|-----------|------------|
| T3.1 | Implementar `selecao_gulosa(atividades)` | Após ordenar por fim, escolher sempre a próxima compatível | 2h |
| T3.2 | Retornar conjunto selecionado + métricas | Quantidade, soma de prioridades, soma de participantes | 1h |
| T3.3 | Medir tempo de execução | `time.perf_counter()` | 0.5h |

---

### 🟦 STORY 4 — Programação Dinâmica com Pesos

> Como sistema, quero maximizar o benefício total (não apenas a quantidade) usando PD.

| ID | Task | Descrição | Estimativa |
|------|------|-----------|------------|
| T4.1 | Implementar busca binária `p(j)` | Última atividade compatível antes de j | 2h |
| T4.2 | Implementar `weighted_interval_scheduling` | Tabela DP: `OPT[j] = max(peso[j]+OPT[p(j)], OPT[j-1])` | 3h |
| T4.3 | Reconstruir conjunto solução | Backtracking na tabela DP | 2h |
| T4.4 | Permitir escolher peso | Prioridade OU número de participantes OU combinação | 1h |
| T4.5 | Medir tempo de execução | `time.perf_counter()` | 0.5h |

---

### 🟦 STORY 5 — Busca e Organização

> Como usuário, quero buscar atividades e visualizar de forma organizada.

| ID | Task | Descrição | Estimativa |
|------|------|-----------|------------|
| T5.1 | Busca por código | Linear ou binária após ordenação | 1h |
| T5.2 | Busca por nome (substring) | Filtro simples | 0.5h |
| T5.3 | Exibição formatada em tabela | Print bonito no terminal | 1h |

---

### 🟦 STORY 6 — Comparação entre Abordagens

> Como avaliador, quero comparar Guloso vs PD em quantidade, benefício e tempo.

| ID | Task | Descrição | Estimativa |
|------|------|-----------|------------|
| T6.1 | Tabela comparativa de resultados | Nº atividades, soma de pesos, tempo (ms) | 2h |
| T6.2 | Executar nos 3 conjuntos de teste | Pequeno (5–8), Médio (10–20), Grande (30+) | 2h |
| T6.3 | Gerar gráfico (opcional, mas recomendado) | matplotlib — barras comparativas | 2h |
| T6.4 | Análise de complexidade (teórica) | Guloso O(n log n), PD O(n log n) com busca binária | 1h |

---

### 🟦 STORY 7 — Entregáveis e Documentação

> Como aluno, preciso entregar todos os artefatos exigidos.

| ID | Task | Descrição | Estimativa |
|------|------|-----------|------------|
| T7.1 | Comentar o código todo | Docstrings nas funções principais | 2h |
| T7.2 | Escrever documento da solução | Descrição, algoritmos, comparação, exemplos I/O | 3h |
| T7.3 | Criar slides da apresentação | 10–15 slides | 3h |
| T7.4 | Compactar tudo em `.zip` | Estrutura organizada de pastas | 0.5h |
| T7.5 | Ensaio da apresentação | Verificar se roda na hora | 1h |

---

## 📐 Resumo de Estimativa Total

**Aproximadamente 38–42 horas de trabalho.**

Recomendo dividir em sprints de 1 semana, priorizando Stories 1 → 2 → 3 → 4 (core) antes das 5, 6 e 7.

### Sugestão de Sprints

| Sprint | Stories | Foco |
|--------|---------|------|
| Sprint 1 (semana 1) | Stories 1 e 2 | Modelagem + Merge Sort |
| Sprint 2 (semana 2) | Stories 3 e 5 | Guloso + Busca |
| Sprint 3 (semana 3) | Story 4 | Programação Dinâmica (mais difícil — reserve mais tempo) |
| Sprint 4 (semana 4) | Stories 6 e 7 | Comparação, documentação, slides, .zip |
