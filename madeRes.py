import json

def LoadDataRes():
    litr = 'литр'
    gr = 'гр.'
    t1= [{'Section':'кисломолочные','Name':'Молоко','обьем':'','размерность': litr},
         {'Section':'кисломолочные','Name':'Сметана','обьем':'','размерность': gr},
         {'Section':'кисломолочные','Name':'Кефир','обьем':'','размерность': litr},
         {'Section':'кисломолочные','Name':'Творог','обьем':'','размерность': gr},
         {'Section':'кисломолочные','Name':'Моцарела','обьем':'','размерность': gr},
         {'Section':'кисломолочные','Name':'Пармезан','обьем':'','размерность': gr},
         {'Section':'кисломолочные','Name':'Масдам','обьем':'','размерность': gr},
         {'Section':'кисломолочные','Name':'Сыр','обьем':'','размерность': gr},
         {'Section':'кисломолочные','Name':'Сыр плавленый','обьем':'','размерность': gr}
         ]

    with open("dump.json", "w") as write_file:
        json.dump(t1, write_file,indent=2, ensure_ascii=False)

    # with open("dump.json", "r") as read_file:
    #     data = json.load(read_file)

