import bluetooth

nearby_devices = bluetooth.discover_devices()

for addr, name in nearby_devices:
    print(f'{addr} : {name}')

bd_addr = input("Enter the address of the device you want to connect to: ")

port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

while True:
    data = sock.recv(1024)
    print(data)

sock.close()