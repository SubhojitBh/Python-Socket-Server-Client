import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = socket.gethostname()
    server_port = 9999
    
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print(f"Server started on {server_host}:{server_port}, waiting for connections...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established!")
        
        msg = "Welcome to the server!"
        client_socket.send(msg.encode('utf-8'))
        
        client_socket.close()

if __name__ == "__main__":
    start_server()
