import cv2

camera = cv2.VideoCapture(1)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret,frame = camera.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(gray,scaleFactor = 1.08,minNeighbors = 9)

    for (ex,ey,ew,eh) in eyes:
        frame = cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,0,0),5)

    cv2.imshow("Window",frame)
    if cv2.waitKey(1) == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()