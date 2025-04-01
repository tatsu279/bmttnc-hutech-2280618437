import socket, ssl, threading

# Thong tin server
server_address = ('localhost', 12345)

#danh cho cac client
clients = []

def handle_client(client_socket):
    #them thong tin client vao danh sach
    clients.append(client_socket)
    
    print(f"Client {client_socket.getpeername()} connected.")
    
    try:
        while True:
            # Nhan du lieu tu client
            data = client_socket.recv(1024)
            if not data:
                break
            
            print(f"Received from {client_socket.getpeername()}: {data.decode()}")
            
            # Gui du lieu den tat ca cac client khac
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        print(f"Client {client.getpeername()} disconnected.")
                        clients.remove(client)
    except:
        clients.remove(client_socket)
        
    finally:
        # Dong ket noi
        client_socket.close()
        print(f"Client {client_socket.getpeername()} disconnected.")
        clients.remove(client_socket)
        
#tao socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

print(f"Server listening on {server_address}")

while True:
    # Chap nhan ket noi tu client
    client_socket, client_address = server_socket.accept()
    
    #tao ssl
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain(certfile="./certificates/server-cert.crt",
    keyfile = "./certificates/server-key.key")
    
    #thiet lap ket noi ssl
    ssl_socket = context.wrap_socket(client_socket, server_side=True)
    
    #bat dau luong luong cho client
    client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
    client_thread.start()
