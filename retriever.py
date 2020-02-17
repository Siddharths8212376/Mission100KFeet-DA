# the firebase retriever module
# to be run constantly
import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate('./ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

users_ref = db.collection(u'raw-data')
docs = users_ref.stream()

for doc in docs:
    # print(u'{} => {}'.format(doc.id, doc.to_dict()))
    data_dictionary = doc.to_dict()
    for id, data in data_dictionary.items():
        with open(str(id) + '.txt', mode='w', encoding='utf-8', errors='ignore') as write_file:
            write_file.write(data)
        