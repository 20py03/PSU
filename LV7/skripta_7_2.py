from keras.models import load_model
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np

filename = 'test.png'

img = mpimg.imread(filename)
img = color.rgb2gray(img)
img = resize(img, (28, 28))


plt.figure()
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()


img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')


# TODO: ucitaj model
model=load_model('model.h5')
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

# TODO: napravi predikciju 
result=model.predict(img)

# TODO: ispis rezultat
print("------------------------")
print(np.argmax(result))




