import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Modelagem import Atividade
import MergeSort as ms

# Busca binária: retorna índice (base 1) da última atividade compatível com lista[j]
def p(lista, j):
    inicio = lista[j].inicio
    esquerda, direita = 0, j - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio].fim <= inicio:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return direita + 1

# Monta a tabela OPT iterativamente
def montar_tabela(lista):
    n = len(lista)
    tabela = [0] * (n + 1)
    for j in range(1, n + 1):
        peso = lista[j - 1].get('prioridade') * lista[j - 1].get('participantes')
        tabela[j] = max(peso + tabela[p(lista, j - 1)], tabela[j - 1])
    return tabela

# Reconstrói o conjunto de atividades via backtracking na tabela OPT
def reconstruir(lista, tabela, j=None):
    if j is None:
        j = len(lista)
    if j == 0:
        return []
    peso = lista[j - 1].get('prioridade') * lista[j - 1].get('participantes')
    pj = p(lista, j - 1)
    if peso + tabela[pj] >= tabela[j - 1]:
        return reconstruir(lista, tabela, pj) + [lista[j - 1]]
    else:
        return reconstruir(lista, tabela, j - 1)

# O algoritmo de seleção em sí
def weighted_interval_scheduling(lista):
    ordenada = ms.mergeSort(lista, 'fim')
    tabela = montar_tabela(ordenada)
    selecionadas = reconstruir(ordenada, tabela)
    quantidade = len(selecionadas)
    soma_prioridades = sum(a.prioridade for a in selecionadas)
    soma_participantes = sum(a.participantes for a in selecionadas)
    return selecionadas, quantidade, soma_prioridades, soma_participantes

# Mede o tempo de execução
def executar_com_tempo(lista):
    inicio = time.perf_counter()
    resultado = weighted_interval_scheduling(lista)
    fim = time.perf_counter()
    return resultado, fim - inicio
