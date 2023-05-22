
from funkcija_5_1 import generate_data
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

scores = []
X=generate_data(500,1)
plt.plot(X[:,0],X[:,1],'*',color='blue')
plt.show()

boje = ['purple','red','cyan']

kmeans = KMeans(n_clusters=3,n_init="auto")
label = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_
for i in label:
    plt.scatter(X[label == i,0],X[label == i,1],label = i, color = boje[i])
plt.scatter(centroids[:,0],centroids[:,1],s = 30, color = 'black')
plt.show() 

for i in range(1, 21):
    kmeans = KMeans(n_clusters=i, random_state=42).fit(X)
    score = kmeans.score(X)
    scores.append(abs(score))

plt.plot(range(1, 21), scores, marker='o')
plt.xlabel('Broj klastera')
plt.ylabel('Vrijednost kriterijske funkcije')
plt.show()

link = linkage(X, method='ward')

plt.figure(figsize=(10, 5))
dendrogram(link,truncate_mode="level", p=3)
plt.show()

# Generiraju se drugacije tockice svaki puta kada pokrenemo program
# Mijenja se način grupiranja nasumičnih podataka 
# Lakat metoda - optimalan broj klastera (3)
