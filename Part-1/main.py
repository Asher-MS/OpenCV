import cv2

img=cv2.imread("images\cat1.jpg")
new_image=cv2.resize(img,(500,500))
cv2.imshow("CAT",new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
