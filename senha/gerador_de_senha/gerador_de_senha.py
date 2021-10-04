import random
import string


def gera_senha_minuscula():
    caracteres_minusculos = string.ascii_lowercase
    print("==============senha=============\n"
          "Copie sua senha: " +
          "".join(random.choice(caracteres_minusculos)
                  for caractere in range(tamanho_da_senha)))


def gera_senha_maiuscula():
    caracteres_maiusculos = string.ascii_uppercase
    print("==============senha=============\n"
          "Copie sua senha: " +
          "".join(random.choice(caracteres_maiusculos)
                  for caractere in range(tamanho_da_senha)))


def gera_senha_numerica():
    caracteres_numericos = string.digits
    print("==============senha=============\n"
          "Copie sua senha: " +
          "".join(random.choice(caracteres_numericos)
                  for caractere in range(tamanho_da_senha)))


def gera_senha_caracteres_especiais():
    caracteres_especiais = "@#!&$#%*/ç.;:?¨()[]{}|,^~+-¨'_=°ªº"
    print("==============senha=============\n"
          "Copie sua senha: " +
          "".join(random.choice(caracteres_especiais)
                  for caractere in range(tamanho_da_senha)))


print("==========gerador de senha==========")
print("Tipos:\n"
      "1) Letras minúsculas\n"
      "2) Letras maiúsculas\n"
      "3) Caracteres especiais\n"
      "4) Dígitos\n"
      "5) Todos os anteriores (recomendado)\n")

tipo_de_senha = int(input("Digite o tipo de senha escolhido: "))
tamanho_da_senha = int(input("Digite o tamanho desejado para a senha: "))

if tipo_de_senha == 1:
    gera_senha_minuscula()

elif tipo_de_senha == 2:
    gera_senha_maiuscula()

elif tipo_de_senha == 3:
    gera_senha_caracteres_especiais()

elif tipo_de_senha == 4:
    gera_senha_numerica()
