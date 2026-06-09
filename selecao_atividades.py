import AlgoritmoGuloso
import AlgoritmoDinamico
from util import clear_cmd, exibir_resultado, print_table

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
                (selecionadas_G, quantidade_G, soma_prioridades_G, soma_participantes_G), tempo_G = AlgoritmoGuloso.executar_com_tempo(lista)
                (selecionadas_D, quantidade_D, soma_prioridades_D, soma_participantes_D), tempo_D = AlgoritmoDinamico.executar_com_tempo(lista)
                print_table(['Algoritmo', 'Soma Prioridades', 'Soma Participantes', 'Tempo'], [
                    ['Guloso', soma_prioridades_G, soma_participantes_G, tempo_G],
                    ['Dinâmico', soma_prioridades_D, soma_participantes_D, tempo_D]
                ])
                if (soma_prioridades_D > soma_prioridades_G):
                    print(f"O algoritmo Dinâmico foi melhor na seleção do cronograma por {soma_prioridades_D - soma_prioridades_G} pontos de prioridade")
                else:
                    print(f"O algoritmo Guloso foi melhor na seleção do cronograma por {soma_prioridades_G - soma_prioridades_D} pontos de prioridade")
                if (tempo_D > tempo_G):
                    print(f"O algoritmo Guloso foi melhor no tempo por {tempo_D - tempo_G}s")
                else:
                    print(f"O algoritmo Dinâmico foi melhor no tempo por {tempo_G - tempo_D}s")
                return
            case():
                continue