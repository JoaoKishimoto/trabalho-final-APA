import MergeSort as ms
from clear import clear_cmd

def organizar_atividades(lista):
    end = False
    while not end:
        print("1 - Nome")
        print("2 - Horário de início")
        print("3 - Horário de Fim")
        print("4 - Prioridade")
        print("5 - Número de Participantes")
        print("6 - Código da Atividade")
        print("0 - Voltar")
        resposta = int(input("Você quer organizar as tarefas com base em que parâmetro?\n"))
        clear_cmd()
        match(resposta):
            case(1):
                return ms.mergeSort(lista, 'nome')
                end = True
                continue
            case(2):
                return ms.mergeSort(lista, 'inicio')
                end = True
                continue
            case(3):
                return ms.mergeSort(lista, 'fim')
                end = True
                continue
            case(4):
                return ms.mergeSort(lista, 'prioridade')
                end = True
                continue
            case(5):
                return ms.mergeSort(lista, 'participantes')
                end = True
                continue
            case(6):
                return ms.mergeSort(lista, 'codigo')
                end = True
                continue
            case(0):
                return
            case():
                continue
        print("Valor inválido, tente novamente")
            
