import socket  # noqa: F401

def make_connection():
    server_port = 4221
    server_ip = '127.0.0.1'
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', server_port))
    server_socket.listen()
    # server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    # server_socket.accept() # wait for client


    # keep accepting the connections.
    while True:
        client, address = server_socket.accept()
        request = print(client.recv(1024).decode())

        print(request)
        # this is an http response
        http_response = (
           ' HTTP/1.1 200 OK\r\n\r\n'
        )

        client.sendall(http_response.encode())


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    
        # client.close()
        # client.send('HTTP/1.1'.encode())
    # run the server.
    make_connection()

if __name__ == "__main__":
    main()
