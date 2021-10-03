from cryptography.fernet import Fernet


# lê arquivo que contém a chave
with open("chave_simetrica.txt", "rb") as arquivo_chave:
    chave = arquivo_chave.read()

fernet = Fernet(chave)

# abre arquivo criptografado
with open("teste.txt", "rb") as arquivo_criptografado:
    criptografado = arquivo_criptografado.read()

# descriptografa arquivo
arquivo_descriptografado = fernet.decrypt(criptografado)

# salva a descriptografia
with open("teste.txt", "wb") as descriptografado:
    descriptografado.write(arquivo_descriptografado)
