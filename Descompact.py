# -*- coding: utf-8 -*-
def descompact(lista):
    binario = []
    quantidade = []
    qualidade = []
    quantidade.append(lista[0])
    lista.remove(lista[0])
    lista_completa = []
    outra_lista = []
    dicionario = {}
    binario_completo = []
    resultado =[]
    
    for i in range(int(lista[0])):
            qualidade.append(lista[i])
    for i in range(quantidade[0]):
        lista.pop(0)
    for i in lista:
        x = bin(i)
        x = str(x)[2:]
        binario.append(x)
    for j in binario:
        while len(j) < 8:
            j = '0' + j
        lista_completa.append(j)
    lista_completa = "".join(lista_completa)
    lista_completa = lista_completa.split("0")
    for i in lista_completa:
        outra_lista.append(i+"0")
    for i in range(len(qualidade)):
        if i == 0:
            binario_completo.append("0")
        else:
            binario_completo.append(i*"1"+"0")
    
    for i in range(len(qualidade)):
        dicionario[binario_completo[i]] = str(qualidade[i])
    outra_lista.pop()
    for i in outra_lista:
        resultado.append(int(dicionario[i]))
    return resultado

lista= [1, 3, 0, 15]
print(descompact(lista))