import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Modelagem import Atividade
import MergeSort as ms

# T3.1 - Seleciona o maior numero de atividades sem conflito usando estrategia gulosa
def selecao_gulosa(atividades):
    ordenadas = ms.mergeSort(atividades, 'fim')
    selecionadas = []
    ultimo_fim = 0
    for atividade in ordenadas:
        if atividade.inicio >= ultimo_fim:
            selecionadas.append(atividade)
            ultimo_fim = atividade.fim
    quantidade = len(selecionadas)
    soma_prioridades = sum(a.prioridade for a in selecionadas)
    soma_participantes = sum(a.participantes for a in selecionadas)
    return selecionadas, quantidade, soma_prioridades, soma_participantes

# T3.3 - Mede o tempo de execucao do algoritmo
def executar_com_tempo(atividades):
    inicio = time.perf_counter()
    resultado = selecao_gulosa(atividades)
    fim = time.perf_counter()
    tempo = fim - inicio
    return resultado, tempo