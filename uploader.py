# the firebase uploader plugin
# to be run constantly using scheduler
import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

data = open('./mission_flight/lora_final.txt', encoding='utf-8', errors='ignore')
content = data.read()
# print(content)

doc_ref = db.collection(u'raw-data').document(u'data')
doc_ref.set({u'lora_final': content})


