from cryptography.fernet import Fernet


chave = Fernet.generate_key()

# guarda chave em um arquivo
with open("chave_simetrica.txt", "wb") as arquivo_chave:
    arquivo_chave.write(chave)

# abre o arquivo da chave
with open("chave_simetrica.txt", "rb") as arquivo_chave:
    chave_simetrica = arquivo_chave.read()

fernet = Fernet(chave_simetrica)

# abre arquivo teste
with open("teste.txt", "rb") as arquivo:
    arquivo_original = arquivo.read()

# criptografa arquivo
arquivo_criptografado = fernet.encrypt(arquivo_original)

# salva criptografia
with open("teste.txt", "wb") as criptografado:
    criptografado.write(arquivo_criptografado)
