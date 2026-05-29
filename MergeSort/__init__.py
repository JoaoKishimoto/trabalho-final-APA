import math

# Algoritmo de merge-sort sobre o array olhando a chave `element` de cada item
# que deve ser passado em formato de string.
def mergeSort(array, element):
    if len(array) == 1:
        return array
    else:
        size = len(array)
        size = math.floor(size/2)
        array = funnel(mergeSort(array[:size], element), mergeSort(array[size:], element), element)
    return array

# Algoritmo de funil que une dois arrays olhando para a chave `element` de cada item.
def funnel(array1, array2, element):
    array1.reverse()
    array2.reverse()
    
    array = []
    while len(array1) >= 1 and  len(array2) >= 1:
        if array1[-1].get(element) <= array2[-1].get(element):
            array.append(array1.pop())
        else:
            array.append(array2.pop())
    if len(array1) == 0:
        while len(array2) != 0:
            array.append(array2.pop())
    else:
        while len(array1) != 0:
            array.append(array1.pop())
    return array