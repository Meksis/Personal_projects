import bluetooth as bt
import subprocess as sp
import socket as sc
from bluetooth import *

target_device='HC-06'    #or input()

port = 1
use_pass=0

nearby_devices = discover_devices(duration=1, lookup_names=True, flush_cache=True)

print('COMMON DEVICES\n')
for address, name in nearby_devices:
    #name=nearby_devices[counter][1]
    print(f'{name} \naddress: {address}')
    if name==target_device:
        target_address=address
        print('Target device was founded')
    else:
        print('Target device not founded')

    print('\n')
    #print(f'name of device = {bt.lookup_name( address )}, address = {address}')


sp.call("kill -9 `pidof bluetooth-agent`", shell=True)

if use_pass==1:
    status = sp.call("bluetooth-agent " + passkey + " &",shell=True)
else:
    status = sp.call("bluetooth-agent "+" &",shell=True)

    s = sc.socket(socket.AF_BLUETOOTH, sc.SOCK_STREAM, sc.BTPROTO_RFCOMM)
    #s = bt.BluetoothSocket(bt.RFCOMM)
    s.connect((target_address, port))
