import  cv2 as cv
import  numpy as np
images_path = '/home/rohit/PycharmProjects/images/'

def show_image(image,delay):
    delay  = delay*1000
    cv.namedWindow('image',cv.WINDOW_NORMAL)
    cv.imshow('image',image)
    cv.waitKey(delay)



messi = cv.imread(images_path+'messi5.jpg')
logo = cv.imread(images_path + 'logo.png')
messi = cv.resize(messi,(512,512))
logo = cv.resize(logo,(512,512))
dest = cv.addWeighted(messi,0.3,logo,0.7,10)

show_image(dest,2)
cv.destroyAllWindows()










