import numpy as np
import matplotlib.pyplot as plt
 
def create(size, height, width):
    black = np.zeros((size, size), dtype=np.uint8)
    white = np.ones((size, size), dtype=np.uint8) * 255
 
    img = np.zeros((size * height, size * width), dtype=np.uint8)
 
    for i in range(height):
        for j in range(width):
            if (i + j) % 2 == 0:
                img[i * size:(i+1) * size, j * size:(j+1) * size] = white
            else:
                img[i * size:(i+1) * size, j * size:(j+1) * size] = black
 
 
    return img
 
img=create(50,4,5)
plt.figure()
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()    