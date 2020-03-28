import cv2 as cv
import numpy as np
import math
images_path = '/home/rohit/PycharmProjects/images/'


def show_image(image, delay):
    delay = delay * 1000
    cv.namedWindow('image', cv.WINDOW_NORMAL)
    cv.imshow('image', image)
    cv.waitKey(delay)

ppt = []
class process_10_frames:
    def __init__(self,path):
        self.ppts  = []
        self.buffer = []
        self.path = path
        self.cap = cv.VideoCapture(path)
        self.frame1 = None
        self.frame2 = None
        self.diff = None
        self.win1 = 'myvidio'
        self.win2 = 'win2'
        self.width = int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        cv.namedWindow(self.win2,cv.WINDOW_NORMAL)
        cv.namedWindow(self.win1,cv.WINDOW_NORMAL)
        if self.cap.isOpened():
            _ ,self.frame1 = self.cap.read()


    def run(self):
        # print(np.shape(self.frame1))
        self.frame1 = cv.cvtColor(self.frame1, cv.COLOR_BGR2GRAY)
        interval = 80
        counter =interval
        # mask = np.zeros(math.floor(self.width),math.floor(self.height), np.uint8)
        mask = np.zeros((self.height,self.width),dtype=np.uint8)
        self.buffer = []
        while True:
            ret,self.frame2 = self.cap.read()
            if ret is False:
                break
            self.buffer.append(self.frame2)
            # print(self.frame2)
            self.frame2 = cv.cvtColor(self.frame2,cv.COLOR_BGR2GRAY)

            self.diff = cv.absdiff(self.frame1,self.frame2)
            _,thresh = cv.threshold(self.diff,5,255,cv.THRESH_BINARY)
            # thresh_mask = thresh > 6
            # print(thresh_mask)
            mask   = np.bitwise_or(mask,thresh)
            counter-=1
            if counter == 0:
                self.classify(mask)
                self.buffer = []
                counter = interval
                cv.imshow('myimage',mask)
                mask = np.zeros((self.height,self.width),dtype=np.uint8)

            # print(np.shape(self.diff))
            cv.imshow(self.win2,thresh)
            cv.imshow(self.win1,self.frame2)
            if cv.waitKey(1)&0xFF == 27:
                # self.saveppts()
                break
            self.frame1 = self.frame2

    def classify(self,mask):
        # ones = np.count_nonzero(mask)
        ones = np.count_nonzero(mask)
        # print(ones)
        total = self.width * self.height
        zeros = total - ones;
        # print("zeros= {}".format(zeros))
        ppt_chance = (zeros*100)/total
        print(ppt_chance)
        if ppt_chance >= 90.00:
            # print("ppt showing")
            ppt.append(self.buffer[int(len(self.buffer)/2)])
            print(len(ppt))
            # print("ppt not showing")

def saveppts():
    path_for_ss = '/home/rohit/PycharmProjects/ss'
    total = len(ppt)
    for i in range(total):
        cv.imwrite(str(i)+'.jpg',ppt[i])


def filter():
    curr = None
    prev = None
    rest   = 0;
    if(len(ppt)):
        prev = ppt[0]
        prev = cv.cvtColor(prev, cv.COLOR_BGR2GRAY)
    for i in range(1,len(ppt)):

       curr = ppt[i]
       curr = cv.cvtColor(curr,cv.COLOR_BGR2GRAY)
       diff = cv.absdiff(prev,curr)
       _,diff_thresh = cv.threshold(diff,3,255,cv.THRESH_BINARY)
       ones = np.count_nonzero(diff_thresh)
       total = np.shape(diff_thresh)[0]*np.shape(diff_thresh)[1]
       zeros = total - ones
       simi =  (100*zeros)/total
       print("simi = {}".format(simi))
       if simi < 90:
          cv.imwrite(str(i)+'.jpg',ppt[i-1])
          rest += 1
       prev = curr
    print("rest = {}".format(rest))


class detect_contours:
    def __init__(self,path):
        self.path = path
        self.cap = cv.VideoCapture(path)
        self.frame1 = None
        self.frame2 = None
        self.diff = None
        self.win1 = 'myvidio'
        self.win2 = 'win2'
        cv.namedWindow(self.win2,cv.WINDOW_NORMAL)
        cv.namedWindow(self.win1,cv.WINDOW_NORMAL)
        if self.cap.isOpened():
            _ ,self.frame1 = self.cap.read()


    def run(self):
        print(np.shape(self.frame1))
        self.frame1 = cv.cvtColor(self.frame1, cv.COLOR_BGR2GRAY)
        while True:
            _,self.frame2 = self.cap.read()
            # print(self.frame2)
            self.frame2 = cv.cvtColor(self.frame2,cv.COLOR_BGR2GRAY)

            self.diff = cv.absdiff(self.frame1,self.frame2)
            _,thresh = cv.threshold(self.diff,5,255,cv.THRESH_BINARY)
            # print(np.shape(self.diff))
            cv.imshow(self.win2,thresh)
            cv.imshow(self.win1,self.frame2)
            if cv.waitKey(10)&0xFF == 27:
                break
            self.frame1 = self.frame2


def main():
    path = '/home/rohit/PycharmProjects/vidios/lecture3.mp4'
    # worker = detect_contours(path)
    # worker.run()
    worker = process_10_frames(path)
    worker.run()
    print(len(ppt))
    # saveppts()
    filter()
    cv.destroyAllWindows()

main()
