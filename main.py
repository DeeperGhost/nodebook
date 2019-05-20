from notebook import notebok
from notebook import testClassNodebook

import glob
from acreditationDooD import compil_ot_file
from acreditationDooD import copy_to_pdf
from acreditationDooD import copySHEN
from acreditationDooD import copyDrozdova

from madeRes import CatalogTovar
import datetime

def main():
    run = datetime.datetime.today()
    print(str(run.__format__('%d-%m-%Y %H:%M:%S')) + " <-- Start")
    dirName = 'O:\\БАЗА УП НА АККРЕДИТАЦИЮ/'
    # dirName = 'D:\\up base'
    dirToPDF = 'D:\\up base PDF'
    SHENDOOD = 'D:\\SHENDOOD'
    SHENDROZDOVA = 'W:\ШЕН_Дроздова'
    fileOutAll = 'file.txt'
    fileOutPDF = 'filePDF.txt'

    # notebok('обед',datetime.datetime.today().strftime('%d/%m/%Y:%H/%M'))

    # testClassNodebook()


    # работит

    # p = CatalogTovar()
    # p.testAddNode()
    # p.readCSV()


    # Создать общий выходной файл
    compil_ot_file(dirName,fileOutAll)



    # Создать выходной файл для PDF директории
    # compil_ot_file(dirToPDF, fileOutPDF)

    # qrcodeprint()

    # копирует пдфки
    # copy_to_pdf(dirName,dirToPDF,'ШИГН') #ШИГН
    # copy_to_pdf(dirName,dirToPDF,'ЮШ') #ЮШ
    # copy_to_pdf(dirName,dirToPDF,'ШЕН')

    # Копирует УПЫ И КУГИ с ДООД
    # copySHEN(dirName,SHENDOOD,'ШЕН')

    # Копирует из дроздова не УПЫ и КУГИ
    # copyDrozdova(SHENDROZDOVA,SHENDOOD,'ШЕНДРОЗДОВА')



    # with open('file.csv', mode='w') as csvf:
    #     csvf = csv.writer(csvf, delimiter=';')#, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     for r, d,f in os.walk(dirName):
    #         name = str(r).replace(dirName,'')
    #         csvf.writerow(name.split('\\'))
    #         numb+=1
    #         print("пройдено = "+ str(numb) )

    # print(next(os.walk(dirName)))
    #
    # print(count(dirName))

    fin = datetime.datetime.today()
    LeadTime = fin - run

    print(str(run.__format__('%d-%m-%Y %H:%M:%S')) + " <-- Start")
    print(str(fin.__format__('%d-%m-%Y %H:%M:%S')) + " <-- Finished")

    print('Lead time = ' + str(LeadTime))

if __name__ == '__main__':
    main()