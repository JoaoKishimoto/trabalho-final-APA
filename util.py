import os

def clear_cmd():
    # 'nt' indica o sistema operacional Windows
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

def exibir_resultado(selecionadas, quantidade, soma_prioridades, soma_participantes, tempo):
    print(f"\nAtividades selecionadas ({quantidade}):")
    for a in selecionadas:
        print(" ", a)
    print(f"\nSoma de prioridades: {soma_prioridades}")
    print(f"Soma de participantes: {soma_participantes}")
    print(f"Tempo de execucao: {tempo:.6f}s\n")

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
