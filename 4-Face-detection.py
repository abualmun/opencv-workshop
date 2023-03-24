import cv2

camera = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    _,frame = camera.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 9)

    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),5)
    cv2.imshow("Window",frame)

    
    if cv2.waitKey(1) != -1:
        break
cv2.destroyAllWindows()