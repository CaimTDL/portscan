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

identify_open_door() 