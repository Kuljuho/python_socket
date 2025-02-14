import socket

def laheta_viesti():
    HOST = '127.0.0.1' 
    PORT = 65432    

    viesti = "Tervehdys palvelimelle!"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Yhdistetään osoitteeseen {HOST}:{PORT}")
        s.connect((HOST, PORT))
        
        print(f"Lähetetään viesti: {viesti}")
        s.sendall(viesti.encode())
        print("Viesti lähetetty")

if __name__ == "__main__":
    try:
        laheta_viesti()
    except KeyboardInterrupt:
        print("\nOhjelma keskeytetty käyttäjän toimesta")
    except ConnectionRefusedError:
        print("Yhteyttä palvelimeen ei voitu muodostaa. Varmista että palvelin on käynnissä.")