import csv
import json
import datetime

import pyrebase


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


def firebase_Test():
    # t = input('Start!\n')
    # email = "evgenioseev@gmail.com"

    email = "kareolis8@yandex.ru"
    password = "return123"

    config = {
        "apiKey": "AIzaSyCvEFOYGk5UyUXMWyV8TR0yI20RHHyHrec",
        "authDomain": "notebook-7304e.firebaseapp.com",
        "databaseURL": "https://notebook-7304e.firebaseio.com",
        "projectId": "notebook-7304e",
        "storageBucket": "notebook-7304e.appspot.com",
        "messagingSenderId": "409747025419"
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email,password)
    autht = auth.get_account_info(user['idToken'])
    print(autht)
    # auth.send_email_verification(user['idToken'])

    db = firebase.database()
    db.child('names').push({'node':'обед'})
