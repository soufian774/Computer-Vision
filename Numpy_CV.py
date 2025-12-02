#Basi di Numpy per Computer Vision
import numpy as np
from PIL import Image

arr = np.array([[1,2,3,4,5],[1,2,3,4,5]]) #Creazione di un semplice Array Numpy (conversione lista python in Numpy)
print(arr.shape) #Vediamo la dimensione dell'array

arr = np.random.randint(0,255,(100,100), dtype=np.uint8)  #Creazione immagine GrayScale (B/N)  0 = NERO 255 = BIANCO

arr[0] = np.zeros(100)
arr[-1] = np.zeros(100)
arr[:,0] = np.zeros(100)
arr[:,-1] = np.zeros(100)  #In questo modo abbiamo circondato l'immagine con un box Nero

np_white = np.ones((20,20), dtype=np.uint8) * 255


x_offset = int(np_white.shape[0]/2)  
y_offset = int(np_white.shape[1]/2)

x_start = int(arr.shape[0] / 2 )- x_offset
y_start = int(arr.shape[1] / 2 )- y_offset

x_end = int(arr.shape[0] / 2 ) + x_offset
y_end = int(arr.shape[1] / 2 ) + y_offset


arr[x_start:x_end, y_start:y_end] = np_white


img = Image.fromarray(arr) #Creiamo l'immagine raffigurata dall'array random Numpy

print(arr)

img.save("test.png")
