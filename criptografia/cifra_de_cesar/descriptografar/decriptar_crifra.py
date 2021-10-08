def decriptar_cifra_de_cesar(cifra: str, chave: int) -> None:
    alfabeto: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cifra_decriptada: str = ""

    for letra in cifra:
        index_alfabeto: int = int(alfabeto.find(letra))

        if letra not in alfabeto:
            cifra_decriptada += letra

        elif index_alfabeto != 0:
            index_letra_decriptada = index_alfabeto - chave
            letra_decriptada = alfabeto[index_letra_decriptada]
            cifra_decriptada += letra_decriptada

        elif index_alfabeto == 0 and chave == 1:
            index_letra_decriptada = -1
            letra_decriptada = alfabeto[index_letra_decriptada]
            cifra_decriptada += letra_decriptada

        elif index_alfabeto == 0 and chave != 1:
            index_letra_decriptada = -chave
            letra_decriptada = alfabeto[index_letra_decriptada]
            cifra_decriptada += letra_decriptada

    return cifra_decriptada


print(decriptar_cifra_de_cesar('FSMDYB  NSJ: YVK WEXNY!', 10))
