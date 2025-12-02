#Disegnare Rettangoli, cerchi e linee

import cv2 
print(cv2.__file__)

TICKNESS = -1
RED = (0,0,255)     #OPENCV IN FORMATO BGR
BLUE = (255,0,0)
GREEN = (0,255,0)

img = cv2.imread("res_lezione2/elon.jpg")

cv2.imshow("window", img)

cv2.waitKey(0)

#Disegniamo un quatopdrato

img_h, img_w = img.shape[0], img.shape[1]

l = 200

center = (img_w//2, img_h//2)

#Con OpenCV per disegnare appunto il rettangolo devo dare le coordinate del vertice in alto a sinistra e in basso a destra
cv2.rectangle(img, (center[0]-l// 2, center[1]-l//2), (center[0]+l//2, center[1]+l//2), RED, TICKNESS)
cv2.imshow("window",img)
cv2.waitKey(0)

#Cerchio

r = 50
cv2.circle(img, center, r, BLUE, TICKNESS)

cv2.imshow("window",img)


cv2.waitKey(0)
#Linee

cv2.line(img, (center[0],0), (center[0], img_h), GREEN, 10)
cv2.imshow("window",img)
cv2.waitKey(0)

cv2.line(img, (0, center[1]), (img_w, center[1]), GREEN, 10)
cv2.imshow("window",img)
cv2.waitKey(0)

#Scrivere testo al di sopra delle immagini

cv2.putText(img, "@Soufian Markouni", (0, img_h - 120), cv2.FONT_HERSHEY_PLAIN, 2, RED, 2)
cv2.imshow("window",img)
cv2.waitKey(0)


cv2.destroyAllWindows()