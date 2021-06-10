import rpyc
from constRPYC import *

class Client:
    conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)
    (address, port) = conn_directory.root.exposed_lookup("ServerCalculadora")
    if address == 'error':
        print(port)
    else:
        print(f"Connection: {address}:{port}")
        numA = int(input("Primeiro numero: "))
        numB = int(input("Segundo numero: "))
        conn_server = rpyc.connect(address, port)
        soma = conn_server.root.exposed_sum(numA, numB)
        sub = conn_server.root.exposed_sub(numA, numB)
        multi = conn_server.root.exposed_multi(numA, numB)
        divi =conn_server.root.exposed_divi(numA, numB)
        print(f"Soma: {soma}")
        print(f"Sub: {sub}")
        print(f"multi: {multi}")
        print(f"Divi: {divi}")