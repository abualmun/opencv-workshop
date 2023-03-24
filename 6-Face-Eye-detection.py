import cv2

camera = cv2.VideoCapture(1)

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    _,frame = camera.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 9)
    for (ex,ey,ew,eh) in eyes:
        mask = cv2.imread("assets/sharingan.png",1)
        mask = cv2.resize(mask, (ew,eh))
        try:
            frame[ey:ey+eh,ex:ex+ew] = mask
        except:
            continue

    cv2.imshow("Window",frame)
    if cv2.waitKey(1) != -1:
        break

cv2.destroyAllWindows()