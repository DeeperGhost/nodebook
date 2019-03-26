import json

class CatalogTovar :
    def __init__(self):
        self.path = 'dump.json'
        self.section = 'Section'
        self.name = 'Name'
        self.value = 'Value'
        self.dimension = 'Dimension'

        with open("dump.json", "r") as read_file:
            self.catalog = json.load(read_file)


    def addTovar(self,section, name,  value, dimension):
        t = {self.section: section, self.name: name, self.value: value, self.dimension: dimension}
        if t in self.catalog:
            print('Элемент есть в списке')
        else:
            self.catalog.append(t)


    def testAddNode(self):
        self.addTovar(section="хищное",name='иичко',value="",dimension='литр')
        with open("dump.json", "w") as write_file:
            json.dump(self.catalog, write_file,indent=2, ensure_ascii=False)


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



