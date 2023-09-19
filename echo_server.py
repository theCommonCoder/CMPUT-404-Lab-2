import socket
import time

HOST = "127.0.0.1"
PORT = 8080
buffer_size = 2048


def main():
    with socket.socket() as s:
        s.bind((HOST, PORT))
        s.listen(2)
        conn, addr = s.accept()
        print("Connected by", addr)
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)

            # receive data, wait a bit, then send it back
            full_data = conn.recv(buffer_size)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()


if __name__ == "__main__":
    main()