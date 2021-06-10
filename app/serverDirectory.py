from random import randint
import rpyc
from constRPYC import * 
from rpyc.utils.server import ThreadedServer

servers = {}
class Directory(rpyc.Service):

    def exposed_register(self, server_name, ip_adress, port_number): 
        addr = (ip_adress,port_number)
        if server_name not in servers:
            #Gera hash para gerar o token
            token = str(hash(server_name)+hash(randint(0,50)))
            #informações do servidor
            servers [server_name] = {'ip': addr , 'token': token}
            print(f"\n###\nConnected Server:{server_name} \n IP/PORT: {ip_adress}:{port_number} \n Token: {token}\n###\n\n")
            success = (True, token)
            return success
        else:
            failure = (False, "null")
            return failure

    def exposed_update_register(self, server_name, ip_adress, port_number, token):
        if servers[server_name]['token'] == token:
            addr = (ip_adress,port_number)
            servers [server_name]['ip'] = addr
            print(f"Updated {server_name} = {servers[server_name]}")
            return True
        else:
            return False

    def exposed_unregister(self, server_name, token):  
        if servers[server_name]['token'] == token:
            servers.pop(server_name)
            print(f"Removed {server_name}")
            print(f"Full: {servers}")
            return True
        else:
            return False

    def exposed_lookup(self, server_name):
        if server_name in servers:
            return servers[server_name]['ip']
        else:
            notreg = ("error", "Service not registered")
            return notreg


if __name__ == "__main__":
    print (f"\n\nServer Started on {DIR_PORT}. Waiting Requests\n\n")
    server_dir = ThreadedServer(Directory, port = DIR_PORT, protocol_config={"allow_public_attrs": True} )
    server_dir.start()