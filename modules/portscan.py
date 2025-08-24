import socket

def scan_ports(target):
    print(f"Scanning ports on {target}...")
    common_ports = [21, 22, 23, 80, 443, 3306, 8080]
    open_ports = []

    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((target, port))
            open_ports.append(port)
        except:
            pass
        s.close()
    return open_ports
