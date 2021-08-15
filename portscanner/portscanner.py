import socket
from IPy import IP

def scan(target, port_num=500):
    converted_ip = check_ip(target)
    print()
    print(f'[-_o Scanning Target] {target}')
    for port in range(1, port_num+1):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(sock):
    return sock.recv(1024).decode().strip("\n")

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print(f'[+] Open Port {port} : {banner}')
        except:
            print(f'[+] Open Port {port}')
    except:
        pass

if __name__ == '__main__':
    targets = input('[+] Enter Target To Scan: ')
    
    default_port = 500
    port_num = input(f'Enter Number Of Ports Want To Scan(default={default_port}): ')

    if port_num:
        port_num = int(port_num)
    else:
        port_num = 500
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '), port_num)

    else:
        scan(targets, port_num)