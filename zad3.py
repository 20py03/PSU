import numpy as np
import matplotlib.pyplot as plt
 
img=plt.imread('tiger.png')
img=img[:,:,0].copy()
 
brightness=img+0.7
brightness[brightness > 1] = 1
plt.figure()
plt.imshow(brightness,cmap='gray')
plt.show()
 
 
rotated=np.rot90(img,3)
plt.figure()
plt.imshow(rotated,cmap='gray')
plt.show()
 
 
mirror=np.fliplr(img)
plt.figure()
plt.imshow(mirror,cmap='gray')
plt.show()
 
 
res=img[::10,::10]
plt.figure()
plt.imshow(res,cmap='gray')
plt.show()
 
 
height,width=img.shape
new=np.zeros((height,width),dtype=np.float32)
width2=int(width/4)
new[:,:width2]=img[:,width2:2*width2]
plt.figure()
plt.imshow(new,cmap='gray')
plt.show()



