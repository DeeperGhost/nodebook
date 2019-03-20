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
def copy_to_pdf(directory,directoryToPdf):
    shutil.copytree(directory,directoryToPdf,ignore=ignore_patterns('*.doc', '*.docx','*.txt','*.pli','*.xml','*.plx','*.plm',
                                                                    '*.xlsx','*.doc','*.xls'))
    print("Закопировано")


