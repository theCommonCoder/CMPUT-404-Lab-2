import socket
from threading import Thread

PROXY_HOST = "127.0.0.1"
PROXY_PORT = 8080
buffer_size = 2048


def send_request(host, port, request):
    with socket.socket() as client_socket:
        client_socket.connect((host, port))
        client_socket.send(request)
        client_socket.shutdown(socket.SHUT_WR)

        all_data = b""
        while True:
            data = client_socket.recv(buffer_size)
            if not data:
                break
            all_data += data
    return all_data


def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")

        request = b""
        while True:
            data = conn.recv(buffer_size)
            if not data:
                break
            request += data
        conn.sendall(send_request("www.google.com", 80, request))


def start_server():
    with socket.socket() as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((PROXY_HOST, PROXY_PORT))
        server_socket.listen(3)

        conn, addr = server_socket.accept()

        handle_connection(conn, addr)


def start_threaded_server():
    with socket.socket() as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((PROXY_HOST, PROXY_PORT))
        server_socket.listen(3)

        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()


def main():
    # start_server()
    start_threaded_server()


if __name__ == "__main__":
    main()