from keras.layers import Dense, Flatten
from keras.models import Sequential
import numpy as np
import tensorflow as tf
import keras


model =Sequential() #construindo o modelo
model.add(keras.Input(shape=(28,28)))

model.add(Flatten()) #input layer
model.add(Dense(128, activation='relu'))#hidden layer, goat activation
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.summary()


# model.built= True
model.load_weights('modelo_loko2.h5')

mnist = tf.keras.datasets.mnist #importando uma data set, mnist e tipo um hello world do keras
#imagem feita a mão 28x28 que tem digitos de 0-9


#unpacking
(x_train,y_train), (x_test, y_test) = mnist.load_data()
#scaling it
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_train, axis=1)

input_image = np.expand_dims(x_test[0], axis=0)
prediction = model.predict(input_image)

dict_ = {key: ' eh {}'.format(key) for key in range(0,10) }
local_max = np.argmax(prediction[0])

print(prediction,local_max,dict_[int(local_max)])

