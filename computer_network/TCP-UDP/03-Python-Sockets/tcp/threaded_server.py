"""Threaded TCP server illustrating concurrent client handling and a lock."""

import socket
import threading

HOST = "127.0.0.1"
PORT = 50000
BUFFER_SIZE = 1024

active_clients = 0
client_count_lock = threading.Lock()


def handle_client(conn, address):
    global active_clients
    registered = False

    try:
        with client_count_lock:
            active_clients += 1
            current_count = active_clients
            registered = True

        print(f"Client {address} connected; active clients: {current_count}")

        with conn:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                return

            message = data.decode("utf-8", errors="replace").rstrip("\n")
            print(f"{address} says: {message}")
            conn.sendall(b"Threaded server received your message.\n")
    except OSError as exc:
        print(f"Socket error with {address}: {exc}")
    finally:
        if registered:
            with client_count_lock:
                active_clients -= 1


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Threaded TCP server listening on {HOST}:{PORT}")

        try:
            while True:
                conn, address = server.accept()
                thread = threading.Thread(
                    target=handle_client,
                    args=(conn, address),
                    daemon=True,
                )
                thread.start()
        except KeyboardInterrupt:
            print("\nStopping server.")


if __name__ == "__main__":
    main()
