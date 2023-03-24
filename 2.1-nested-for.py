import cv2

image = cv2.imread("assets/EEESE.png",1)


for i in range(50,300):
    for j in range(50,300):
        image[i][j] = [255,0,0]

cv2.imshow("window",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
