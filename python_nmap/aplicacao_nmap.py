import nmap
# Para este código poder ser executado será necessário a instalação
# do nmap, além de instalar via pip a lib python-nmap, com:
# pip install python-nmap


scan = nmap.PortScanner()

scan.scan('8.8.8.8', ports='1-100')

for host in scan.all_hosts():
    print('----------------------------------------------------')
    # imprime o nome do(s) host(s) que estão sendo escaneados
    print(f'Host: {host} - {scan["host"].hostname()}')

    # imprime o status do host (ativo ou inativo)
    print(f'Estado: {scan["host"].state()}')
    print('----------------------------------------------------')

    for protocolo in scan["host"].all_protocols():
        # imprime o tipo de protocolo que o host está utilizando (ex.: TCP)
        print(f'Protocolo: {protocolo}')

        # armazena as portas que estão sendo escaneadas
        portas = scan[host][protocolo].keys()
        portas.sort()

        for porta in portas:
            print('----------------------------------------------------')
            # imprime a(s) porta(s) e seu(s) status (aberta, fechada, etc)
            print(f'Porta: {porta} - Status: \
            {scan[host][protocolo][porta]["state"]}')
