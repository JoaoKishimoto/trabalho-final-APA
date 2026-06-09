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

    def get(self, atributo):
        match(atributo):
            case("codigo"):
                return self.codigo
            case("nome"):
                return self.nome
            case("inicio"):
                return self.inicio
            case("fim"):
                return self.fim
            case("prioridade"):
                return self.prioridade
            case("participantes"):
                return self.participantes
            case():
                return

# Verifica se os dados da atividade sao validos antes de salvar
def validar(codigo, nome, inicio, fim, prioridade, participantes):
    if inicio > 2359 or inicio < 0:
        return False, f"Início ({inicio}) não é um horário válido"
    if type(inicio) != 'str': 
        return False, f"Início ({inicio}) não está no formato 1230 (equivalente a 12:30)"
    if fim > 2359 or fim < 0:
        return False, f"Fim ({fim}) não é um horário válido"
    if type(fim) != 'str': 
        return False, f"Fim ({fim}) não está no formato 1230 (equivalente a 12:30)"
    if fim <= inicio:
        return False, f"Fim ({fim}) deve ser maior que inicio ({inicio})."
    if prioridade < 0 or prioridade > 10:
        return False, f"Prioridade deve estar entre 0 e 10."
    if participantes <= 0:
        return False, f"O número de participantes deve ser maior que 0."
    return True, ""


# Permite cadastrar uma atividade digitando os dados no terminal através do menu
def adicionar(codigo, nome, inicio, fim, prioridade, participantes):
    ok, erro = validar(codigo, nome, inicio, fim, prioridade, participantes)
    if not ok:
        print("Erro:", erro)
        return
    return Atividade(codigo, nome, inicio, fim, prioridade, participantes)

# Exibe todas as atividades da lista na tela
def listar(lista):
    if not lista:
        print("Nenhuma atividade cadastrada.")
        return
    for a in lista:
        print(a)
    print(f"Total: {len(lista)}\n")
