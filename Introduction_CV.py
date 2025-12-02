#INTRODUZIONE AD OPENCV
import cv2

print(cv2.__version__) #Otteniamo la versione installata con OpenCV

#Apriamo un'immagine

img = cv2.imread("res_lezione2/elon.jpg", cv2.IMREAD_GRAYSCALE) #Lo carica come un array NumPy codifica aRGB, posso mettere
                                                                #anche il tipo dell'immagine di default passa IMREAD_COLOR
                                                                #con IMREAD_GRAYSCALE diventa B/N

print(type(img)) #np.array

cv2.imshow('image', img) #Mettiamo il titolo con cui vogliamo aprire la finestra e l'array numpy
cv2.waitKey(0)  #in questo modo finchè non premiamo un tasto la finestra non si chiude

img = cv2.imread("res_lezione2/elon.jpg", cv2.IMREAD_COLOR) #Lo carica come un array NumPy codifica aRGB, posso mettere
                                                                #anche il tipo dell'immagine di default passa IMREAD_COLOR
                                                                #con IMREAD_GRAYSCALE diventa B/N

print(type(img)) #np.array

cv2.imshow('imagegr', img) #Mettiamo il titolo con cui vogliamo aprire la finestra e l'array numpy
cv2.waitKey(0)  #in questo modo finchè non premiamo un tasto la finestra non si chiude

cv2.destroyAllWindows() #Siamo sicuri che le finestre vengano tutte chiuse