import os

def adicionar_atividades():
    while True:
        print("como você quer adicionar as atividades?")
        print("1 - Input (ideal para 1 ou 2 atividades)")
        print("2 - Arquivo .txt (ideal para mais atividades)")
        print("3 - Voltar")
        resposta = input("O que você deseja fazer? ")
        limpar_terminal()
        match(resposta):
            case('1'):
                add_input()
                break
            case('2'):
                add_txt()
                break
            case('3'):
                return

def add_input():
    codigo = input("Qual o código da atividade?")
    nome = input("Qual o nome da atividade?")
    inicio = input("Qual o horário de início da atividade? (formato 2359 ou 23:59)")
    while (int(inicio.split(':')[0]) not in range(24) or int(inicio.split(':')[0]) not in range(60)) or (int(inicio) > 2359 or int(inicio) < 0 or int(inicio) % 100 > 59):
        print("valor inválido")
        inicio = input("Qual o horário de início da atividade? (formato 2359 ou 23:59)")
    
    fim = input("Qual o horário de fim da atividade?")
    while (int(fim).split(':')[0] not in range(24) or int(fim).split(':')[0] not in range(60)) or (int(fim) > 2359 or int(fim) < 0 or int(fim) % 100 > 59):
        print("valor inválido")
        fim = input("Qual o horário de fim da atividade? (formato 2359 ou 23:59)")

    prioridade = int(input("Qual a prioridade da atividade?"))
    while prioridade < 0 or prioridade > 10:
        print("Valor Inválido")
        prioridade = int(input("Qual a prioridade da Atividade?"))
    

    participantes = int(input("Quantas pessoas podem participar da atividade?"))
    while participantes < 0:
        print("valor inválido")
        participantes = int(input("Quantas pessoas podem participar da atividade?"))

    # TODO: criar atividade e adicionar à lista.
    limpar_terminal()
    again = str.capitalize(input("Atividade adicionada! Adicionar mais uma? (s/N)"))
    if again == "S": add_input()
    return    

def add_txt():
    print("Para que o arquivo funcione deve conter nele uma lista de objetos no seguinte formato em JSON:")
    print('{codigo: "str", nome: "str", inicio: int ou "str", fim: int ou "str", prioridade: int, participantes: int}')
    path = input("Qual o caminho absoluto do arquivo a ser lido?")
    with open(path, 'r') as arquivo:
        for linha in arquivo.readlines():
            #TODO: adicionar cada atividade
            print("cheguei aqui")
    return
    

def limpar_terminal():
    # 'nt' indica o sistema operacional Windows
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

adicionar_atividades()