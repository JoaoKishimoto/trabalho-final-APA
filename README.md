# Gerenciador de Atividades — APA

Sistema de gerenciamento de atividades com ordenação, busca e seleção otimizada por algoritmos clássicos de APA (Análise e Projeto de Algoritmos).

## Como executar

```bash
python main.py
```

Não há dependências externas — apenas Python 3.10+.

---

## Menu principal

```
1 - Adicionar atividades
2 - Organizar as atividades
3 - Mostrar as atividades
4 - Busca
5 - Seleção de atividades
6 - Comparação e testes
0 - Sair
```

---

## Funcionalidades

### 1 — Adicionar atividades

Duas formas de entrada:

- **Input manual:** digita cada campo (código, nome, horário de início, horário de fim, prioridade, participantes) direto no terminal.
- **Arquivo `.txt`:** lê um arquivo onde cada linha é um objeto JSON com os campos acima.

Formato esperado do arquivo:

```json
{"codigo": "A001", "nome": "Reuniao de planejamento", "inicio": 800, "fim": 1000, "prioridade": 1, "participantes": 5}
```

Os horários seguem o formato `HHMM` sem separador (ex: `1430` = 14:30). Arquivos de teste prontos estão em `Teste/`.

---

### 2 — Organizar atividades

Ordena a lista atual usando **Merge Sort** (`MergeSort/`) por um dos campos:

| Opção | Campo             |
|-------|-------------------|
| 1     | Horário de início |
| 2     | Horário de fim    |
| 3     | Prioridade        |
| 4     | Participantes     |

**Complexidade:** O(n log n).

---

### 3 — Mostrar atividades

Exibe todas as atividades da lista atual no terminal.

---

### 4 — Busca

Dois modos de busca (`Busca/`):

#### Por código — Merge Sort + Busca Binária

1. Ordena a lista por código via Merge Sort: O(n log n).
2. Aplica busca binária sobre a lista ordenada: O(log n).

A comparação de strings funciona corretamente porque todos os códigos seguem o padrão `[Letra][3 dígitos]` (ex: `A001`, `B012`), onde a ordem lexicográfica coincide com a ordem esperada.

#### Por nome — Busca linear (substring)

Percorre toda a lista e retorna as atividades cujo nome contém o termo buscado (case-insensitive): O(n).

---

### 5 — Seleção de atividades

Dado o conjunto atual de atividades, seleciona um subconjunto sem conflitos de horário, maximizando algum critério. Dois algoritmos disponíveis:

#### Algoritmo Guloso (`AlgoritmoGuloso/`)

Estratégia: ordenar pelo horário de fim e selecionar gananciosamente a próxima atividade compatível.

- Maximiza a **quantidade** de atividades selecionadas.
- Não garante maximização de prioridade.
- **Complexidade:** O(n log n) — dominado pela ordenação.

#### Algoritmo Dinâmico — Weighted Interval Scheduling (`AlgoritmoDinamico/`)

Estratégia: programação dinâmica com backtracking para encontrar o conjunto de maior soma de prioridades sem conflito.

1. Ordena as atividades pelo horário de fim via Merge Sort.
2. Para cada atividade `j`, usa busca binária para encontrar a última atividade compatível `p(j)` (aquela que termina antes de `j` começar).
3. Monta a tabela `OPT[j] = max(prioridade[j] + OPT[p(j)], OPT[j-1])` iterativamente.
4. Reconstrói o conjunto ótimo por backtracking na tabela.

- Maximiza a **soma de prioridades** das atividades selecionadas.
- Solução globalmente ótima.
- **Complexidade:** O(n log n) — ordenação + busca binária por elemento.

#### Comparar os dois

Executa ambos os algoritmos sobre a mesma lista e exibe os resultados lado a lado com o tempo de execução de cada um.

---

### 6 — Comparação e testes

Carrega um dos conjuntos de teste prontos e executa automaticamente a comparação entre os dois algoritmos:

| Opção | Arquivo             | Tamanho |
|-------|---------------------|---------|
| 1     | `Teste/listaP.txt`  | 6 atividades  |
| 2     | `Teste/listaM.txt`  | 20 atividades |
| 3     | `Teste/listaG.txt`  | 50 atividades |

---

## Estrutura do projeto

```
.
├── main.py                    # Ponto de entrada — menu principal
├── adicionar_atividades.py    # Lógica de adição (input / arquivo)
├── organizar_atividades.py    # Menu de ordenação por campo
├── selecao_atividades.py      # Menu de seleção de atividades
├── pg_busca.py                # Menu de busca
├── comp_testes.py             # Carrega arquivos de teste e compara algoritmos
├── util.py                    # Utilitários (clear, exibição de resultados)
│
├── Modelagem/                 # Classe Atividade e funções auxiliares
├── MergeSort/                 # Implementação do Merge Sort genérico
├── Busca/                     # Busca por código (binária) e por nome (linear)
├── AlgoritmoGuloso/           # Seleção gulosa de intervalos
├── AlgoritmoDinamico/         # Weighted Interval Scheduling (DP)
│
└── Teste/
    ├── listaP.txt             # 6 atividades
    ├── listaM.txt             # 20 atividades
    └── listaG.txt             # 50 atividades
```

---

## Complexidade resumida

| Operação                        | Algoritmo              | Complexidade  |
|---------------------------------|------------------------|---------------|
| Ordenação                       | Merge Sort             | O(n log n)    |
| Busca por código                | Merge Sort + Binária   | O(n log n)    |
| Busca por nome                  | Linear (substring)     | O(n)          |
| Seleção — Guloso                | Greedy + Merge Sort    | O(n log n)    |
| Seleção — Dinâmico              | DP + Busca Binária     | O(n log n)    |
