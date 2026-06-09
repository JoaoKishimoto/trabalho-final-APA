import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Modelagem import Atividade, carregar_dados_teste

# T3.1 - Seleciona o maior numero de atividades sem conflito usando estrategia gulosa
def selecao_gulosa(atividades):
    ordenadas = sorted(atividades, key=lambda a: a.fim)
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

# Exibe o resultado da selecao gulosa
def exibir_resultado(selecionadas, quantidade, soma_prioridades, soma_participantes, tempo):
    print(f"\nAtividades selecionadas ({quantidade}):")
    for a in selecionadas:
        print(" ", a)
    print(f"\nSoma de prioridades: {soma_prioridades}")
    print(f"Soma de participantes: {soma_participantes}")
    print(f"Tempo de execucao: {tempo:.6f}s")

if __name__ == "__main__":
    atividades = carregar_dados_teste()
    (selecionadas, qtd, prio, partic), tempo = executar_com_tempo(atividades)
    exibir_resultado(selecionadas, qtd, prio, partic, tempo)