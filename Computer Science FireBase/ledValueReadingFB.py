import serial
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM3"
ser.open()


cred = credentials.Certificate('C:/Users/Charlie Flynn/Downloads/charlie-s-project-c04fe-firebase-adminsdk-wncui-83481220fa.json')
firebase_admin.initialize_app(cred,{'databaseURL': 'https://charlie-s-project-c04fe-default-rtdb.europe-west1.firebasedatabase.app/'})


ref = db.reference()
ref.update({'led_log':''})
ref = db.reference().child('led_log')


source = input("Please input the colour of this LED: ")


while True:
    mb_led = str(ser.readline().decode('utf-8'))
    mb_led = mb_led.replace(" ", "")
    mb_led = mb_led.replace("\r\n","")
    print(mb_led)
    if mb_led.isdigit():
        if mb_led == '1':
            val = "ON"
        else:
            val = "OFF"
        ref.update({str(int(time.time())):{'LED':mb_led, 'Colour':source, 'Value':val}})
    else:
        print("Check data source")