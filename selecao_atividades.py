import AlgoritmoGuloso
import AlgoritmoDinamico
from util import clear_cmd, exibir_resultado, compare_algoriths

def selecao_atividades(lista):
    while True:
        print("1 - Algoritmo Guloso")
        print("2 - Algoritmo Dinâmico")
        print("3 - Comparar os 2 acima")
        print("0 - Voltar")
        resposta = input("Qual algoritmo você deseja utilizar?\n")
        clear_cmd()
        match(resposta):
            case('0'):
                return
            case('1'):
                (selecionadas, quantidade, soma_prioridades, soma_participantes), tempo = AlgoritmoGuloso.executar_com_tempo(lista)
                exibir_resultado(selecionadas, quantidade, soma_prioridades, soma_participantes, tempo)
                return
            case('2'):
                (selecionadas, quantidade, soma_prioridades, soma_participantes), tempo = AlgoritmoDinamico.executar_com_tempo(lista)
                exibir_resultado(selecionadas, quantidade, soma_prioridades, soma_participantes, tempo)
                return
            case('3'):
                compare_algoriths(lista)
                return
            case():
                continue