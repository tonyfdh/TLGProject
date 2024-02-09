import socket
import subprocess

def ping_host(host):
    try:
        subprocess.run(["ping", host], check=True)
        print(f"Ping to {host}: OK")
    except subprocess.CalledProcessError:
        print(f"Ping to {host}: FAILED")

def dns_lookup(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"DNS lookup for {hostname}: {ip_address}")
    except socket.gaierror:
        print(f"DNS lookup for {hostname}: FAILED")

def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)  # Set timeout for connection attempt
            s.connect((host, port))
            print(f"Port {port} on {host}: OPEN")
    except (socket.timeout, ConnectionRefusedError):
        print(f"Port {port} on {host}: CLOSED")
