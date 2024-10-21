

# --------------------------------------------

import cv2

video = cv2.VideoCapture(r'E:\computer vision\video\56310-479197605.mp4')

counter = 0
while video.isOpened():
        r,frame = video.read()
        if r == True:
            frame = cv2.resize(frame, (1000,600))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            car = cv2.CascadeClassifier(r'E:\computer vision\vehicle_detection_video57\cars.xml')
            detect = car.detectMultiScale(gray, 2.2,3)  
          #   counter = counter + 1
          #   print(counter)

            for (x,y,w,h) in detect:
                 cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0), 3)


            cv2.imshow('orignal', frame)
         
            if cv2.waitKey(25) & 0xff == ord('p'):
                break
        else:
             break
            


video.release()

cv2.destroyAllWindows()
