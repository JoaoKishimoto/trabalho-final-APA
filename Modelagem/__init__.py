# Cria a classe Atividade com todos os atributos necessarios
class Atividade:
    def __init__(self, codigo, nome, inicio, fim, prioridade, participantes):
        self.codigo = codigo
        self.nome = nome
        self.inicio = inicio
        self.fim = fim
        self.prioridade = prioridade
        self.participantes = participantes

    def __str__(self):
        return f"[{self.codigo}] {self.nome} | Inicio: {self.inicio}h Fim: {self.fim}h | Prioridade: {self.prioridade} | Participantes: {self.participantes}"


# Verifica se os dados da atividade sao validos antes de salvar
def validar(codigo, nome, inicio, fim, prioridade, participantes):
    if not codigo or not nome:
        return False, "Codigo e nome nao podem ser vazios."
    if fim <= inicio:
        return False, f"Fim ({fim}) deve ser maior que inicio ({inicio})."
    if prioridade < 0:
        return False, f"Prioridade nao pode ser negativa."
    if participantes <= 0:
        return False, f"Participantes deve ser maior que 0."
    return True, ""


# Permite cadastrar uma atividade digitando os dados no terminal
def adicionar(lista):
    print("\nCadastrar nova atividade:")
    codigo = input("Codigo: ")
    nome = input("Nome: ")
    inicio = int(input("Inicio (hora): "))
    fim = int(input("Fim (hora): "))
    prioridade = int(input("Prioridade: "))
    participantes = int(input("Participantes: "))

    ok, erro = validar(codigo, nome, inicio, fim, prioridade, participantes)
    if not ok:
        print("Erro:", erro)
        return

    lista.append(Atividade(codigo, nome, inicio, fim, prioridade, participantes))
    print("Atividade cadastrada!")


# Carrega uma lista de atividades prontas para usar nos testes
def carregar_dados_teste():
    dados = [
        ("A001", "Reuniao de planejamento", 8, 10, 1, 5),
        ("A002", "Desenvolvimento", 9, 17, 2, 3),
        ("A003", "Revisao de codigo", 14, 16, 1, 4),
        ("A004", "Deploy", 16, 18, 3, 2),
        ("A005", "Testes", 10, 12, 2, 3),
        ("A006", "Documentacao", 13, 15, 0, 1),
    ]

    lista = []
    for d in dados:
        ok, erro = validar(*d)
        if ok:
            lista.append(Atividade(*d))
        else:
            print(f"Atividade '{d[1]}' ignorada: {erro}")

    print(f"{len(lista)} atividades carregadas.")
    return lista


# Exibe todas as atividades da lista na tela
def listar(lista):
    if not lista:
        print("Nenhuma atividade cadastrada.")
        return
    for a in lista:
        print(a)
    print(f"Total: {len(lista)}")


# Menu principal que chama as funcoes acima
def menu():
    atividades = []

    while True:
        print("\n1 - Cadastrar atividade")
        print("2 - Carregar dados de teste")
        print("3 - Listar atividades")
        print("0 - Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            adicionar(atividades)
        elif opcao == "2":
            atividades += carregar_dados_teste()
        elif opcao == "3":
            listar(atividades)
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    menu()