import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Conv2D, MaxPooling2D, Flatten

import pickle
from DatasetLoader import Loader
from sklearn.model_selection import train_test_split
from  keras.callbacks import ModelCheckpoint

#input layer
model = Sequential()
model.add(Conv2D(64, (3, 3), input_shape=(224, 224, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64, activation="relu"))

model.add(Dense(1))
model.add(Activation('sigmoid')) #minimo da função sigmoid e 0 e o maximo e 1

#add layer pra chamar classificador

model.compile(optimizer='adam', #goat optimiser
              loss='binary_crossentropy',
              metrics=['accuracy'])


model.load_weights("modelDogVsCat.h5") #meter o load loucão




#parte do video
cap = cv2.VideoCapture('/home/fernandobellelis/Downloads/Doguinho.mp4') #abrir stream
ret = True #ret começa sempre true.
while ret:
    ret, frame  = cap.read()
    if not  ret: #caso não ele volta e não começa a stream.
        break
    cv2.imshow('frame', frame)
    cv2.waitKey(1)


    # (224, 224, 3)
    pred_img = cv2.resize(frame, (224, 224)) #meter o louco no resize pra ficar no mesmo padrão da rede neural la em cima
    # (1, 224, 224, 3)
    pred_img = np.expand_dims(pred_img, axis=0) #cria o tensor pra rede neural

    #if movimento usar o predict
    resposta_ = model.predict(pred_img)[0][0] #Colocando uma imagem pra checagem
    #print(resposta_) #printa os valores que decidem se e um gato ou um CARROCHO
    print(resposta_)

    if resposta_<0.5:
        print('e um gatito')
    else:
       print('e um CARROCHO')