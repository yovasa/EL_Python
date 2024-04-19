import serial, time
arduino = serial.Serial("COM2", 9600)
time.sleep(1)
arduino.write(b'5')
time.sleep(2)

# print("hello world")