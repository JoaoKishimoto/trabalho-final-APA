import MergeSort as ms
from util import clear_cmd

def organizar_atividades(lista):
    while True:
        print("1 - Horário de início")
        print("2 - Horário de Fim")
        print("3 - Prioridade")
        print("4 - Número de Participantes")
        print("0 - Voltar")
        resposta = int(input("Você quer organizar as tarefas com base em que parâmetro?\n"))
        clear_cmd()
        match(resposta):
            case(1):
                return ms.mergeSort(lista, 'inicio')
            case(2):
                return ms.mergeSort(lista, 'fim')
            case(3):
                return ms.mergeSort(lista, 'prioridade')
            case(4):
                return ms.mergeSort(lista, 'participantes')
            case(0):
                return
            case():
                print("Valor inválido, tente novamente")
                continue
            
