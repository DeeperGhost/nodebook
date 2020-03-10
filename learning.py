from numpy import loadtxt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

def l0():
    # i2()
    NN()
    # print(0)
    # directory = 'D:\mashinlearn/rno/'
    # # file = 'pima-indians-diabetes.data.csv'
    # file = 'testlearn2.csv'
    # # load the dataset
    #
    # dataset = loadtxt(directory+file, delimiter=',')
    # dataset1 = loadtxt(directory+'testY.csv', delimiter=',')
    # # split into input (X) and output (y) variables
    # X = dataset[:,0:5]
    # y = dataset[:,5]
    #
    # # X1 = dataset1[:,0:5]
    # y1 = dataset1[:,5]
    #
    # X1 = np.array([1.,1.,1.,1.,1.])
    # # X1 = [1.,1.,1.,1.,1.]
    # print('y=',type(X))
    # print('X=',X)
    # print('X1=',type(X1))




    # NN()

def NN():
    directory = 'D:\mashinlearn/rno/'
    # file = 'pima-indians-diabetes.data.csv'
    file = 'testlearn2.csv'
    # load the dataset

    dataset = loadtxt(directory+file, delimiter=',')
    dataset1 = loadtxt(directory+'testY.csv', delimiter=',')
    # split into input (X) and output (y) variables
    X = dataset[:,0:5]
    y = dataset[:,5]

    # X1 = dataset1[:,0:5]
    y1 = dataset1[:,5]

    X1 = np.array([[1,1,1,1,1],[2,2,2,2,2]])
    # X1 = [1.,1.,1.,1.,1.]
    # print(y)
    # print(X)
    # print(X1)




    # define the keras model
    # model = Sequential()
    # model.add(Dense(12, input_dim=8, activation='relu'))
    # model.add(Dense(8, activation='relu'))
    # model.add(Dense(1, activation='sigmoid'))
    model = Sequential()
    model.add(Dense(15, input_dim=5, activation='relu'))
    model.add(Dense(15, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(5, activation='relu'))
    model.add(Dense(15, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(5, activation='relu'))
    # model.add(LSTM(2))
    model.add(Dense(1, activation='relu'))



    # compile the keras model
    # model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # model.compile(loss='squared_hinge', optimizer='sgd', metrics=['accuracy'])
    # model.compile(loss='mse',optimizer='adam', metrics=['accuracy'])
    # model.compile(loss='binary_crossentropy',optimizer='adam')
    model.compile(optimizer="adam", loss="mean_squared_error")

    # fit the keras model on the dataset
    # model.fit(X, y, epochs=15, batch_size=10,validation_data = (X, y))
    model.fit(X, y, epochs=150)

    # evaluate the keras model
    accuracy = model.evaluate(X, y)
    print('Accuracy: %.2f' % (accuracy*100))
    # print('t=',_)
    # print ('x= ',x)

    # make class predictions with the model
    # predictions = model.predict_classes(X)
    p = model.predict(X)
    # summarize the first 5 cases
    for i in range(10):
        print('%s => %d (expected %d)' % (X[i].tolist(), p[i], y[i]))
    p1 = model.predict(X1)

    for i in range(10):
        print('test X1=',X1[i],p1[i],y1[i])

def i2():
    print("123")
    i = 0
    directory = 'D:\mashinlearn/rno/'
    fileIn = 'rno.txt'
    # fileOut = 'out.txt'
    fileX = 'fileX.txt'
    fileY = 'fileY.txt'
    with open(directory + fileX, "w") as foutX:
        with open(directory + fileY, "w") as foutY:
            with open(directory + fileIn, "r") as fileread:
                while i < 1000:
                    strb = fileread.readline()
                    p = strb.split(' ')
                    p.sort()
                    # filewrite.write(str(p.__len__())+' ' + strb+'\n')
                    foutY.write(str(p.__len__())+'~' + strb)
                    for j in p:
                        foutX.write(str(j))
                    # foutX.write('\n')
                    print(i)
                    i+=1

            fileread.close()
        foutY.close()
    foutX.close()