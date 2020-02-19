import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow('mycapture',cv2.WINDOW_NORMAL)
import datetime
print(cam.isOpened())
while cam.isOpened():
    ret,frame = cam.read()
    if ret is True:
        now = datetime.datetime.now()
        frame = cv2.putText(frame,str(now),(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2);
        cv2.imshow('mycapture',frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
cv2.destroyAllWindows()
cam.release()