import cv2

myCam = cv2.VideoCapture(0) ## creates camera object on a specific camera. Camera zero is the built in web cam



## Creates infinite loop 
while True:
    ##firstParam we ignore second is the frame returned from readin the camera
    ignore,frame = myCam.read()
    ## creates new frame variable called grey frame which is eqaul to a method called on cvt called convert color whcih takes the frame just captured and the color to conevrt as a parameter and returns a new fraame with that color 
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ##imageShow
    cv2.imshow("My webcam",frame)
    cv2.imshow("Kaden's Grey webcam",grayFrame)
     ## dictates where window is 
    ##cv2.moveWindow("My webcam",0,1) 
    ## waits 1 milisecond for ordnates of the key key
    if cv2.waitKey(1) == ord('q'):
        break
## relases camera
myCam.release()    

