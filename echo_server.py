import socket
import time
from threading import Thread

HOST = "127.0.0.1"
PORT = 8080
buffer_size = 2048


def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")

        all_data = b""
        while True:
            data = conn.recv(buffer_size)
            if not data:
                break
            all_data += data
        print(all_data.decode("utf8", "ignore"))
        conn.sendall(all_data)


def start_threaded_server():
    with socket.socket() as server_socket:
        # level: socket optname: reuse_addr value: true
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # claim the socket
        server_socket.bind((HOST, PORT))
        # listen to incoming requests
        server_socket.listen(3)

        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()


def main():
    start_threaded_server()


if __name__ == "__main__":
    main()