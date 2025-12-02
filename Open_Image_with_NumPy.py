#Aprire un'immagine con NumPy

import numpy as np
from PIL import Image

img = Image.open("res_lezione1/cat.jpg")  #Viene automatica caricata in formato aRGB

#img = img.convert("L") #Convesione immagine in grayscale (B/N), senza grayscale ogni pixel viene espresso come [R,G,B]

arr = np.array(img)  #In questo modo otteniamo la matrice numerica dell'immagine

print(arr[:,:,0]) #Abbiamo ottenuto la matrice del primo canale (Rosso)

print(arr.shape)