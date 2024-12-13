import socket


def port_ranger():
    try:
        host = str(input("Digite o alvo: "))
        porta = range(0,6536)
        file = open('Export.txt', 'w', encoding='utf8')
        file.write(f'Host: {host}\n\n')
        file.write(f'\tPort\tState\tService\n')
        print('Scanning...\n')
        for p in porta:


            scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scan.settimeout(0.1)
            conect = scan.connect_ex((host, p))

            if conect == 0:
                try:
                    file.write(f"\t\{p}\t\Open\t\{socket.getservbyport(p)}\n")
                except:
                    continue
    
    except socket.gaierror as erro_host:
                print(f"Erro... host inexistente. {erro_host}")
    except KeyboardInterrupt as cancel_conect:
                print(f"Cancelado com sucesso. {cancel_conect}")
    except TypeError as erro_porta:
                print(f"Edite o código. {erro_porta}")

port_ranger()
print('Scan finalizado com sucesso!\n informações no arquivo export.txt')