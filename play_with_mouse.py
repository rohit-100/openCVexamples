import cv2 as cv
import  numpy as np


drawing = False # if true if mouse if pressed
ix,iy = 2,2
mode = True # if True then rectangle ,if False then circle
def event_of_mouse(event,x,y,flags,pram):

    global  drawing , ix,iy,mode
    if event == cv.EVENT_LBUTTONDOWN:
        ix = x
        iy = y
        drawing = True
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
            else:
                cv.circle(img,(x,y),10,(0,0,255),2)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        else:
            cv.circle(img, (x, y), 10, (0, 0, 255), 2)

img = np.zeros((512,512,3),np.uint8)
cv.namedWindow('image',cv.WINDOW_NORMAL)
cv.setMouseCallback('image',event_of_mouse)


while (1):
    cv.imshow('image',img)
    k = cv.waitKey(1000) & 0xff
    if k == ord('m'):
        mode = not mode
    if k == ord('q'):
        break

cv.destroyAllWindows()

