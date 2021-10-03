import random
import string


def gera_senha_minuscula():
    caracteres = string.ascii_lowercase
    print("==============senha=============\n"
          "Copie sua senha: " +
          "".join(random.choice(caracteres)
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
