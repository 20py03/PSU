from tensorflow.keras.preprocessing import image_dataset_from_directory
from keras.layers import Input, Conv2D, MaxPooling2D , Dropout, Flatten, Dense
from keras.models import Sequential
import numpy as np
from tensorflow import keras
from tensorflow.python.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix,accuracy_score
import tensorflow as tf
import seaborn as sns

# ucitavanje podataka iz odredenog direktorija
train_ds = image_dataset_from_directory(
    directory='Train',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48))


test_ds = image_dataset_from_directory(
    directory='Test_dir',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48))


maska = (48,48,3)
input = Input(maska)
model = Sequential()
model.add(Conv2D(filters=32,kernel_size=(3,3),activation='relu'))
model.add(Conv2D(filters=32,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Dropout(0.2))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Dropout(0.2))
model.add(Conv2D(128,(3,3),activation='relu'))
model.add(Conv2D(128,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(512,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(43,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(train_ds, epochs=5, batch_size=32)
print(model.evaluate(test_ds))


metrics = model.evaluate(test_ds)

print("Loss:",metrics[0])
print("Accuracy:",metrics[1])

y_predicted = model.predict(test_ds)
y_predicted = np.argmax(y_predicted, axis=1)

y_true = []
for image_batch, label_batch in test_ds.unbatch():
   y_true.append(label_batch)

y_true = np.argmax(y_true, axis=1)
print(y_predicted)
print(y_true)

cm = confusion_matrix(y_true, y_predicted)
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel("Predicted")
plt.ylabel("Truth")
plt.show()