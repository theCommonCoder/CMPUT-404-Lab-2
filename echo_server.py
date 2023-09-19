import socket
import time

HOST = "127.0.0.1"
PORT = 8080
buffer_size = 2048


def main():
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2)
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)

            # receive data, wait a bit, then send it back
            full_data = conn.recv(buffer_size)
            time.sleep(0.5)
            print(conn.recv(buffer_size))
            conn.sendall(full_data)
            conn.close()


if __name__ == "__main__":
    main()