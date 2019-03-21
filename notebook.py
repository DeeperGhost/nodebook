import csv
import json
import datetime

import pyrebase

from config import email,password,configurate

def notebok(NameAction, timeAction):
    'https://console.firebase.google.com/project/notebook-7304e/database/firestore/data~2Fnodebook~2FAfRFO98EVy2j4JysoDXW'
    directoryFile = '//WS03057/selfDataRes'

    with open(directoryFile + "/data_file.json", "r") as read_file:
        data = json.load(read_file)
        # if not first_char:
        #     print "file is empty" #first character is the empty string..
        # else:

    for i in data:
        print(i)
    # Загружено таки

    #     Формирование ноды
    node = [NameAction,timeAction]

    #Добавление ноды
    data.append(node)

    # Write CSV file
    with open(directoryFile + "/data_file.json", "w") as write_file:
        json.dump(data, write_file,indent=2, ensure_ascii=False)
    print('Finished 1')


def firebase_Test(event):
    # t = input('Start!\n')



    firebase = pyrebase.initialize_app(configurate)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email,password)
    autht = auth.get_account_info(user['idToken'])
    print(autht)
    # auth.send_email_verification(user['idToken'])

    db = firebase.database()
    db.child('names').push({'node':event,'time':datetime.datetime.today().strftime('%d/%m/%Y:%H.%M')})
    # result = db.child('names').get()
    dbstr = db.child('names').get().val()
    # tr = json.loads(db.child('names').get().val().items())
    keys = dbstr.keys()
    for key in keys:
        print(key,dbstr[key])


