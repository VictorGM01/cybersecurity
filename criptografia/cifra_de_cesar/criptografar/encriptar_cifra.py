def encriptar_cifra_de_cesar(cifra: str, chave: int) -> str:
    alfabeto: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cifra_encriptada: str = ""

    for letra in cifra:
        letra: str = letra.upper()
        index_alfabeto: int = alfabeto.find(letra)  # posição no alfabeto

        # Se a letra não estiver no alfabeto, adiciona na cifra encriptada
        # Ex.: espaços, símbolos, etc
        if letra not in alfabeto:
            cifra_encriptada += letra

        # Verifica se a letra não é a última (Z) e então roda o código
        elif index_alfabeto != 25:
            index_letra_encriptada = index_alfabeto + chave

            # compara a posição da letra encriptada com a posição da letra Z
            if index_letra_encriptada <= 25:
                letra_encriptada = alfabeto[index_letra_encriptada]
                cifra_encriptada += letra_encriptada

            # executado apenas se tiver a letra Z na frase encriptada
            else:
                index_letra_encriptada -= 26
                letra_encriptada = alfabeto[index_letra_encriptada]
                cifra_encriptada += letra_encriptada

        # executado apenas se tiver a letra Z na frase a ser encriptada
        elif index_alfabeto == 25:
            index_letra_encriptada = chave - 1
            letra_encriptada = alfabeto[index_letra_encriptada]
            cifra_encriptada += letra_encriptada

    return cifra_encriptada


# teste
print(encriptar_cifra_de_cesar("Victor  diz: Ola Mundo!", 5))
