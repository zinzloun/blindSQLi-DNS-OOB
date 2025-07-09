# ---------- dns-server/dns_listener.py ----------
# to visualize dns server logs: open a new shell then execute:
## sudo docker exec -it blind-sqli-lab_dns-server_1 /bin/bash
## cat dns_log.txt
import socket
import logging

# Config logging
logging.basicConfig(
    filename='/app/dns_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Create socket DNS (UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 53))

print("[*] DNS server listening on port 53...")

while True:
    data, addr = sock.recvfrom(1024)
    domain = data.hex() # decode
    print(f"[+] DNS query from {addr}: RAW = {domain}")
    logging.info(f"DNS query from {addr}: RAW = {domain}")
