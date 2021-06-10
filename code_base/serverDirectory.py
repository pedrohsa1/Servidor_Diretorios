import rpyc
from constRPYC import * 
from rpyc.utils.server import ThreadedServer

class Directory(rpyc.Service):
    registry = {}

    def exposed_register(self, server_name, ip_adress, port_number): 
    
    def exposed_update_register(self, server_name, ip_adress, port_number, token):
    
    def exposed_unregister(self, server_name):  
    
    def exposed_lookup(self, server_name):
        

if __name__ == "__main__":
    server_dir = ThreadedServer(Directory, port = DIR_PORT )
    print ("Server Started. Waiting Requests")
    server_dir.start()