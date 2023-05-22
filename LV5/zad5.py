import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster

image = mpimg.imread('example.png')
(h,w,c) = image.shape

clusters = 3

img2D = image.reshape(h*w,c)

kmeans_model = cluster.KMeans(n_clusters=clusters)
cluster_labels = kmeans_model.fit_predict(img2D)

rgb_cols = kmeans_model.cluster_centers_
img_quant = np.reshape(rgb_cols[cluster_labels],(h,w,rgb_cols.shape[1]))

fig = plt.figure(figsize=(10, 7))

fig.add_subplot(1, 2, 1)
  
plt.imshow(image)
plt.axis('off')
plt.title("Original")
  
fig.add_subplot(1,2, 2)

plt.imshow(img_quant)
plt.axis('off')
plt.title("Kvantizirana")
plt.show()

