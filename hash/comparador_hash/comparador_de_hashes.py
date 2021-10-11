import hashlib


def compara_hash_arquivos():
    arquivo_original = input("Digite o nome/caminho do arquivo original: ")
    arquivo_comparavel = input(
        "Digite o nome/caminho do arquivo a ser comparado: "
    )

    hash_arquivo_original = hashlib.new('ripemd160')
    hash_arquivo_original.update(open(arquivo_original, 'rb').read())

    hash_arquivo_comparavel = hashlib.new('ripemd160')
    hash_arquivo_comparavel.update(open(arquivo_comparavel, 'rb').read())

    if hash_arquivo_original.digest() == hash_arquivo_comparavel.digest():
        print("***************Hash compatível***************")

        print('Hash arquivo original: {}'.format(
            hash_arquivo_original.hexdigest())
        )
        print('Hash arquivo comparado: {}'.format(
            hash_arquivo_comparavel.hexdigest())
        )

    else:
        print("Hash incompatível, conteúdo dos arquivos é diferente")


compara_hash_arquivos()
