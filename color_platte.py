import cv2 as cv
import  numpy as np

def nothing(x):
    pass

img = np.zeros((512,512,3),np.uint8)
cv.namedWindow('image',cv.WINDOW_NORMAL)

cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)

cv.createTrackbar('switch','image',0,1,nothing)


while (1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xff
    if k == ord('q'):
        break
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    switch = cv.getTrackbarPos('switch','image')

    if switch == 1:
        img[:] = [b,g,r]
        text = str(b) + ' ' + str(g) + ' ' + str(r)
        cv.putText(img,text,(150,150),cv.FONT_HERSHEY_SIMPLEX,3,(255,0,252),2)
    else:
        img[:] = 0

cv.destroyAllWindows()
