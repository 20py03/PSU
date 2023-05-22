import numpy as np
from tensorflow import keras
from tensorflow.python.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix,accuracy_score
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense,Conv2D,MaxPooling2D,Flatten
import tensorflow as tf
import seaborn as sns

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: prikazi nekoliko slika iz train skupa
fig=plt.figure(figsize=(8,8))
for i in range (1,3*3+1):
    fig.add_subplot(3,3,i)
    first_image=x_train[i]
    first_image=np.array(first_image,dtype='float')
    pixels=first_image.reshape(28,28)
    plt.imshow(pixels,cmap='gray')
plt.show()

# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)


# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu
model = Sequential()
model.add(Conv2D(28,kernel_size=(3,3),activation='relu',input_shape=(28,28,1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=num_classes, activation='softmax'))      

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])

# TODO: provedi ucenje mreze
model.fit(x_train_s, y_train_s, epochs=5, batch_size=32)


# TODO: Prikazi test accuracy i matricu zabune
metrics = model.evaluate(x_test_s,y_test_s,verbose=2)

print("Loss:",metrics[0])
print("Accuracy:",metrics[1])

y_predicted = model.predict(x_test_s)
y_predicted_labels = [np.argmax(i) for i in y_predicted]
cm = tf.math.confusion_matrix(labels=y_test, predictions=y_predicted_labels)
plt.figure(figsize = (10,7))
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()

# TODO: spremi model
model.save('model.h5')


