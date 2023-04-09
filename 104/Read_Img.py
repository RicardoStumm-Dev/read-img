import cv2

img1 = cv2.imread("poster.jpg")
rocket = img1[120:360, 400:500]
img1[0:240, 500:600] = rocket
text_show = "Estrelas"
cv2.putText(img1, text_show, (20,220), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color = (0,0,255))
cv2.imshow("poster", img1)

cv2.waitKey(0)