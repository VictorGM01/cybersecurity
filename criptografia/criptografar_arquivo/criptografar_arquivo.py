from cryptography.fernet import Fernet

# chave simétrica
chave = Fernet.generate_key()

# guarda chave em um arquivo
with open("chave_simetrica.txt", "wb") as arquivo_chave:
    arquivo_chave.write(chave)
