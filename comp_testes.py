from util import clear_cmd, compare_algoriths
import Modelagem
import MergeSort as ms
import json


def comp_testes():
    lista = []
    print("1 - Testar os algoritmos com 6 atividades")
    print("2 - Testar os algoritmos com 20 atividades")
    print("3 - Testar os algoritmos com 50 atividades")
    print("0 - Voltar")
    print("Todos os testes possuem comparação entre os algoritmos")
    resposta = input("Qual teste você deseja realizar?\n")
    clear_cmd()
    while True:
        match(resposta):
            case('0'):
                return
            case('1'):
                teste(lista, 'Teste/listaP.txt')
                return
            case('2'):
                teste(lista, 'Teste/listaM.txt')
                return
            case('3'):
                teste(lista, 'Teste/listaG.txt')
                return
            case():
                continue
        print('Valor Inválido')


def teste(lista, path):
    # Carrega as atividades na lista
    with open(path, 'r') as arquivo:
        for linha in arquivo.readlines():
            dict = json.loads(linha)
            lista.append(Modelagem.Atividade(dict['codigo'], dict['nome'], dict['inicio'], dict['fim'], dict['prioridade'], dict['participantes']))
    
    # Ordena baseado em end
    ms.mergeSort(lista, 'fim')

    # Roda os algoritmos e os compara
    compare_algoriths(lista)
