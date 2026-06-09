import os
import json
import Modelagem
from clear import clear_cmd

def adicionar_atividades(lista):
    while True:
        print("Gerenciador de Tarefas - Adicionar Atividade")
        print("1 - Input (ideal para 1 ou 2 atividades)")
        print("2 - Arquivo .txt (ideal para mais atividades)")
        print("3 - Voltar")
        resposta = int(input("Como você deseja adicionar a atividade?\n"))
        clear_cmd()
        match(resposta):
            case(1):
                return add_input(lista)
            case(2):
                return add_txt(lista)
            case(3):
                return lista
            case():
                print('input inválido')


def add_input(lista):
    codigo = input("Qual o código da atividade?\n")
    nome = input("Qual o nome da atividade?\n")
    inicio = int(input("Qual o horário de início da atividade? (formato sem ':' exemplo: '23:59'->'2359')\n"))
    while (inicio > 2359 or inicio < 0 or inicio % 100 > 59):
        print("valor inválido")
        inicio = input("Qual o horário de início da atividade? (formato sem ':' exemplo: '23:59'->'2359')\n")
    
    fim = int(input("Qual o horário de fim da atividade? (formato sem ':' exemplo: '23:59'->'2359')\n"))
    while fim > 2359 or fim < 0 or fim % 100 > 59 or fim < inicio:
        if (fim > inicio):
            print("valor inválido")
            fim = input("Qual o horário de fim da atividade? (formato sem ':' exemplo: '23:59'->'2359')\n")
        else:
            print("Error: a atividade deve finalizar após o inicio")
            fim = input("Qual o horário de fim da atividade? (formato sem ':' exemplo: '23:59'->'2359')\n")
             
    prioridade = int(input("Qual a prioridade da atividade? (0 a 10)\n"))
    while prioridade < 0 or prioridade > 10:
        print("Valor Inválido")
        prioridade = int(input("Qual a prioridade da Atividade? (0 a 10)\n"))
    

    participantes = int(input("Quantas pessoas podem participar da atividade?\n"))
    while participantes < 0:
        print("valor inválido, deve ser maior que zero")
        participantes = int(input("Quantas pessoas podem participar da atividade?\n"))

    clear_cmd()
    lista.append(Modelagem.Atividade(codigo, nome, inicio, fim, prioridade, participantes))
    again = str.capitalize(input("Atividade adicionada! Adicionar mais uma? (s/N)\n"))
    if again == "S": add_input(lista)
    return lista

def add_txt(lista):
    print("Para que o arquivo funcione deve conter nele uma lista de objetos no seguinte formato em JSON:")
    print('{"codigo": "str", "nome": "str", "inicio": int ou "str", "fim": int ou "str", "prioridade": int, "participantes": int}')
    path = input("Qual o caminho relativo do arquivo a ser lido?\n")
    clear_cmd()
    with open(path, 'r') as arquivo:
        for linha in arquivo.readlines():
            dict = json.loads(linha)
            lista.append(Modelagem.Atividade(dict['codigo'], dict['nome'], dict['inicio'], dict['fim'], dict['prioridade'], dict['participantes']))
    return lista
