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


player = cv.VideoCapture(vidios_path + 'myvideo.mp4')

if not player.isOpened():
    print("vidio is not loaded ")
    exit(0)
cv.namedWindow('vidio',cv.WINDOW_NORMAL)
period = 5
frames = 0
os.chdir(ss_path)
print(os.path.abspath(os.getcwd()))
frame_count = 0
frames = []
while 1:
    ret,frame = player.read()
    if ret is False:
        print("failed to capture the frame")
        break
    frame_count+=1
    period -= 1
    if period == 0:
        # black_image = np.zeros((255,255,3),np.uint8)

        # cv.imwrite(str(frame)+'.jpg',black_image)
        # cv.namedWindow('new_win',cv.WINDOW_NORMAL)
        # cv.imshow('new_win',frame)
        print(frame_count)
        frames.append(frame)
        period = 5

    cv.imshow('vidio',frame)
    if cv.waitKey(fps) & 0xff == ord('q'):
        break

# messi = cv.imread(images_path + 'messi5.jpg')
# cv.imwrite(str(frames)+'.jpg',messi)
print(len(frames))
name = 1
for frame in frames:
    cv.imwrite(str(name)+'.jpg',frame)
    name += 1

player.release()
cv.destroyAllWindows()


