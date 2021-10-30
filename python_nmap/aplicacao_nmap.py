import nmap


scan = nmap.PortScanner()

scan.scan('8.8.8.8', ports='1-100')

for host in scan.all_hosts():
    print('----------------------------------------------------')
    print(f'Host: {host} - {scan["host"].hostname()}')
    print(f'Estado: {scan["host"].state()}')
    print('----------------------------------------------------')

    for protocolo in scan["host"].all_protocols():
        print(f'Protocolo: {protocolo}')

        portas = scan[host][protocolo].keys()
        portas.sort()

        for porta in portas:
            print('----------------------------------------------------')
            print(f'Porta: {porta} - Status: \
            {scan[host][protocolo][porta]["state"]}')
