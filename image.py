import os
import cv2

img = cv2.imread("img.jpg")
cv2.imshow("display_img", img)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("grayscale_img", gray_img)
cv2.waitKey(0)
print(gray_img)