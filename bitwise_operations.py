import cv2 as cv
import numpy as np

images_path = '/home/rohit/PycharmProjects/images/'
window_name = 'image'
cv.namedWindow(window_name,cv.WINDOW_NORMAL)

def show_image(image, delay):
    delay = delay * 1000
    delay = int(delay)
    cv.imshow(window_name, image)
    cv.waitKey(delay)


def resize_row_and_col(rows,cols):
    rows //= 10
    cols //= 10
    return (rows,cols)


def make_equal_size(image1,image2):
    shape1 = image1.shape
    shape2 = image2.shape
    if shape1[0] > shape2[0]:
        image1 = cv.resize(image1,image2.shape[:2])
    elif shape1[0] == shape2[0]:
        if shape1[1] > shape2[1]:
            image1 = cv.resize(image1,image2.shape[:2])
        else:
            image2 = cv.resize(image2,image1.shape[:2])
    else:
        cv.resize(image2,image1.shape[:2])
    print(image1.shape)
    print(image2.shape)

def insert_logo():
        messi = cv.imread(images_path + 'messi5.jpg')
        logo = cv.imread(images_path+'logo.png')

        logo = cv.resize(logo,(200,130))



        print(logo.shape)
        print(messi.shape)

        rows ,cols,channels = logo.shape
        roi = messi[0:rows,0:cols]
        logo_gray = cv.cvtColor(logo,cv.COLOR_BGR2GRAY)

        _,mask = cv.threshold(logo_gray,10,255,cv.THRESH_BINARY)


        mask_inv = cv.bitwise_not(mask)

        roi_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
        logo_fg = cv.bitwise_and(logo,logo,mask = mask)


        dst = cv.add(roi,logo_fg)
        messi[0:rows,0:cols] = dst
        show_image(messi,500)




def make_animation():
    messi = cv.imread(images_path+'messi5.jpg')
    logo = cv.imread(images_path + 'logo.png')
    print(messi.shape)
    print(logo.shape)

    make_equal_size(messi,logo)
    print(messi.shape)
    print(logo.shape)


# insert_logo()
make_animation()
cv.destroyAllWindows()

