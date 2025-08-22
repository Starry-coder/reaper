from modules.portscan import scan_ports

target = input("Enter target IP/domain: ")
open_ports = scan_ports(target)
print(f"Open ports: {open_ports}")
