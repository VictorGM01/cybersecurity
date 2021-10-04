import random
import string


print("==========gerador de senha==========")
print("Tipos:\n"
      "1) Letras minúsculas\n"
      "2) Letras maiúsculas\n"
      "3) Caracteres especiais\n"
      "4) Dígitos\n"
      "5) Todos os anteriores (recomendado)\n")


tipo_de_senha: int = int(input("Digite o tipo de senha escolhido: "))
tamanho_da_senha: int = int(input("Digite o tamanho desejado para a senha: "))


def gera_senha_minuscula() -> None:
    caracteres_minusculos: str = string.ascii_lowercase
    print("==============senha=============\n"
          "Copie sua senha: " +
          "".join(random.choice(caracteres_minusculos)
                  for caractere in range(tamanho_da_senha)))


def gera_senha_maiuscula() -> None:
    caracteres_maiusculos: str = string.ascii_uppercase
    print("==============senha=============\n"
          "Copie sua senha: " +
          "".join(random.choice(caracteres_maiusculos)
                  for caractere in range(tamanho_da_senha)))


def gera_senha_numerica() -> None:
    caracteres_numericos: str = string.digits
    print("==============senha=============\n"
          "Copie sua senha: " +
          "".join(random.choice(caracteres_numericos)
                  for caractere in range(tamanho_da_senha)))


def gera_senha_caracteres_especiais() -> None:
    caracteres_especiais: str = "@#!&$#%*/ç.;:?¨()[]{}|,^~+-¨'_=°ªº"
    print("==============senha=============\n"
          "Copie sua senha: " +
          "".join(random.choice(caracteres_especiais)
                  for caractere in range(tamanho_da_senha)))


def gera_senha_forte() -> None:
    caracteres: str = string.ascii_letters + string.digits +\
                 "@#!&$#%*/ç.;:?¨()[]{}|,^~+-¨'_=°ªº"
    print("==============senha=============\n"
          "Copie sua senha: " +
          "".join(random.choice(caracteres)
                  for caractere in range(tamanho_da_senha)))


if tipo_de_senha == 1:
    gera_senha_minuscula()

elif tipo_de_senha == 2:
    gera_senha_maiuscula()

elif tipo_de_senha == 3:
    gera_senha_caracteres_especiais()

elif tipo_de_senha == 4:
    gera_senha_numerica()

elif tipo_de_senha == 5:
    gera_senha_forte()

else:
    print("Tipo de senha inválido, tente novamente...")
