import os
import Modelagem
from adicionar_atividades import adicionar_atividades
from organizar_atividades import organizar_atividades
from clear import clear_cmd

def start():
    lista_atividades = []
    sair = False
    while not sair:
        print("Bem vindo(a) ao Gerenciador de Atividades")
        print("1 - Adicionar atividades")
        print("2 - Organizar as atividades")
        print("3 - Mostrar as atividades")
        print("4 - Sair")
        resposta = input("O que você deseja fazer?\n")
        clear_cmd()
        match(resposta):
            case('1'):
                lista_atividades = adicionar_atividades(lista_atividades)
                continue
            case('2'):
                lista_atividades = organizar_atividades(lista_atividades)
                continue
            case('3'):
                Modelagem.listar(lista_atividades)
                continue
            case('4'):
                break
            case():
                continue

start()