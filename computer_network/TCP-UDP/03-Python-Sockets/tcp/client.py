"""Simple TCP client for the local learning server."""

import socket

HOST = "127.0.0.1"
PORT = 50000
BUFFER_SIZE = 1024


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(b"Hello from the TCP client.\n")
        response = client.recv(BUFFER_SIZE)

    if response:
        print(f"Server says: {response.decode('utf-8', errors='replace').rstrip()}")


if __name__ == "__main__":
    main()
