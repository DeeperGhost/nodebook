from notebook import notebok
from notebook import NODEBOOK
from notebook import firebase_Test
import glob

from acreditationDooD import compil_ot_file

def testClassNodebook():
    nodebook  = NODEBOOK()
    nodebook.PUSHH_NODE(event = 'жопник')
    nodebook.PRINT_NODES()



def main():
    dirName = 'O:\\БАЗА УП НА АККРЕДИТАЦИЮ/'
    # dirName = 'D:\\up base'
    dirToPDF = 'D:\\up base PDF'
    fileOutAll = 'file.txt'
    fileOutPDF = 'filePDF.txt'

    # notebok('обед',datetime.datetime.today().strftime('%d/%m/%Y:%H/%M'))
    testClassNodebook()


    # firebase_Test(event = 'Ужин')

    # Создать общий выходной файл
    # compil_ot_file(dirName,fileOutAll)
    # Создать выходной файл для PDF директории
    # compil_ot_file(dirToPDF, fileOutPDF)

    # qrcodeprint()

    # копирует пдфки
    # copy_to_pdf(dirName,dirToPDF)






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
if __name__ == '__main__':
    main()