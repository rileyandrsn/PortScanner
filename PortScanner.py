import socket
import sys

def portScan(ip, ports):
    try:
        print(f"Scanning ports {ports[0]} to {ports[-1]}") # Display ports being scanned
        for port in ports:
            try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create an IPV4 socket using TCP protocol
                    s.settimeout(5) # Set a two-second timeout for socket connection attempt
                    result = s.connect_ex((ip, port)) # Returns 0 if port is open; other value indicates port closed/error
                    if result == 0:
                        print(f"Port {port} open") # Port open
                    else:
                        print(f"Port {port} closed") # Port closed
                    s.close() # Close socket after connection attempt
            except (socket.timeout, ConnectionRefusedError):
                print(f"Port {port} closed")
    except KeyboardInterrupt: # Indicates user closed program
        print("Keyboard Interrupt, exiting program.")
        sys.exit()
    except socket.herror as e: # Host-related socket errors
        print("Host-associated error - " + str(e))
        sys.exit()
    except socket.gaierror as e: # Invalid host/IP errors
        print("Hostname/port could not be resolved - " + str(e))
        sys.exit()

def main():
    ip = "scanme.nmap.org" # Default nmap ip to scan
    ports = list(range(1, 500))
    portScan(ip, ports)

if __name__ == "__main__":
    main()
