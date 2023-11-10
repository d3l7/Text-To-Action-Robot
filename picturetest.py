import cv2, datetime, time

videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    for i in range(2):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite(f"NewPicture{i}.jpg",frame)
        print(datetime.datetime.now())
        result = False
        time.sleep(5)
        
videoCaptureObject.release()
cv2.destroyAllWindows()