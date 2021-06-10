import rpyc
from constRPYC import *

class Client:
    conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)
    (address, port) = conn_directory.root.exposed_lookup("ServerCrypt")
    if address == 'error':
        print(port)
    else:
        print(f"Connection: {address}:{port}")
        conn_server = rpyc.connect(address, port)
        operation = str(input("1) Encrypt\n2) Decript\n3) Cancel\n"))
        if operation == "1" or operation == "2":
            if operation == "1":
                text = input("Message: ")
                (encText, pub_key) = conn_server.root.exposed_encrypt(text)
                print(f"Encrypted: {encText}\n Public Key {pub_key}")
                file = open("enc_message.txt", 'w')
                file.write(encText)
                file.close()
            else:
                enc_message = input("Type the Encryped Message: ")
                print(f"Encripted message: {enc_message}")
                pub_key = input("Public Key: ")
                text = conn_server.root.exposed_decrypt(enc_message, pub_key)
                print(f"Message: {text}")
        else:
            print("Good bye!")
