import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster

image = mpimg.imread('example_grayscale.png')
clusters = 10

X = image.reshape((-1, 1))
k_means = cluster.KMeans(n_clusters=clusters,n_init=1)
k_means.fit(X) 

values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_
image_compressed = np.choose(labels, values)
image_compressed.shape = image.shape

plt.figure(1)
plt.imshow(image,  cmap='gray')
plt.show()

plt.figure(2)
plt.imshow(image_compressed,  cmap='gray')
plt.show()

# Slika je postala tamnija 
# Manje klastera - veća kompresija (gubi se informacija sa slike)
