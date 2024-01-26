import cv2
import numpy as np
startQuestion = "Password: "
startPass = "A!"
displaySquare = 720
userAnswer = None 
pixelEncoding = 3
blue = (255,0,0)


bgrDisplayWindow = "bgr color"

def makeColorHSV():
    frame = np.zeros([displaySquare,displaySquare,pixelEncoding], dtype = np.uint8)
   ## cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    frame[:,:] = blue 
    return frame

userAnswer = input(startQuestion)
if userAnswer == startPass:
    cv2.namedWindow(bgrDisplayWindow)

    while True:
      frame = makeColorHSV()
      cv2.imshow(bgrDisplayWindow, frame)

      if cv2.waitKey(1) == ord("k"):
         break