"""Simple one-client TCP server for local learning."""

import socket

HOST = "127.0.0.1"
PORT = 50000
BUFFER_SIZE = 1024


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"TCP server listening on {HOST}:{PORT}")

        conn, address = server.accept()
        with conn:
            print(f"Connected by {address}")
            data = conn.recv(BUFFER_SIZE)
            if not data:
                print("Client closed without sending data.")
                return

            message = data.decode("utf-8", errors="replace").rstrip("\n")
            print(f"Client says: {message}")
            conn.sendall(b"Server received your message.\n")


if __name__ == "__main__":
    main()
