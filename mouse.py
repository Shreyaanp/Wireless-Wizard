import requests
import time
import serial
import pyautogui as pyag
serial_read = serial.Serial('COM3',9600)

while True:
    arduino_output = serial_read.readline()
    print(arduino_output)

