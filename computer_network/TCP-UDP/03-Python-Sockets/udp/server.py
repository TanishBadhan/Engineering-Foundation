"""Simple UDP reply server for local learning."""

import socket

HOST = "127.0.0.1"
PORT = 50001
BUFFER_SIZE = 2048


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
        server.bind((HOST, PORT))
        print(f"UDP server listening on {HOST}:{PORT}")

        try:
            while True:
                data, address = server.recvfrom(BUFFER_SIZE)
                message = data.decode("utf-8", errors="replace")
                print(f"Received from {address}: {message}")
                server.sendto(b"UDP server received your datagram.", address)
        except KeyboardInterrupt:
            print("\nStopping server.")


if __name__ == "__main__":
    main()
