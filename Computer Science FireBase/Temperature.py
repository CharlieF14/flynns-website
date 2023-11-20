#You need to install the pyserial package to use the serial ports
import serial
import serial.tools.list_ports as list_ports
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial



ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM3'
ser.open()


cred = credentials.Certificate('https://lwetb-my.sharepoint.com/:u:/g/personal/18cflynn_acc_lwetb_ie/EcsAHlQfgA9BqqGurGtUoPoB25yalkfx5NFMcjBkaa_8Ug?e=bkTbfg')
firebase_admin.initialize_app(cred,{'databaseURL': 'https://console.firebase.google.com/u/2/project/charlie-s-project-c04fe/database/charlie-s-project-c04fe-default-rtdb/data/~2F'})
ref = db.reference()
ref.update({'temperature_log':''})
ref = db.reference().child('temperature_log')
source = input('Please input the source of this data: ')
i = 0
while True:
    mb_temperature = str(ser.readline().decode('utf-8'))
    mb_temperature = mb_temperature.replace(" ", "")
    mb_temperature = mb_temperature.replace("\r\n","")
    
    if mb_temperature.isdigit():
        ref.update({str(int(time.time())):{'Temperature':mb_temperature, 'Location':source}})
        i = i + 1
    else:
        print("Check data source")