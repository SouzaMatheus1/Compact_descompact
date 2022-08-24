# -*- coding: utf-8 -*-
def compactar(x):
    repetidos = []
    conversao = {}
    conversao_ordenado = {}
    binario = []
    conversao_completa = {}
    chaves = []
    final = []
    count = 1
    counts = 0
    convertido = []

    # Faz uma lista com os números recebidos e uma lista de números sem repetir
    for i in x:
        if not i in repetidos:
            repetidos.append(i)
    convertido.append(len(repetidos))
    # Cria um dicionario com o número e quantas vezes ele se repete
    for i in repetidos:
        conversao[i] = x.count(i)

    # Cria uma lista com os números que seram usados
    for i in range(len(conversao)):
        if i == 0:
            binario.append("0")
        else:
            num = (i*"1")+"0"
            binario.append(num)

    # Cria um dicionario ordenado e uma lista so com as chaves
    for i in sorted(conversao, key = conversao.get, reverse=True):
        conversao_ordenado[i] = conversao[i]
        chaves.append(i)
    for i in conversao_ordenado:
        convertido.append(i)
    # Cria dicionario ordenado com o valor em binario
    for i in range(len(conversao_ordenado)):
        conversao_completa[chaves[i]] = binario[i]
        
    for i in x:
        final.append(conversao_completa[i])
    quase = "".join(final)
    final = []

    for i in quase:
        final.append(i)
        if count == 8:
            count = 0
            final.append(",")
        count += 1
    final = "".join(final)
    final = final.split(",")
    while len(final[len(final)-1]) < 8:
        final.insert(len(final)-1, final[len(final)-1]+"1")
        final.pop()
        
    numero = 0

    for j in final:
        numero = 0
        for i in j:
            if counts == 0 and i == "1":
                numero += 128
            elif counts == 1 and i == "1":
                numero += 64
            elif counts == 2 and i == "1":
                numero += 32
            elif counts == 3 and i == "1":
                numero += 16
            elif counts == 4 and i == "1":
                numero += 8
            elif counts == 5 and i == "1":
                numero += 4
            elif counts == 6 and i == "1":
                numero += 2
            elif counts == 7 and i == "1":
                numero += 1
            counts += 1
        counts = 0
        convertido.append(numero)
    return convertido
lista = [2,2,2,2,2,2,2,2,2,2,2,2]
print(compactar(lista))