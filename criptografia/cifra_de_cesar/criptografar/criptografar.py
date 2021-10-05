def encriptar_cifra_de_cesar(cifra, chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cifra_encriptada = ""

    for letra in cifra:
        letra = letra.upper()
        index_alfabeto = alfabeto.find(letra)

        if letra not in alfabeto:
            cifra_encriptada += letra

        elif index_alfabeto != -1 and index_alfabeto != 25:
            index_letra_encriptada = index_alfabeto + chave
            if index_letra_encriptada <= 25:
                letra_encriptada = alfabeto[index_letra_encriptada]
                cifra_encriptada += letra_encriptada
            else:
                index_letra_encriptada -= 26
                letra_encriptada = alfabeto[index_letra_encriptada]
                cifra_encriptada += letra_encriptada

        elif index_alfabeto == 25:
            index_letra_encriptada = chave - 1
            letra_encriptada = alfabeto[index_letra_encriptada]
            cifra_encriptada += letra_encriptada

    print(cifra_encriptada)


# teste
encriptar_cifra_de_cesar("Victor ZWx diz: Ola Mundo!", 5)
