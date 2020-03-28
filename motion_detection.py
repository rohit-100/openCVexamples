import cv2 as cv
import numpy as np
import time


images_path = '/home/rohit/PycharmProjects/images/'


def show_image(image, delay):
    delay = delay * 1000
    cv.namedWindow('image', cv.WINDOW_NORMAL)
    cv.imshow('image', image)
    cv.waitKey(delay)

class motiondetection:
    def __init__(self,frame11,frame22):
        self.frame1 = frame11
        self.frame2 = frame22
        self.n = 320
        self.m = 240

        self.diff = np.zeros((self.n,self.m),np.uint8)
        self.res = None


    def resizing(self):
        self.frame1 = cv.resize(self.frame1, (self.n, self.m))
        self.frame2 = cv.resize(self.frame2, (self.n,self.m))

    def printsize(self):
        print(self.frame1.shape)
        print(self.frame2.shape)

    def takediff(self):
        self.diff  = cv.absdiff(self.frame1,self.frame2)
        _ , self.diff = cv.threshold(self.diff,20,255,cv.THRESH_BINARY)
        # print(self.frame1)
        # print(self.frame2)
        # print(np.any(self.diff))
    def percentage_similiar(self):
        n,m = self.diff.shape
        total_pixles = n*m
        mask = self.diff < 5
        black_pixles = np.count_nonzero(mask)
        return (black_pixles*100)/total_pixles

def is_same(img1,img2):
    l,b,h = img1.shape
    for i in range(l):
        for j in range(b):
            for k in range(h):
                if img1[i][j][k] != img2[i][j][k]:
                    print(str(i)+" "+str(j)+" "+str(k))


    return True
def main():
    print("hello")
    img1 = cv.imread(images_path+'ss16.png',cv.IMREAD_GRAYSCALE)
    img2 = cv.imread(images_path+'ss17.png',cv.IMREAD_GRAYSCALE)

    # print(is_same(img1,img2))
    # cv.namedWindow('images',cv.WINDOW_NORMAL)
    # cv.imshow('images',img2)
    # cv.waitKey(5000)
    motiondetector = motiondetection(img1,img2)
    # motiondetector.resizing()
    # motiondetector.printsize()
    motiondetector.takediff()
    print(motiondetector.diff)
    print(motiondetector.percentage_similiar())
    cv.namedWindow('images',cv.WINDOW_NORMAL)
    cv.imshow('images',motiondetector.diff)
    cv.waitKey(100000)
    # print(motiondetector.diff)
    # show_image(motiondetector.diff,5)
    # show_image(img2,5)
    # motiondetector.diff[0][0][0] = 10
    # print(np.any(motiondetector.diff))

    cv.destroyAllWindows()


main()

