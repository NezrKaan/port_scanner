# Port Scanner

This is a simple port scanning tool implemented in Python using the `socket` module. It allows you to check if a specific port is open or closed on a given IP address.

## Usage

1. Clone the repository or download the `port_scanner.py` file.

2. Make sure you have Python installed on your system.

3. Open a terminal or command prompt and navigate to the directory where the `port_scanner.py` file is located.

4. Run the script by entering the following command:
   ```
   python port_scanner.py
   ```

5. The program will prompt you to enter the IP address and port number you want to scan.

6. Enter the IP address in the format `xxx.xxx.xxx.xxx`, where each `x` represents a number between 0 and 255.

7. Enter the port number you want to scan.

8. The program will attempt to establish a TCP connection to the specified IP address and port.

9. If the port is open, it will display the message: "Port [port number] is open on [IP address]!"

10. If the port is closed, it will display the message: "Port [port number] is closed on [IP address]!"

## Notes

- The program uses the `socket` module in Python to establish TCP connections. Therefore, it can only scan TCP ports.

- By default, the program has a timeout of 2 seconds for each connection attempt. You can modify the timeout value by changing the `sock.settimeout(2)` line in the `port_scan` function.

- Make sure you have the necessary permissions to scan ports on the specified IP address. Some networks or hosts may have security measures in place that block or restrict port scanning activities.

- This program is intended for educational and informational purposes only. Please use it responsibly and ensure that you have proper authorization before scanning any systems or networks.

Please let me know if you need any further assistance!
