import socket

def port_scan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def main():
    host = input("Enter the IP address: ")
    port = int(input("Enter the port number: "))

    if port_scan(host, port):
        print(f"Port {port} is open on {host}!")
    else:
        print(f"Port {port} is closed on {host}!")

if __name__ == '__main__':
    main()
