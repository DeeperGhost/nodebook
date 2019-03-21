import csv
import json
import datetime

import pyrebase

from config import email,password,configurate
from collections import OrderedDict

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

class NODEBOOK:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(configurate)
        self.auth = self.firebase.auth()
        self.user = self.auth.sign_in_with_email_and_password(email,password)
        self.autht = self.auth.get_account_info(self.user['idToken'])
        print(self.autht)
        self.db = self.firebase.database()

    def PUSHH_NODE(self,event):
        self.db.child('names').push({'node':event,'time':datetime.datetime.today().strftime('%d/%m/%Y:%H.%M')})

    def PRINT_NODES(self):
        dbstr = self.db.child('names').get().val()

        keys = dbstr.keys()
        for key in keys:
            print(key,dbstr[key])

    def BUY_NODE(self):
        buy = input('Че подбросить?')
        print(buy + " <- зафиксировано, взято на контроль.")

    def DO_BUY_NODE(self):
        buy = input('Че Купил Епта?')
        print(buy + " <- Вычеркнуто, красавчик")

    #Очистить список записей полное обнуление
    def CLEAR_NODES(self):
        self.db.child('names').remove(self.user['idToken'])




def testClassNodebook():
    nodebook  = NODEBOOK()
    nodebook.PUSHH_NODE(event = 'жопник')
    nodebook.PRINT_NODES()
    # nodebook.BUY_NODE()
    # nodebook.DO_BUY_NODE()
    # nodebook.CLEAR_NODES()