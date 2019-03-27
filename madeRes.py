import json
import csv

class CatalogTovar :
    def __init__(self):
        self.path = 'dump.json'
        self.section = 'Section'
        self.name = 'Name'
        self.value = 'Value'
        self.dimension = 'Dimension'
        self.caption = 'Caption'

        try:
            with open("dump.json", "r") as read_file:
                self.catalog = json.load(read_file)
        except FileNotFoundError:
            print('файл загрузки было пустенько')
            self.catalog = []

    # Добавление товара через секцию, имя
    def addTovar(self,section, name,  value, dimension,caption):
        t = {self.section: section, self.name: name, self.value: value, self.dimension: dimension,self.caption:caption}
        if t in self.catalog:
            print('Элемент есть в списке')
        else:
            self.catalog.append(t)
            print('Успешно добавлено')

    # Дампит каталог товаров -> Json
    def testAddNode(self):
        # self.addTovar(section="хищное",name='колбаса вареная',value="",dimension='кг')
        with open("dump.json", "w") as write_file:
            json.dump(self.catalog, write_file,indent=2, ensure_ascii=False)

    # Читает из 'BdTovarRes.csv' список базовых товаров и пишет в json
    def readCSV(self):
        path = 'BdTovarRes.csv'
        with open(path, "r", newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for line in reader:
                self.addTovar(section=line[0],name=line[1],value=line[2],dimension=line[3],caption=line[4])
                print(line)

        self.testAddNode()




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



