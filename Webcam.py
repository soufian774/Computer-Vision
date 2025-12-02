import cv2
from datetime import datetime

bg_mode = False
dt_mode = False

GREEN = (0,255,0)

cap = cv2.VideoCapture(0)   #Passo 0 per collegarmi alla WebCam principale

#ret, frame = cap.read()     #ret contiene True o False, cioè se la camera funziona o meno

if(not(cap.isOpened())):
    print("Webcam non disponibile")
    exit(0)
    
#Singolo Frame
#cv2.imshow("frame", frame)


#Stream Frame

while(cap.isOpened()):
    ret, frame = cap.read()     #ret contiene True o False, cioè se la camera funziona o meno
    
    if(bg_mode):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if(dt_mode):
        point = (frame.shape[1] - 160, frame.shape[0] - 5)
        now = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        cv2.putText(frame, now, point, cv2.FONT_HERSHEY_PLAIN, 1, GREEN, 2)
    
    
    cv2.imshow("Webcam", frame)
    k = cv2.waitKey(1)
    
    
    if(k==ord("b")):
        bg_mode = not(bg_mode)
        print("Modalità B/N")
    elif(k == ord("t")):
        dt_mode = not(dt_mode)
        print("Mostra data e ora")
    elif(k == 27):                #ESC
        break

cap.release()                   #Rilasciamo la WebCam
cv2.destroyAllWindows()         #Assicuriamoci che tutte le finestre vengano chiuse