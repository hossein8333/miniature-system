from typing import List
from port_scanner import PortScanner

class PortScannerCLI:
    def __init__(self):
        self.port_scanner = PortScanner()

    def run(self):
        print("Welcome to the Port Scanner!")
        while True:
            print("\nMenu:")
            print("1. Scan ports on a single IP address")
            print("2. Scan ports on multiple IP addresses")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")
            if choice == "1":
                self.scan_single_ip()
            elif choice == "2":
                self.scan_multiple_ips()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def scan_single_ip(self):
        ip_address = input("Enter the IP address to scan: ")
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        open_ports = self.port_scanner.scan_ports(ip_address, start_port, end_port)
        print(f"Open ports on {ip_address}: {open_ports}")

    def scan_multiple_ips(self):
        ip_addresses = input("Enter the IP addresses to scan (comma-separated): ").split(",")
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        results = self.port_scanner.scan_ip_addresses(ip_addresses, start_port, end_port)
        for ip_address, open_ports in results.items():
            print(f"Open ports on {ip_address}: {open_ports}")
