import  cv2
import numpy as np
img = cv2.imread('myimage.jpeg',1)

img = cv2.line(img,(0,1),(22,330),(255,255,0),10)

cv2.imshow('myimage',img)
cv2.waitKey()
cv2.destroyAllWindows()
