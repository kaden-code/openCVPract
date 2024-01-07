## color
## blakc and white
## color 
## black and white 
import cv2
cameraWindowOne = cv2.VideoCapture(0)


startInputAnswer = "start"

startInputQuestion = input("Enter key:")


def returnFrame(camera):
      ignore,frame = camera.read()
      return frame
   

if startInputAnswer == startInputQuestion:
    while True:
      frame = returnFrame(cameraWindowOne)
      blackAndWhiteFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      cv2.imshow("Color Frame", frame)
      cv2.imshow("Grey Frame", blackAndWhiteFrame)
      cv2.imshow("Color Frame2", frame)
      cv2.imshow("Grey Frame2", blackAndWhiteFrame)
      cv2.moveWindow("Color Frame", 0,0)
      cv2.moveWindow("Grey Frame", 0,500)
      cv2.moveWindow("Color Frame2", 500,500)
      cv2.moveWindow("Grey Frame2", 500,0)
      if cv2.waitKey(1) == ord("q"):
         break
      
    cameraWindowOne.release()