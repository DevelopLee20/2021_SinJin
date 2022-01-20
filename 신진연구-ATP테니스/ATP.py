from typing import Sequence
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras import utils
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models, optimizers

class Model():
    def __init__(self):
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.result = []
        
    # 파일명, 훈련데이터 비율, 원-핫 인코딩 여부, 프린트 옵션
    # 리스트 반환
    def load_data(self, file_name, feature, test_rate):
        csv = pd.read_csv(file_name)

        X = csv.values[:,:feature]
        y = csv.values[:,feature]
        
        y = utils.to_categorical(y, 2)
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, stratify=y, test_size=test_rate, random_state=1004)

    def print_result(self):
        print(pd.DataFrame(self.result, columns=['Model','Optimizer','lr','epoch','batch','train_acc','test_acc']))

    # 데이터 리스트, 학습률, 반복횟수, 배치 사이즈
    def Model_DNN(self, lr, epoch, batch):
        model = models.Sequential()
        model.add(layers.Dense(64, input_shape=(self.X_train.shape[1],), activation='relu'))
        model.add(layers.Dense(32, activation='relu'))
        model.add(layers.Dense(8, activation='relu'))
        model.add(layers.Dense(2,  activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer=optimizers.Adam(lr), metrics=['accuracy'])
        model.summary()
        history = model.fit(self.X_train, self.y_train, epochs=epoch, verbose=0, batch_size=batch)
        score = model.evaluate(self.X_test, self.y_test, verbose=0)
        
        self.result.append(["DNN", "Adam", lr, epoch, batch, history.history['accuracy'][-1] ,score[1]])
        
    def Model_CNN(self, lr, epoch, batch):
        X_train = self.X_train.reshape(self.X_train.shape[0], 18, 1, 1)
        X_test = self.X_test.reshape(self.X_test.shape[0], 18, 1, 1)
        
        model = models.Sequential()
        model.add(layers.Conv2D(64, kernel_size=(5,1), input_shape=(18,1,1), activation='relu'))
        model.add(layers.Conv2D(64, (5,1), activation='relu'))
        model.add(layers.MaxPooling2D(pool_size=(3,1)))
        model.add(layers.Dropout(0.25))
        model.add(layers.Flatten())
        model.add(layers.Dense(16, activation='relu'))
        model.add(layers.Dropout(0.25))
        model.add(layers.Dense(2, activation='softmax'))
        model.compile(loss='categorical_crossentropy',  optimizer=optimizers.RMSprop(lr), metrics=['accuracy'])
        model.summary()
        history = model.fit(X_train, self.y_train, epochs=epoch, verbose=0, batch_size=batch)
        score = model.evaluate(X_test, self.y_test, verbose=0)
        
        self.result.append(["CNN", 'RMSprop', lr, epoch, batch, history.history['accuracy'][-1] ,score[1]])
        
    def excel_result(self):
        result = pd.DataFrame(self.result, columns=['Model','Optimizer','lr','epoch','batch','train_acc','test_acc'])
        result.to_csv('result.csv', index=False)
    
if __name__ == '__main__':
    file_name = 'C:/Users/dldls/바탕 화면/Coding/신진연구-ATP테니스/ATP_ML.csv'
    feature = 18
    test_rate = 0.3
    lrs = [i*0.000005 for i in range(1,11)]
    epochs = [i*50 for i in range(1,7)]
    batchs = [i*500 for i in range(1,11)]
    
    model = Model()
    model.load_data(file_name, feature, test_rate)
    
    for a in lrs:
        for b in epochs:
            for c in batchs:                
                model.Model_CNN(a,b,c)
                model.Model_DNN(a,b,c)
    
    model.print_result()
    model.excel_result()