from util import clear_cmd
import Busca
import Modelagem

def pg_busca(lista):

    while True:
        print("1 - Buscar por código")
        print("2 - Buscar por nome")
        print("0 - Voltar")
        resultado = input("Qual busca você deseja realizar?\n")
        clear_cmd()

        match(resultado):
            case('0'):
                return
            case('1'):
                codigo = input("\nDigite o codigo para buscar (ex: A001): ").strip()

                resposta = Busca.busca_por_codigo(lista, codigo)
                if resultado:
                    Busca.exibir_tabela([resposta])
                else:
                    print("Atividade nao encontrada.")
                return
            case('2'):
                termo = input("\nDigite o nome (ou parte do nome) para buscar: ").strip()
                resposta = Busca.busca_por_nome(lista, termo)
                Busca.exibir_tabela(resposta)
                return
            case():
                continue
        
        clear_cmd()
        print("valor inválido")
