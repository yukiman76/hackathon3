"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).

MAC
system_profiler SPBluetoothDataType

LINUX
hciconf 
"""

import socket

hostMACAddress = '00:1f:e1:dd:08:3d' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data)
except:
    print("Closing socket")
    client.close()
    s.close()
