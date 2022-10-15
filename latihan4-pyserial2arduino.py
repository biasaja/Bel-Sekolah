#latihan4-pyserial2arduino.py
import serial
import time
 
ser = serial.Serial('COM4', 9600, timeout = 1)
time.sleep(3)
 
def getH():
    ser.write(b'H')
    arduinoData = ser.readline().decode('ascii')
    return arduinoData

def getL():
    ser.write(b'L')
    arduinoData = ser.readline().decode('ascii')
    return arduinoData

e = 0
while e <= 5:
    uinput = input("Silahkan masukkan L atau H: ").upper()
    #userInput = eval('Get data point?')
 
    if uinput == 'H':
        getH()
        continue
    elif uinput == "L":
        getL()
        continue
    else:
        print("Salah ketik mas...")
    e += 1
else:
    print("Buyar, salah terus guest...")

