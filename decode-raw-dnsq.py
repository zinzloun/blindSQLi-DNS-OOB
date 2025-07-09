import sys

def decode_dns_query(hexstring):
    # Skip DNS header (12 bytes = 24 hex chars)
    query_hex = hexstring[24:]
    i = 0
    labels = []
    while i < len(query_hex):
        length = int(query_hex[i:i+2], 16)
        if length == 0:
            break
        i += 2
        label = bytes.fromhex(query_hex[i:i+length*2]).decode('ascii')
        labels.append(label)
        i += length * 2
    return '.'.join(labels)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python decode-raw-dnsq.py <hex_raw>")
        sys.exit(1)
    
    raw = sys.argv[1].strip().lower()
    
    try:
        domain = decode_dns_query(raw)
        print(f"[+] Plain domain value: {domain}")
    except Exception as e:
        print(f"[!] Decoding error: {e}")
