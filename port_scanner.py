import socket
import concurrent.futures

def port_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.gaierror:
        return False
    except socket.error:
        return False

def perform_scan(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if port_scan(host, port):
            open_ports.append(port)
    return open_ports

def main():
    host = input("Enter the IP address: ")
    start_port = int(input("Enter the start port number: "))
    end_port = int(input("Enter the end port number: "))

    print(f"Scanning ports on {host}...\n")

    open_ports = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for port in range(start_port, end_port + 1):
            futures.append(executor.submit(port_scan, host, port))

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(future.result())

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"Port {port} is open on {host}!")
    else:
        print(f"No open ports found on {host}.")

if __name__ == '__main__':
    main()
