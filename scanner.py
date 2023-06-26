import socket

targets = input("[*] Enter ip address of target(s) separated by commas: ")
ports = int(input("[*] Enter total number of ports you want ot scan: "))

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] {str(port)} - open")
        sock.close()
    except:
        pass

def scan(target, ports):
    print(f"scan results for {target}")
    for port in range(1,ports):
        scan_port(target, port)

if "," in targets:
    print("[*] Scanning multiple targets.......")
    for target in targets.split(","):
        scan(target.strip(' '), ports)
else:
    scan(targets, ports)