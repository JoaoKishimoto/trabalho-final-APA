import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Modelagem import Atividade
from MergeSort import mergeSort


# Busca por codigo (linear ou binaria apos ordenacao)
def busca_por_codigo(lista, codigo):
    # Ordena por codigo para busca binaria
    ordenadas = mergeSort(lista, "codigo")

    esquerda, direita = 0, len(ordenadas) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if ordenadas[meio].codigo == codigo:
            return ordenadas[meio]
        elif ordenadas[meio].codigo < codigo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None


# Busca por nome (substring)
def busca_por_nome(lista, termo):
    termo_lower = termo.lower()
    return [a for a in lista if termo_lower in a.nome.lower()]


# Exibicao formatada em tabela
def exibir_tabela(lista):
    if not lista:
        print("Nenhuma atividade encontrada.")
        return

    # Cabecalho
    print("\n" + "=" * 75)
    print(f"{'Código':<8} {'Nome':<30} {'Início':>7} {'Fim':>5} {'Prior.':>7} {'Partic.':>8}")
    print("=" * 75)

    # Linhas
    for a in lista:
        print(f"{a.codigo:<8} {a.nome:<30} {a.inicio:>6}h {a.fim:>4}h {a.prioridade:>7} {a.participantes:>8}")

    print("=" * 75)
    print(f"Total: {len(lista)} atividade(s)")
