import cv2
import numpy as np
img = cv2.imread('myimage.jpeg')

b,g,r = cv2.split(img)
# print(b)
# print(g)
# print(r)
B,G,R = [img[:,:,x] for x in range(3)]
# print(B)
if np.array_equal(b,B):
    print('yes\n')
else:
    print('no\n')

