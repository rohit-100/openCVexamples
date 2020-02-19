import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,10000)
cap.set(4,100000)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    res,frame = cap.read()

    if res is True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + 'Height: ' + str(cap.get(4))
        frame = cv2.putText(frame,text,(10,50),font,0.75,(255,255,255),2)
        cv2.imshow('frame' , frame)

        if cv2.waitKey(50) & 0xff == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


