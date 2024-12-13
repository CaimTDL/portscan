import socket

def identify_open_door():

    try:
        host = str(input("Digite o alvo: "))
        porta = int(input("Digite uma porta: "))

        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scan.settimeout(0.5)
        conect = scan.connect_ex((host, porta))

        if conect == 0:
            print(f"\n\t - open: {porta}")
        else:
            print(f"\n\t - closed: {porta}")
    except socket.gaierror as erro_host:
        print(f"Erro... host inexistente. {erro_host}")

    except ValueError as erro_porta:
        print(f"Porta inexistente... {erro_porta}")

def PortScan_list():
    try:
        host = str(input("Digite o alvo: "))
        porta = [80, 3302, 443]
        for p in porta:


            scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scan.settimeout(0.5)
            conect = scan.connect_ex((host, p))

            if conect == 0:
                print(f"\n\t - open: {p}")
            else:
                print(f"\n\t - closed: {p}")
    except socket.gaierror as erro_host:
                print(f"Erro... host inexistente. {erro_host}")

def port_ranger():
    try:
        host = str(input("Digite o alvo: "))
        porta = range(0,65536)
        for p in porta:


            scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scan.settimeout(0.1)
            conect = scan.connect_ex((host, p))

            if conect == 0:
                print(f"\n\t - open: {p}")
    except socket.gaierror as erro_host:
                print(f"Erro... host inexistente. {erro_host}")

port_ranger()