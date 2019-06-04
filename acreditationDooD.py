import os
import datetime

import shutil
import qrcode

from shutil import ignore_patterns
# import qrcode.image.svg


def count(dir, counter=0):
    pout = open('out.txt', 'w')
    "returns number of files in dir and subdirs"
    for pack in os.walk(dir):
        for f in pack[2]:
            pout.write(str(dir) +str(pack[0])+ str(f) +'\n' )
            counter += 1
    pout.close()
    return dir + " : " + str(counter) + "files"


# пробегает по директории и создает файл с рестром папок с пометкой пуста папка или нет
def compil_ot_file(dirName,fileOutName):
    # dirName = 'O:\\БАЗА УП НА АККРЕДИТАЦИЮ/'
    # dirName = 'D:\\up base'

    listName = ['аОПОП','аРПУД','прил 0 опоп','прил 1 КУГ','прил 2 УП','прил 3 МК','прил 4 РПУДы','прил 5 ПП НИР',
                'прил 6 пр ГИА','прил 7 ССК','прил 8 ЭБС','прил 9 МТО','прил 10 РОП']
    numb = 0
    numberPapok = 0

    bufSTR ="1"
    bufSTR2 = '2'

    fileOut = dirName + '\Struct\\'+fileOutName
    print(fileOut)
    with open(fileOut, "w", encoding="utf-8") as filewrite:
        for r, d, f in os.walk(dirName):
            for i in listName:
                if(i in str(r)):
                    b = r[dirName.__len__():str(r).rfind(str(i))]+';'+str(i)
                    bufSTR = b + ';' + ' 0' + '\n'

                    # bufSTR = str(r)+'/'+ '0' +'\n'
                    filewrite.write(bufSTR)
                    for file in f:
                        # print(str(r)+'/'+str(file) +'\n')
                        b = r[dirName.__len__():str(r).rfind(str(i))]+';'+str(i)
                        bufSTR = b + ';' + ' 1' + '\n'

                        if(bufSTR != bufSTR2):
                            filewrite.write(bufSTR)
                            numberPapok += 1
                            bufSTR2 = bufSTR
            numb += 1
            print("пройдено = " + str(numb) + ' найдено папок = '+str(numberPapok))
    print('процент заполнения = ' + str(100*numberPapok/numb)[0:4] + '%')

    fout = open(dirName + '\Struct\\' + 'src.txt', 'w')
    fout.write(datetime.datetime.today().strftime("%d/%m/%Y:%H-%M-%S"))
    fout.close()

# Создание QR кода
def qrcodeprint():
    # Create qr code instance
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )

    # The data that you want to store
    data = "https://www.dvfu.ru/about/rectorate/4915/the-department-of-organization-of-educational-activities/"
    probel = "\n"
    name = "Департамент организации образовательной деятельсти , - За подмену листа, убью сука!"
    # Add data
    qr.add_data(data)
    qr.add_data(probel)
    qr.add_data(name)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    img.save("image.jpg")

#копирует директорию с pdf
def copy_to_pdf(directory,directoryToPdf,school):
    print(school)
    # shutil.copytree(directory,directoryToPdf,ignore=ignore_patterns('*.doc', '*.docx','*.txt','*.pli','*.xml','*.plx','*.plm',
    #                                                                 '*.xlsx','*.doc','*.xls','*Арсеньев*',
    #                                                                 '*аспирантура*','*Большой Камень*','*Дальнегорск*',
    #                                                                 '*Находка*','*Уссурийск*','*ЦРПДО*',
    #                                                                 '*Электронные версии ОС ВО ДВФУ*',
    #                                                                 '*Электронные версии ФГОС ВО*',
    #                                                                 '*Электронные версии ФГОС ВО 3++*'))
    # рабочая схема
    shutil.copytree(directory+school,directoryToPdf+'/'+school,ignore=ignore_patterns('*.doc', '*.docx','*.txt','*.pli','*.xml','*.plx','*.plm','*.db',
                                                                    '*.xlsx','*.doc','*.xls','*.xlsm','*.rtf','*Арсеньев*',
                                                                    '*аспирантура*','*Большой Камень*','*Дальнегорск*',
                                                                    '*Находка*','*Уссурийск*','*ЦРПДО*',
                                                                    '*Электронные версии ОС ВО ДВФУ*',
                                                                    '*Электронные версии ФГОС ВО*',
                                                                    '*Электронные версии ФГОС ВО 3++*','*УВЦ*',
                                                                    '*российско-австралийская*','*российско-американская*',
                                                                    '*е выходя*'))
    #тестовая без папок
    # shutil.copytree(directory+school,directoryToPdf+'/'+school,ignore=ignore_patterns('*.doc', '*.docx','*.txt','*.pli','*.xml','*.plx','*.plm',
    #                                                                                   '*.xlsx','*.doc','*.xls','*.xlsm','*.rtf','*Арсеньев*',
    #                                                                                   '*аспирантура*','*Большой Камень*','*Дальнегорск*',
    #                                                                                   '*Находка*','*Уссурийск*','*ЦРПДО*',
    #                                                                                   '*Электронные версии ОС ВО ДВФУ*',
    #                                                                                   '*Электронные версии ФГОС ВО*',
    #                                                                                   '*Электронные версии ФГОС ВО 3++*','*УВЦ*',
    #                                                                                   '*российско-австралийская*','*российско-американская*',
    #                                                                                   '*е выходя*',
    #                                                                                   '*прил 0 опоп*','*прил 3 МК*','*прил 7 ССК*','*прил 8 ЭБС*','*прил 9 МТО*','*прил 10 РОП*'))
    print("Закопировано")

