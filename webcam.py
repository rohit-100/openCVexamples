import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow('webcam',cv2.WINDOW_NORMAL)
cv2.resizeWindow('webcam',600,600)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))


while cap.isOpened():

    ret,frame = cap.read()
    newframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    print(cv2.CAP_PROP_FRAME_HEIGHT)
    print(cv2.CAP_PROP_FRAME_WIDTH)
    if ret is True:
        cv2.imshow('webcam',newframe)
        # cv2.imshow('mywebcam',frame)
        out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
out.release()
cv2.destroyAllWindows()