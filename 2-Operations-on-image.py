import cv2

image = cv2.imread("assets/Boss.png")

crop = image[40:140,30:330]

print(crop.shape)

# crop = cv2.rotate(crop,cv2.ROTATE_90_CLOCKWISE)
image[200:300,300:600] = crop


cv2.imshow("window",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
