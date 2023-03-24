import cv2

camera = cv2.VideoCapture(1)


while True:

    _,frame = camera.read()
    # frame = cv2.rectangle(frame,(20,20),(100,100),(0,255,0),10)
    # frame = cv2.circle(frame,(300,300),(100),(0,0,255),20)
    cv2.imshow("Window",frame)

    if cv2.waitKey(1) != -1:
        break

cv2.destroyAllWindows()