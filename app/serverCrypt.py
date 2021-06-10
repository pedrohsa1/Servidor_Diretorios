from random import randint
import rpyc
from socket import gethostbyname,gethostname
from constRPYC import *
from rpyc.utils.server import ThreadedServer


class ServerCrypt(rpyc.Service): #alterar ServerCrypt para o nome do servidor
    priv_key = 1
    def __encrypt(self, mensagem, pub_key):
        value = ''
        for item in mensagem:
            value = value + chr((ord(item) + pub_key + self.priv_key))
        return value
    
    def __decrypt(self, mensagem, pub_key):
        value = ''
        for item in mensagem:
            value = value + chr((ord(item) - int(pub_key) - self.priv_key))
        return value

    def exposed_encrypt(self, text):
        pub_key = randint(1, 25)
        enc_message = self.__encrypt(text, pub_key)
        return (enc_message, pub_key)

    def exposed_decrypt(self, message, pub_key):
        return self.__decrypt(message, pub_key)


if __name__ == "__main__":
    server = ThreadedServer(ServerCrypt, port = 20303) #alterar o ServerCrypt para o nome do servidor
    conn = rpyc.connect(host=DIR_SERVER, port=DIR_PORT)
    my_address = gethostbyname(gethostname())
    (reg, token) = conn.root.exposed_register("ServerCrypt", my_address, 20303)
    # print (reg) #precisa ser alterado para receber o token/senha de alteração
    if reg:
        print(f"First time connection. Token: {token}")
        server.start()
    else:
        print("Relaunching")
        option = str(input("1) Update service.\n2) Remove sevice.\n3) Cancel\n"))
        if option == "1" or option == "2":
            if option == "1" : 
                token = str(input("Token: "))
                update = conn.root.exposed_update_register("ServerCrypt", my_address, 20303, token)
                if update:
                    print("Updated! Initializing...")
                    server.start()
                else: 
                    print("Token not authorized")
            else:
                token = str(input("Token: "))
                remove = conn.root.exposed_unregister("ServerCrypt", token)
                if remove: 
                    print("Service removed")
                else:
                    print("Token not authorized")
        else:
            print("Good bye!")