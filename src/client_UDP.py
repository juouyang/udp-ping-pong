import socket
import sys

def ping_pong(addr):
    # Create socket for client-server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)

    # Send ping
    send_data = "ping"
    s.sendto(send_data.encode('utf-8'), addr)
    print("Client sent: ", send_data)

    try:
        # Receive pong
        data, address = s.recvfrom(4096)
        print("Client received: ", data.decode('utf-8'))

    except socket.timeout:
        print("Timeout!!!")

    # Close the socket
    s.close()

def main():
    # Check if it was well compiled and has 2 args
    if len(sys.argv) == 3:
        ip = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Run like: python3 client_UDP.py serverIP serverPORT")
        exit(1)

    server_address = (ip, port)
    ping_pong(server_address)

#-----------------------------------------------------
if __name__ == '__main__':
    main()