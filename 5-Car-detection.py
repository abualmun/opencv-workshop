
import cv2


car_cascade = cv2.CascadeClassifier("cars.xml")

frame = cv2.imread("assets/cars.png",1)
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray, 1.05, 4)

for (x,y,w,h) in cars:
    frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)

cv2.imshow("Window",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()