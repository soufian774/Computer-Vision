#Ridimensionare e ritagliare un'immagine con OpenCV

import cv2

img = cv2.imread("res_lezione2/elon.jpg")

cv2.imshow("image", img)

cv2.waitKey(0)

print(img.shape) #Dimensione originale = 960x1280

# Ridimensionamento immagine

img_h, img_w = 550,400

img_resized = cv2.resize(img, (img_w, img_h))  #Passo l'array con l'immagine ed una tupla con i nuovi valori del resize

cv2.imshow("image_resized", img_resized)

cv2.waitKey(0)

#Ritagliare immagine, si puà fare direttamente con slicing con NumPy

size = 200

print(img_resized.shape)

img_cropped = img_resized[img_h//2 - size//2:img_h//2 + size//2,
                          img_w // 2 -size//2: img_w // 2 + size // 2]

cv2.imshow("img_cropped", img_cropped)

cv2.waitKey(0)


#Ruotare un'immagine

angle = 180
center = (img_w/2, img_h/2)

#Dobbiamo creare una matrice di rotazione

rot_mat = cv2.getRotationMatrix2D(center, angle, 1.)

img_rotated = cv2.warpAffine(img_resized, rot_mat, (img_w, img_h))

cv2.imshow("img_rotate", img_rotated)

cv2.waitKey(0)

cv2.imwrite("res_lezione4/img_resized.jpg", img_resized) #ridimensionata
cv2.imwrite("res_lezione4/img_cropped.jpg", img_cropped) #tagliata
cv2.imwrite("res_lezione4/img_rotated.jpg", img_rotated) #ruotata


cv2.destroyAllWindows()