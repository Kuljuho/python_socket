import socket

HOST = '127.0.0.1'
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Palvelin kuuntelee osoitteessa {HOST}:{PORT}")
    
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Yhteys muodostettu osoitteesta {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Vastaanotettu viesti: {data.decode()}")