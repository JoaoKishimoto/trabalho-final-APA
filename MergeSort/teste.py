import __init__

# função para criar dicionários com 2 valores, um `igual` com valor 11
# e um `numero` com valor igual à entrada da função.
def criaObjeto(n):
    objeto = {}
    objeto["numero"] = n
    objeto["igual"] = 11
    return objeto

# resultado esperado é o mesmo array de entrada (números mantém a ordem de entrada).
resultado1 = __init__.mergeSort([criaObjeto(0),criaObjeto(3),criaObjeto(5), criaObjeto(1),criaObjeto(2),criaObjeto(4)], 'igual')
if resultado1 == [{'numero': 0, 'igual': 11}, {'numero': 3, 'igual': 11}, {'numero': 5, 'igual': 11}, {'numero': 1, 'igual': 11}, {'numero': 2, 'igual': 11}, {'numero': 4, 'igual': 11}]:
    print("Estabilidade Funcionando: \n", resultado1)
else:
    print("Estabilidade não está funcionando: \n", resultado1)

# resultado esperado é o array de entrada organizado pelo parâmetro `numero`.
resultado2 = __init__.mergeSort([criaObjeto(0),criaObjeto(3),criaObjeto(5), criaObjeto(1),criaObjeto(2),criaObjeto(4)], 'numero')
if resultado2 == [{'numero': 0, 'igual': 11}, {'numero': 1, 'igual': 11}, {'numero': 2, 'igual': 11}, {'numero': 3, 'igual': 11}, {'numero': 4, 'igual': 11}, {'numero': 5, 'igual': 11}]:
    print("Ordenação funcionando: \n", resultado2)
else: 
    print("Ordenação não funcional: \n", resultado2)