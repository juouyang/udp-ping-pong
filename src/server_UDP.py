import socket
import sys

def ping_pong(addr, silent=False):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(addr)

    while True:
        if not silent:
            print("------- Server is listening -------")
        data, address = s.recvfrom(4096)
        received_message = data.decode('utf-8')
        if not silent:
            print(f"Server received: {received_message} from {address}")

        if received_message == "ping":
            send_data = "pong"
            s.sendto(send_data.encode('utf-8'), address)
            if not silent:
                print(f"Server sent: {send_data} to {address}")
        elif not silent:
            print(f"Server ignored: {received_message} from {address}")

def main():
    # Default log visibility
    silent = False

    # Check arguments
    if len(sys.argv) >= 3:
        ip = sys.argv[1]
        port = int(sys.argv[2])
        if len(sys.argv) == 4 and sys.argv[3] == "--silent":
            silent = True
    else:
        print("Run like: python3 server_UDP.py serverIP serverPORT [--silent]")
        exit(1)

    server_address = (ip, port)
    ping_pong(server_address, silent)

if __name__ == '__main__':
    main()