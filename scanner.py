import  socket
import argparse
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print(f'\niniciando scan em {target}')
    print(f'intervalo de tempo: {datetime.now()}')
    start_time = datetime.now()
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setfaulttimeout(0.5) # tempo limite de resposta
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f'Porta {port}: esta Aberta')
            sock.close()
    except KeyboardInterrupt:
        print('\nScan interrompido pelo usuário.')
    except socket.gaierror:
        print('host invalido ou nao encontrado.')
    except socket.error:
        print('erro de coneçao com o servidor.')
    end_time = datetime.now()
    total=end_time - start_time
    print(f'\ntempo toltal de execuçao: {total}') 

    if __name__ == '__main__':
            parser = argparse.ArgumentParser(description='Scanner de Portas em Python')
            parser.add_argument('-t,''--target', required=True, help='Endereço IP ou nome do host escaneado')
            parser.add_argument('-s', '--start-port', required=True, help=' intervalo de portas (ex: 20-80)',)
            args = parser.parse_args()

            try:
                port_range = args.start_port.split('-')
                start_port = int(port_range[0])
                end_port = int(port_range[1])
            except:
             print('formato de porta invalido. use o formato: 20-80')
             exit(1)

            scan_ports(args.target, start_port, end_port)
           
