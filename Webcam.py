import cv2
from datetime import datetime

bg_mode = False
dt_mode = False
save = False
rec = False

GREEN = (0,255,0)

cap = cv2.VideoCapture(0)   #Passo 0 per collegarmi alla WebCam principale
codec = cv2.VideoWriter_fourcc(*"MJPG")
out = cv2.VideoWriter('output.avi', codec, 30, (640,480))

face_cascade = cv2.CascadeClassifier("face_detection/haarcascade_frontalface_default.xml")
smile_casdade = cv2.CascadeClassifier("face_detection/haarcascade_smile.xml")

#ret, frame = cap.read()     #ret contiene True o False, cioè se la camera funziona o meno

if(not(cap.isOpened())):
    print("Webcam non disponibile")
    exit(0)
    
#Singolo Frame
#cv2.imshow("frame", frame)


#Stream Frame

while(cap.isOpened()):
    ret, frame = cap.read()     #ret contiene True o False, cioè se la camera funziona o meno
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if(bg_mode):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if(dt_mode):
        point = (frame.shape[1] - 160, frame.shape[0] - 5)
        now = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        cv2.putText(frame, now, point, cv2.FONT_HERSHEY_PLAIN, 1, GREEN, 2)
    if(save):
        now = datetime.now().strftime("%d_%m_%y %H_%M_%S")
        cv2.imwrite(f"img_{now}.jpg", frame)
        print("Salvato")
        save = not(save)
    if(rec): 
        cv2.circle(frame, (frame.shape[1] - 20, 20), 8, (0,0,255), cv2.FILLED)
        out.write(frame)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (xf,yf,wf,hf) in faces:
        cv2.rectangle(frame, (xf,yf), (xf+wf, yf+hf), (255,0,0), 3)
        cropped = frame[yf:(yf+hf),xf:(xf+wf)]
        smiles = smile_casdade.detectMultiScale(cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY), 1.5, 20)
        for (xs,ys,ws,hs) in smiles:
            cv2.rectangle(frame, (xf+xs,yf+ys), (xf+xs+ws, yf+ys+hs), (255,0,0), 3)
            cv2.imwrite("smile.jpg", cropped)
        
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
    elif(k == ord("s")):
        save = not(save)
    elif(k ==ord("r")):
        rec = not(rec)
        

if(out != None):
    out.release()

cap.release()                   #Rilasciamo la WebCam
cv2.destroyAllWindows()         #Assicuriamoci che tutte le finestre vengano chiuse