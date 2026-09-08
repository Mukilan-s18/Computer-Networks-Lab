import socket
import threading
import time

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(1)
    
    conn, addr = server.accept()
    with open("output.txt", "a") as f:
        f.write(f"Server: Connection accepted from {addr}\n")
    
    data = conn.recv(1024).decode('utf-8')
    with open("output.txt", "a") as f:
        f.write(f"Server: Received message - {data}\n")
    
    conn.send(f"Echo: {data}".encode('utf-8'))
    conn.close()
    server.close()

def run_client():
    time.sleep(1) 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 8080))
    
    msg = "Hello Transport Layer!"
    client.send(msg.encode('utf-8'))
    
    resp = client.recv(1024).decode('utf-8')
    with open("output.txt", "a") as f:
        f.write(f"Client: Sent message - {msg}\n")
        f.write(f"Client: Received response - {resp}\n")
    client.close()

open("output.txt", "w").close()

t1 = threading.Thread(target=run_server)
t2 = threading.Thread(target=run_client)

t1.start()
t2.start()

t1.join()
t2.join()
