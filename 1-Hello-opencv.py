import cv2

image = cv2.imread("assets/sharingan.png",1)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
