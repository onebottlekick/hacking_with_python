from portscanner import PortScan

targets_ip = input('[+] * Enter Target To Scan For Vulnerable Open Ports: ')
port_number = int(input('[+] * Enter Amount Of Ports You Want To Scan: ')) + 1
# vul_file = input("[+] * Enter Path Of To The File With Vulverable Softwares: ")
vul_file = 'vulbanners.txt'
print('\n')

target = PortScan(targets_ip, port_number)
target.scan()

with open(vul_file, 'r') as file:
    cnt = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() == banner:
                print(f'[!!] VULNERABLE BANNER: {banner} ON PORT {target.open_ports[cnt]}')
        cnt += 1