import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = socket.gethostname()
    server_port = 9999
    
    client_socket.connect((server_host, server_port))
    
    msg = client_socket.recv(1024)
    print(msg.decode('utf-8'))
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
