import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('C:/Users/Charlie Flynn/Downloads/charlie-s-project-c04fe-firebase-adminsdk-wncui-83481220fa.json')
firebase_admin.initialize_app(cred,{'databaseURL': 'https://charlie-s-project-c04fe-default-rtdb.europe-west1.firebasedatabase.app/'})

ref = db.reference()

ref.update({'led_log':''})

ref = db.reference().child('led_log')

i = 0
while i < 10:
    ref.update({'iteration':False})
    i = i + 1


