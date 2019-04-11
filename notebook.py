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
        self.pathDataTovarJson = "DataTovar.json"

    def PUSHH_NODE(self,event):
        self.db.child('names').push({'node':event,'time':datetime.datetime.today().strftime('%d/%m/%Y:%H.%M')})

    def PRINT_NODES(self):
        dbstr = self.db.child('dataProductBase').get().val()

        keys = dbstr.keys()
        for key in keys:
            print(key,dbstr[key])
        return dbstr

    def BUY_NODE(self, urgency, name, value):
        # buy = input('Че подбросить?')
        timenow =datetime.datetime.today().strftime('%d/%m/%Y:%H.%M')
        testNode = {'idDataProductBase': '-Lb1MDlKPbZ352DSEpOb', 'Value':700, 'Check' : 'false','DateAdd' : timenow,
                    'DateBuy':"",'DateCheckout':'', 'Urgensy':urgency,'MaxPrice':70,'MinPrice':''}
        self.db.child('HataNet').child('TransactionList').push(testNode)
        # print(buy + " <- зафиксировано, взято на контроль.")

    def DO_BUY_NODE(self):
        buy = input('Че Купил Епта?')
        print(buy + " <- Вычеркнуто, красавчик")

    #Очистить список записей полное обнуление
    def CLEAR_NODES(self):
        self.db.child('names').remove(self.user['idToken'])

    # Загрузить инфу о возможных товарах из Json
    def initBase(self):

        with open("dump.json", "r") as read_file:
            data = json.load(read_file)

        self.db.child('dataProductBase').remove()
        for i in data:
            self.db.child('dataProductBase').push(i)
        print("Загружено")

    # поиск в базе товаров по имени наброски рукожопные абы как работало
    def SEARCH_IN_BASE(self, name):

        dbBASE = self.db.child('dataProductBase').get().val()
        keys = dbBASE.keys()
        # Нахождение точного совпадения
        for key in keys:
            if name == dbBASE[key]['Name']:
                print("найдено--> ",key,dbBASE[key])
                return key
        # нахождение частичного совпадения
        t=[]
        for key in keys:
            if dbBASE[key]['Name'].find(name) > -1:
                print("найдено подстрока в --> ",key,dbBASE[key])
                t.append(key)
        if(t.__len__() > 0):
            return(t)
        # выход если совпаденией не найддено
        else:
            print('not found -->> please update Base if you want')
            return (0)


def testClassNodebook():
    nodebook  = NODEBOOK()

    # nodebook.BUY_NODE(urgency=6)

    print(nodebook.SEARCH_IN_BASE(name="Говядина"))

    # nodebook.PUSHH_NODE(event = 'жопник')
    nodebook.PRINT_NODES()

    # загружает базу товара из Json
    # nodebook.initBase()
    # nodebook.BUY_NODE()
    # nodebook.DO_BUY_NODE()
    # nodebook.CLEAR_NODES()