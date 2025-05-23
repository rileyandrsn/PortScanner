**Python Port Scanner**
Python script scanning TCP ports on an IP address. By default, it scans scanme.nmap.org across ports 1–499 and reports whether each port is open or closed.

**How It Works**
Establishes a TCP connection using Python's Socket module. If the connection is successful (connect_ex() returns 0), the port is printed as opened, otherwise if connection fails (error, closed port, timeout) port is marked as closed.

**Requirements**
Python 3.x
Python Libraries:
-socket
-sys

**Installation**
Clone the repository:
git clone https://github.com/rileyandrsn/PortScanner.git
cd PortScanner
Run the script:
python3 portScanner.py


**Example Output**
python3 portScanner.py 
Scanning ports 1 to 499
Port 1 closed
Port 2 closed
Port 3 closed
...
Port 499 closed

**Future Updates**
- Multithreaded scanning for faster scanning.
- GUI interface for users to specifiy a target IP address and range of ports.

**Disclaimer**
This tool is to be used for educational purposes and to be used with authorized use. Do not scan networks or systems you do not own without persmission, doing so can be illegal.
