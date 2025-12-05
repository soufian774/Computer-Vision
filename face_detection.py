import cv2

webcam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("face_detection/haarcascade_frontalface_default.xml") #Il cascade classifier funziona su immagini in B/N


while(webcam.isOpened()):
    ret, img = webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) #restituisce (x,y,w,h)

    print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x + w, y+h), (255,0,0), 3)


    cv2.imshow("face", img)

    k = cv2.waitKey(1)
    if(k == 27):
        break
    
webcam.release()
cv2.destroyAllWindows()