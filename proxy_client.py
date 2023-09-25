import socket

HOST = "127.0.0.1"
PORT = 8080
buffer_size = 2048
request = f"GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"


def get(host, port):
    with socket.socket() as s:
        s.connect((host, port))
        s.send(request.encode())
        # prevents further writes
        s.shutdown(socket.SHUT_WR)

        all_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            all_data += data
    return all_data


def main():
    print(get("127.0.0.1", 8080))


if __name__ == "__main__":
    main()