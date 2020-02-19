import cv2
import  numpy as np
def mouse_event_capture(event ,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' ',y)


img = np.zeros((250,250,3),np.uint8)
cv2.imshow('image',img)
# print(img)
cv2.setMouseCallback('image',mouse_event_capture)
cv2.waitKey(0)
cv2.destroyAllWindows()
