import os
import AlgoritmoGuloso
import AlgoritmoDinamico

# limpa o terminal para que ele não fique poluído
def clear_cmd():
    # 'nt' indica o sistema operacional Windows
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

#mostra os resultados de um algoritmo individual
def exibir_resultado(selecionadas, quantidade, soma_prioridades, soma_participantes, tempo):
    print(f"\nAtividades selecionadas ({quantidade}):")
    for a in selecionadas:
        print(" ", a)
    print(f"\nSoma de prioridades: {soma_prioridades}")
    print(f"Soma de participantes: {soma_participantes}")
    print(f"Tempo de execucao: {tempo:.6f}s\n")

# imprime uma tabela bonita e legível
def print_table(headers, rows):
    widths = [max(len(str(r[i])) for r in [headers] + rows) for i in range(len(headers))]

    top    = "┌" + "┬".join("─" * (w + 2) for w in widths) + "┐"
    sep    = "├" + "┼".join("─" * (w + 2) for w in widths) + "┤"
    bottom = "└" + "┴".join("─" * (w + 2) for w in widths) + "┘"

    def row_line(row):
        return "│" + "│".join(f" {str(v):<{w}} " for v, w in zip(row, widths)) + "│"

    print(top)
    print(row_line(headers))
    print(sep)
    for row in rows:
        print(row_line(row))
    print(bottom)

# compara os algoritmos, mostra as atividades selecionadas, os resultados e compara eles
def compare_algoriths(lista):
    (selecionadas_G, quantidade_G, soma_prioridades_G, soma_participantes_G), tempo_G = AlgoritmoGuloso.executar_com_tempo(lista)
    (selecionadas_D, quantidade_D, soma_prioridades_D, soma_participantes_D), tempo_D = AlgoritmoDinamico.executar_com_tempo(lista)

    print_table(['Algoritmo', 'n de Atividades','Soma Pesos', 'Tempo (ms)'], [
        ['Guloso', quantidade_G, soma_prioridades_G*soma_participantes_G, format((tempo_G * 1000), ".3f")],
        ['Dinâmico', quantidade_D, soma_prioridades_D*soma_participantes_D, format((tempo_D * 1000), ".3f")]
    ])
    print()
    if (soma_prioridades_D * soma_participantes_D > soma_prioridades_G * soma_participantes_G):
        print(f"O algoritmo Dinâmico foi melhor na seleção do cronograma por {soma_prioridades_D * soma_participantes_D - soma_prioridades_G * soma_participantes_G} pontos de peso")
    else:
        print(f"O algoritmo Guloso foi melhor na seleção do cronograma por {soma_prioridades_G * soma_participantes_G - soma_prioridades_D * soma_participantes_D} pontos de peso")
    if (tempo_D > tempo_G):
        print(f"O algoritmo Guloso foi melhor no tempo por {format(((tempo_D - tempo_G) * 1000), ".3f")}ms\n")
    else:
        print(f"O algoritmo Dinâmico foi melhor no tempo por {format(((tempo_G - tempo_D) * 1000), ".3f")}ms\n")
    return