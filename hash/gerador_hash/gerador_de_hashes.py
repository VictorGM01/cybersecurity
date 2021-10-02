import hashlib


def gera_hash():
    tipo_hash = int(input('''Alguns tipos de Hashs:
    1) MD5
    2) SHA1
    3) SHA256
    4) SHA512
    Digite o tipo de hash desejado: '''))
    texto = input("Digite o texto a ser gerado o hash: ")

    if tipo_hash == 1:
        hash_md5 = hashlib.md5(texto.encode('UTF-8'))
        print(f'O Hash MD5 para o texto: "{texto}" é:' +
              f' {hash_md5.hexdigest()}')

    elif tipo_hash == 2:
        hash_sha1 = hashlib.sha1(texto.encode('UTF-8'))
        print(f'O Hash SHA1 para o texto: "{texto}" é:' +
              f' {hash_sha1.hexdigest()}')

    elif tipo_hash == 3:
        hash_sha256 = hashlib.sha256(texto.encode('UTF-8'))
        print(f'O Hash SHA256 para o texto: "{texto}" é:' +
              f' {hash_sha256.hexdigest()}')

    elif tipo_hash == 4:
        hash_sha512 = hashlib.sha512(texto.encode('UTF-8'))
        print(f'O Hash SHA512 para o texto: "{texto}" é:' +
              f' {hash_sha512.hexdigest()}')

    else:
        print("x" * 73)
        print("Tipo de hash não foi identificado, gostaria de " +
              "tentar novamente?")
        print("x" * 73)
        resposta = str(input("Resposta: "))

        if resposta.lower() == "sim":
            gera_hash()

        else:
            print("Ok!")


gera_hash()
