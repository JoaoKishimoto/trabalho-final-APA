import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Modelagem import Atividade, carregar_dados_teste


# T5.1 - Busca por codigo (linear ou binaria apos ordenacao)
def busca_por_codigo(atividades, codigo):
    # Ordena por codigo para busca binaria
    ordenadas = sorted(atividades, key=lambda a: a.codigo)

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


# T5.2 - Busca por nome (substring)
def busca_por_nome(atividades, termo):
    termo_lower = termo.lower()
    return [a for a in atividades if termo_lower in a.nome.lower()]


# T5.3 - Exibicao formatada em tabela
def exibir_tabela(atividades):
    if not atividades:
        print("Nenhuma atividade encontrada.")
        return

    # Cabecalho
    print("\n" + "=" * 75)
    print(f"{'Código':<8} {'Nome':<30} {'Início':>7} {'Fim':>5} {'Prior.':>7} {'Partic.':>8}")
    print("=" * 75)

    # Linhas
    for a in atividades:
        print(f"{a.codigo:<8} {a.nome:<30} {a.inicio:>6}h {a.fim:>4}h {a.prioridade:>7} {a.participantes:>8}")

    print("=" * 75)
    print(f"Total: {len(atividades)} atividade(s)")


if __name__ == "__main__":
    atividades = carregar_dados_teste()

    # Exibe todas em tabela
    print("\n--- Todas as atividades ---")
    exibir_tabela(atividades)

    # T5.1 - Busca por codigo
    codigo = input("\nDigite o codigo para buscar (ex: A001): ").strip()
    resultado = busca_por_codigo(atividades, codigo)
    print(f"\n--- Resultado da busca por codigo: '{codigo}' ---")
    if resultado:
        exibir_tabela([resultado])
    else:
        print("Atividade nao encontrada.")

    # T5.2 - Busca por nome
    termo = input("\nDigite o nome (ou parte do nome) para buscar: ").strip()
    resultados = busca_por_nome(atividades, termo)
    print(f"\n--- Resultado da busca por nome: '{termo}' ---")
    exibir_tabela(resultados)