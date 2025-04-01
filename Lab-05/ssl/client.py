import socket, ssl, threading

#
# Thong tin server 
server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    while True:
        try:
            # Nhan du lieu tu server
            data = ssl_socket.recv(1024)
            if not data:
                break
            
            print(f"Received from server: {data.decode('utf-8')}")
        except:
            pass
        finally:
            ssl_socket.close()
            print("Connection closed.")
            
#Tao socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#tao ssl context
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False

#thiet lap ket noi ssl
ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
ssl_socket.connect(server_address)

#bat dau luong luong nhan du lieu tu server
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

#bat dau gui du lieu den server
try:
    while True:
        message = input("Enter message to send to server: ")
        ssl_socket.send(message.encode('utf-8'))
        
except KeyboardInterrupt:
    pass
finally:    
    ssl_socket.close()
    print("Client socket closed.")