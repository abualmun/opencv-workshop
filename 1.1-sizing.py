import cv2

image = cv2.imread("assets/EEESE.png",1)

# image.shape = [x,y,p]


image = cv2.resize(image,(100,400))
print(image.shape)
cv2.imshow("Image",image)
cv2.imwrite("assets/new_logo.png",image)

cv2.waitKey(0)
cv2.destroyAllWindows()