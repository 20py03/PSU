import numpy as np
from sklearn.datasets import fetch_openml
import joblib
import pickle
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import seaborn as sn


X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)


# TODO: prikazi nekoliko ulaznih slika

for i in range(9):  
    plt.subplot(330 + 1 + i)
    pixels = X[i].reshape((28, 28))
    plt.imshow(pixels, cmap='gray')

plt.show()

# skaliraj podatke, train/test split
X = X / 255.
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]


# TODO: izgradite vlastitu mrezu pomocu sckitlearn MPLClassifier 

mlp_mnist = MLPClassifier(hidden_layer_sizes=(50,), alpha=1e-4, verbose=10, random_state=1,learning_rate_init=.1, solver='sgd', max_iter=10,activation='logistic')
mlp_mnist.fit(X_train,y_train)

predict_train = mlp_mnist.predict(X_train)
predict_test = mlp_mnist.predict(X_test)

# TODO: evaluirajte izgradenu mrezu

print('Training set score: ', mlp_mnist.score(X_train,y_train).round(3))
print('Test set score: ', mlp_mnist.score(X_test,y_test).round(3))

# spremi mrezu na disk
filename = "NN_model.sav"
joblib.dump(mlp_mnist, filename)

prediction = mlp_mnist.predict(X_test)

cm = metrics.confusion_matrix(y_true=y_test, y_pred=prediction,labels=mlp_mnist.classes_)
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()