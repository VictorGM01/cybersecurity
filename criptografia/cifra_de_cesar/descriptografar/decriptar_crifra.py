def decriptar_cifra_de_cesar(cifra: str, chave: int) -> str:
    alfabeto: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cifra_decriptada: str = ""

    for letra in cifra:
        index_alfabeto: int = int(alfabeto.find(letra))

        # Se a letra não estiver no alfabeto, adiciona na cifra encriptada
        # Ex.: espaços, símbolos, etc
        if letra not in alfabeto:
            cifra_decriptada += letra

        # verifica se a letra não é a primeira (A) e então roda o código
        elif index_alfabeto != 0:
            index_letra_decriptada = index_alfabeto - chave
            letra_decriptada = alfabeto[index_letra_decriptada]
            cifra_decriptada += letra_decriptada

        # executado apenas se tiver a letra A e a chave for 1
        elif index_alfabeto == 0 and chave == 1:
            index_letra_decriptada = -1
            letra_decriptada = alfabeto[index_letra_decriptada]
            cifra_decriptada += letra_decriptada

        elif index_alfabeto == 0 and chave != 1:
            index_letra_decriptada = -chave
            letra_decriptada = alfabeto[index_letra_decriptada]
            cifra_decriptada += letra_decriptada

    return cifra_decriptada


# teste -> compatível com o arquivo 'encripta_cifra'
print(decriptar_cifra_de_cesar('FSMDYB NSJ: YVK WEXNY!', 10))
# output: VICTOR DIZ: OLA MUNDO!
