from modules.portscan import scan_ports
from modules.http_check import check_http_vulnerabilities


target = input("Enter target IP/domain: ")
open_ports = scan_ports(target)
print(f"Open ports: {open_ports}")


vuln_results = check_http_vulnerabilities(target)
print("HTTP check results:", vuln_results)