import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import credentials

cred = credentials.Certificate("C:/Users/Charlie Flynn/Downloads/charlie-s-project-c04fe-firebase-adminsdk-wncui-83481220fa.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://console.firebase.google.com/project/charlie-s-project-c04fe/database/charlie-s-project-c04fe-default-rtdb/data/~2F'})
