import json
from tabulate import tabulate
with open ('tsis4\json\sample-data.json', 'r') as access:
    read = json.load(access)

nested_list = []
for item in read['imdata']:
    attributes = item['l1PhysIf']['attributes']
    if attributes['dn'] == "topology/pod-1/node-201/sys/phys-[eth1/33]" or attributes['dn'] == "topology/pod-1/node-201/sys/phys-[eth1/34]" or attributes['dn'] == "topology/pod-1/node-201/sys/phys-[eth1/35]":
        nested_list.append([attributes['dn'], attributes['descr'], attributes['speed'], attributes['mtu']])



        
print("Interface Status")
print("================================================================================")      
print (tabulate(nested_list, headers=["DN", "Description", "Speed", "MTU"]))

   
        
            

    
    

