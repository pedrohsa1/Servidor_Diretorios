import rpyc
from socket import gethostbyname,gethostname
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class ServerCalculadora(rpyc.Service): #alterar ServerCalculadora para o nome do servidor
    value = []

    def exposed_sum(self, num1, num2):
        print(f"{num1} soma {num2}")
        return num1+num2

    def exposed_sub(self, num1, num2):
        print(f"{num1} sub {num2}")
        return num1-num2

    def exposed_multi(self, num1, num2):
        print(f"{num1} multi {num2}")
        return num1*num2

    def exposed_divi(self, num1, num2):
        print(f"{num1} divi {num2}")
        return num1/num2



if __name__ == "__main__":
    server = ThreadedServer(ServerCalculadora, port = 20202) #alterar o ServerCalculadora para o nome do servidor
    conn = rpyc.connect(host=DIR_SERVER, port=DIR_PORT)
    my_address = gethostbyname(gethostname())
    (reg, token) = conn.root.exposed_register("ServerCalculadora", my_address, 20202)
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
                update = conn.root.exposed_update_register("ServerCalculadora", my_address, 20202, token)
                if update:
                    print("Updated! Initializing...")
                    server.start()
                else: 
                    print("Token not authorized")
            else:
                token = str(input("Token: "))
                remove = conn.root.exposed_unregister("ServerCalculadora", token)
                if remove: 
                    print("Service removed")
                else:
                    print("Token not authorized")
        else:
            print("Good bye!")
