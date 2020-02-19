import cv2 as cv
print(cv.__version__)

img = cv.imread('myimage.jpeg',1)
if img is None:
    print("no image")
cv.imshow('myimage',img)
cv.waitKey(0)
cv.destroyAllWindows()

