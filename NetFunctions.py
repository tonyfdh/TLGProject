import socket
import subprocess
import speedtest
import scapy.all as scapy

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

def traceroute(destination):
    try:
        print(f"Traceroute to {destination}:")
        subprocess.run(["tracert", destination], check=True)
    except subprocess.CalledProcessError:
        print(f"Traceroute to {destination}: FAILED")

def bandwidth_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")

def arp_table_view():
    arp_result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
    print("ARP Table:")
    print(arp_result.stdout)

def speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1024 / 1024  # Convert to Mbps
        upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
        print(f"Download speed: {download_speed:.2f} Mbps")
        print(f"Upload speed: {upload_speed:.2f} Mbps")
    except speedtest.SpeedtestException as e:
        print(f"Speed test failed: {e}")

if __name__ == "__main__":
    ping_host("example.com")
    dns_lookup("example.com")
    check_port("example.com", 80)
    traceroute("example.com")
    bandwidth_test()
    arp_table_view()
    speed_test()