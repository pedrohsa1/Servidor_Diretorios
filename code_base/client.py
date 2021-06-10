import rpyc
from constRPYC import *

class Client:
    conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)
    (address, port) = conn_directory.root.exposed_lookup("ServerName")
    print (address, port)

    conn_server = rpyc.connect(address, port)
    conn_server.root.exposed_sum(2, 4)
