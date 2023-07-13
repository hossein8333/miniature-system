import socket
from typing import List, Dict

class PortScanner:
    def scan_ports(self, ip_address: str, start_port: int, end_port: int) -> List[int]:
        open_ports = []
        for port in range(start_port, end_port + 1):
            if self.is_port_open(ip_address, port):
                open_ports.append(port)
        return open_ports

    def is_port_open(self, ip_address: str, port: int) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                return True
            else:
                return False
        except socket.error:
            return False

    def scan_ip_addresses(self, ip_addresses: List[str], start_port: int, end_port: int) -> Dict[str, List[int]]:
        results = {}
        for ip_address in ip_addresses:
            open_ports = self.scan_ports(ip_address, start_port, end_port)
            results[ip_address] = open_ports
        return results
