import socket

host = "127.0.0.1"
port = 8080
request = f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"


def main():
    with socket.create_connection((host, port)) as s:
        s.send(request.encode())
        s.shutdown(socket.SHUT_WR)

        buffer_size = 2048
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            full_data += data
        print(full_data.decode("utf8", "replace"))


if __name__ == "__main__":
    main()