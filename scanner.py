import threading
import sys
import socket
import re
import argparse
import ipaddress

HOSTNAME_REGEX = re.compile(
    r"^(?=.{1,253}$)"
    r"(?:[a-zA-Z0-9]"
    r"(?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+"
    r"[a-zA-Z]{2,63}$"
)

PORTS_REGEX = re.compile(r"^\d{1,5}(-\d{1,5})?$")

def validate_ports(ports):
    if PORTS_REGEX.fullmatch(ports):
        return True
    else:
        return False

def is_hostname(value: str) -> bool:
    return bool(HOSTNAME_REGEX.fullmatch(value))

def is_valid_ip(addr):
    try:
        ipaddress.ip_address(addr)
        return True
    except:
        pass
    return is_hostname(addr)

def parse_input():
    parser = argparse.ArgumentParser(
        description="Simple TCP port scanner"
    )

    parser.add_argument(
        "target",
        help="Target IP or hostname"
    )
    
    parser.add_argument(
        "-p", "--ports",
        default="1-1024",
        help="Port range (e.g. 80, 443, 8000-9000)"
    )

    parser.add_argument(
        "-t", "--timeout",
        type=float,
        default=1.0,
        help="Socket timeout in seconds"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )

    args = parser.parse_args()

    if not is_valid_ip(args.target):
        print("Error: Invalid target address")
        sys.exit(1)

    ports = args.ports
    if not validate_ports(ports):
        print("Error: Invalid port argument")
        sys.exit(1)

    try:
        start_port, end_port = ports.split("-")
    except:
        start_port = end_port = ports

    start_port = int(start_port)
    end_port = int(end_port)

    num_threads = 1
    if not start_port == end_port:
        num_threads = min(end_port-start_port, 100)


    if not 1<=start_port <= end_port <= 65535:
        print("Error: Invalid port or port range")
        sys.exit(1)
    
    if(args.timeout < 0):
        print("Error: invalid timeout limit")
        sys.exit(1)

    return {
        "target":args.target,
        "start_port":start_port,
        "end_port":end_port, 
        "timeout":args.timeout,
        "verbose":args.verbose,
        "num_threads":num_threads
    }
    
def scan(config):
    target = str(config["target"])
    port_map = {}
    for port in range(config["start_port"],config["end_port"]+1,1):
        status = -1
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(config["timeout"])
            status = sock.connect_ex((target,port))
        finally:
            sock.close()
            if(status == 0):
                result = "open"
            else:
                result = "closed"
            if config["verbose"]:
                print(f"Port {port}: {result}")
            port_map[port] = result

def main():
    config = parse_input()
    print(config)
    scan(config)
        
if __name__ == "__main__":
    main()