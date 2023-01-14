mouse = Controller()

ser = serial.Serial('COM3',baudrate = 115200)       # Setting Serial port number and baudrate
while 1:
    count = 0                             # While loop to continuesly scan and read data from serial port and execute
    dump = ser.readline()                           # Reading Serial port
    dump = str(dump)                                # Converting byte data into string
    dump = dump[2:-5]                               # Cleaning up the raw data recieved from serial port
    data = dump.split(',')
    # print("hello")
            # Spliting up the data to individual items in a list. the first item being the data identifier
    print(data)                     # Calculating the difference between the current Y value and the previous Y value
    if(len(data)==5):
        if (data[0] == "DATAL" ):
            mouse.move(int(int(data[2])/1.6),int(int(data[1])/1.5))
