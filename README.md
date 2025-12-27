
# Port Scanner

A configurable TCP port scanner written in Python.  
This tool performs **TCP connect scans** against a target host to identify open and closed ports across a single port or a specified range.

## How It Works

### 1. Argument Parsing & Validation
- Uses `argparse` to handle positional arguments and optional flags
- Validates user input (target, ports, timeout, verbosity)
- Returns a configuration dictionary passed to the scanning function

### 2. Port Scanning
- Extracts scan settings from the configuration dictionary
- For each port:
  - Creates an IPv4 TCP socket (`socket.AF_INET`, `socket.SOCK_STREAM`)
  - Attempts a TCP connection within the specified timeout
  - Reports the port status (open/closed)



## Usage

```bash
scanner.py [-h] [-p PORTS] [-t TIMEOUT] [-v] target

*in terminal 1*
python -m http.server 8080 --bind 0.0.0.0

*in terminal 2
scanner.py 127.0.0.1 -p 8080 -v

*result*
Port 8080: open
```
## Example

Start a local HTTP server on port `8080`:
```bash
# Terminal 1 
python -m http.server 8080 --bind 0.0.0.0
```
Run the scanner against the local host:
```bash
# Terminal 2 
scanner.py 127.0.0.1 -p 8080 -v
```
**Output:**
```bash
Port 8080: open
```


## Future Plans
-   IPv6 support
-   Multithreaded scanning for improved performance
-   Enhanced CLI options and output formatting
-   Optional graphical user interface (GUI)
## LEGAL DISCLAIMER

This tool is intended **solely for educational purposes and authorized security testing**.
You are responsible for ensuring you have **explicit permission** to scan any target system.  
Unauthorized port scanning may be illegal and unethical in many jurisdictions.
The author assumes **no liability** for misuse or damage caused by this software.
