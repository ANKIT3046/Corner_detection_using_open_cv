import cv2
import numpy as np

img=cv2.imread('image/box2.jpg')
cv2.imshow('original image',img)
cv2.waitKey()

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


corners=cv2.goodFeaturesToTrack(gray,50,0.01,10)
print(len(corners))

for corner in corners:
    x,y=corner[0]
    x=int(x)
    y=int(y)
    cv2.rectangle(img,(x-5,y-5),(x+5,y+5),(0,255,0),2)

cv2.imshow('corner found ',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
