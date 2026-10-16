"""Simple UDP client for the local learning server."""

import socket

HOST = "127.0.0.1"
PORT = 50001
BUFFER_SIZE = 2048


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.settimeout(3.0)
        client.sendto(b"Hello from the UDP client.", (HOST, PORT))

        try:
            data, server_address = client.recvfrom(BUFFER_SIZE)
        except socket.timeout:
            print("No reply received before the timeout.")
            return

    print(
        f"Reply from {server_address}: "
        f"{data.decode('utf-8', errors='replace')}"
    )


if __name__ == "__main__":
    main()
