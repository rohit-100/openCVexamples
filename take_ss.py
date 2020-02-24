'''

THIS CODE IS NOT WORKING
I WANT TO SAVE THE FRAME WHEN CERTAIN TIME PASSES

'''







import cv2 as cv
import numpy as np
import os
fps = 35
images_path = '/home/rohit/PycharmProjects/images/'
vidios_path = '/home/rohit/PycharmProjects/vidios/'
ss_path = '/home/rohit/PycharmProjects/ss/'


def show_image(image, delay):
    delay = delay * 1000
    delay = int(delay)
    cv.namedWindow('image', cv.WINDOW_NORMAL)
    cv.imshow('image', image)
    cv.waitKey(delay)


player = cv.VideoCapture(vidios_path + 'sample.mp4')

if not player.isOpened():
    print("vidio is not loaded ")
    exit(0)
cv.namedWindow('vidio',cv.WINDOW_NORMAL)
period = 50
frames = 0
os.chdir(ss_path)
print(os.path.abspath(os.getcwd()))
while 1:
    ret,frame = player.read()
    if ret is False:
        print("failed to capture the frame")
        break
    # show_image(frame,0.001)
    period -= 1
    if period == 0:
        print("now")
        # print(frame)
        # cv.imwrite(str(frame)+'.jpg',frame)
        frames += 1
        period = 50

    cv.imshow('vidio',frame)
    if cv.waitKey(fps) & 0xff == ord('q'):
        print(frames)
        break

# messi = cv.imread(images_path + 'messi5.jpg')
# cv.imwrite(str(frames)+'.jpg',messi)
player.release()
cv.destroyAllWindows()