# выполняет задание по обновлению
def updateQuest():
    print("updateQuest")
    t= 'O:\БАЗА УП НА АККРЕДИТАЦИЮ\ШЭМ\Бакалавриат\\2014 г.н. ЗФО 38.03.01 Бухгалтерский учет, анализ и аудит\аОПОП'
    t1= '\ШЭМ\Бакалавриат\\2014 г.н. ЗФО 38.03.01 Бухгалтерский учет, анализ и аудит\аОПОП'
    dirToPDF = 'D:\\up base PDF\\UPDATE'
    dir1 = "O:\\БАЗА УП НА АККРЕДИТАЦИЮ"
    fileQuest = "ОБНОВЛЕНИЕ.txt"

    logUpdate = open('D:\\up base PDF\\logUpdate.txt', 'a')
    f = open(dir1+'\\'+fileQuest,'r')
    print(dir1+'\\'+fileQuest)
    for line in f:
        print(line)
    # shutil.copy(dir1+fileQuest,r'D:/1.txt')
        str1 = 'O'+line[1:]
        str1 = str1.replace('\n','')
        print(str1)
        str2 = str1.replace('O:\\БАЗА УП НА АККРЕДИТАЦИЮ',dirToPDF)

        run = datetime.datetime.today()
        logUpdate.write(str(run.__format__('%d-%m-%Y %H:%M:%S'))+' ' + str2+'\n')

        shutil.copytree(str1,str2,ignore=ignore_patterns('*.doc', '*.docx','*.txt','*.pli','*.xml','*.plx','*.plm','*.db',
                                                                                          '*.xlsx','*.doc','*.xls','*.xlsm','*.rtf','*Арсеньев*',
                                                                                          '*аспирантура*','*Большой Камень*','*Дальнегорск*',
                                                                                          '*Находка*','*Уссурийск*','*ЦРПДО*',
                                                                                          '*Электронные версии ОС ВО ДВФУ*',
                                                                                          '*Электронные версии ФГОС ВО*',
                                                                                          '*Электронные версии ФГОС ВО 3++*','*УВЦ*',
                                                                                          '*российско-австралийская*','*российско-американская*',
                                                                                          '*е выходя*'))


    logUpdate.close()
def copySHEN(directory,directoryToPdf,school):
    listName = ['аОПОП','аРПУД','прил 0 опоп','прил 1 КУГ','прил 2 УП','прил 3 МК','прил 4 РПУДы','прил 5 ПП НИР',
                'прил 6 пр ГИА','прил 7 ССК','прил 8 ЭБС','прил 9 МТО','прил 10 РОП']

    shutil.copytree(directory+school,directoryToPdf+'/'+school,ignore=ignore_patterns('*аОПОП*','*аРПУД*','*прил 0 опоп*','*прил 3 МК*','*прил 4 РПУДы*','*прил 5 ПП НИР*',
                                                                                      '*прил 6 пр ГИА*','*прил 7 ССК*','*прил 8 ЭБС*','*прил 9 МТО*','*прил 10 РОП*'))
def copyDrozdova(directory,directoryToPdf,school):
    listName = ['аОПОП','аРПУД','прил 0 опоп','прил 1 КУГ','прил 2 УП','прил 3 МК','прил 4 РПУДы','прил 5 ПП НИР',
                'прил 6 пр ГИА','прил 7 ССК','прил 8 ЭБС','прил 9 МТО','прил 10 РОП']

    shutil.copytree(directory,directoryToPdf+'/'+school,ignore=ignore_patterns('*прил 1 КУГ*','*прил 2 УП*'))


def accreditation():
    dirName = 'O:\\БАЗА УП НА АККРЕДИТАЦИЮ/'
    # dirName = 'D:\\up base'
    dirToPDF = 'D:\\up base PDF'
    SHENDOOD = 'D:\\SHENDOOD'
    SHENDROZDOVA = 'W:\ШЕН_Дроздова'
    fileOutAll = 'file.txt'
    fileOutPDF = 'filePDF.txt'

    # Создать общий выходной файл
    compil_ot_file(dirName,fileOutAll)



    # Создать выходной файл для PDF директории
    # compil_ot_file(dirToPDF, fileOutPDF)

    # qrcodeprint()



    # копирует пдфки
    # copy_to_pdf(dirName,dirToPDF,'ШИГН') #ШИГН
    # copy_to_pdf(dirName,dirToPDF,'ЮШ') #ЮШ
    # copy_to_pdf(dirName,dirToPDF,'ШЕН')
    # copy_to_pdf(dirName,dirToPDF,'ИШ')
    # copy_to_pdf(dirName,dirToPDF,'ШРМИ')

    # copy_to_pdf(dirName,dirToPDF,'ШЭМ')
    # copy_to_pdf(dirName,dirToPDF,'ШБМ')
    # copy_to_pdf(dirName,dirToPDF,'ШЦЭ')

    # обновление по запросу
    # updateQuest()

    # Копирует УПЫ И КУГИ с ДООД
    # copySHEN(dirName,SHENDOOD,'ШЕН')

    # Копирует из дроздова не УПЫ и КУГИ
    # copyDrozdova(SHENDROZDOVA,SHENDOOD,'ШЕНДРОЗДОВА')