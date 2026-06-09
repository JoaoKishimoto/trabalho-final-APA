import os

def __init__():
    lista_atividades = []
    start()

def start():
    print("Bem vindo(a) ao Gerenciador de Atividades")
    print("1 - Adicionar atividades")
    print("2 - Organizar as atividades")
    print("3 - Sair")
    resposta = input("O que você deseja fazer? ")
    limpar_terminal()
    print(resposta)



def limpar_terminal():
    # 'nt' indica o sistema operacional Windows
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

__init__()