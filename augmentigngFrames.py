import cv2
import time 

startQuestion = "Enter Key: "
startKey = "AI"

cameraWidth = 640
cameraHeight = 360


topLeftCordinates = (250,140)
lowerRightCordinates = (390,220)
rectangleThickness = 2



circleRadius = 40



textContent = ""
textFont = cv2.FONT_HERSHEY_COMPLEX
textSize = 1
textThickness = 1
startTextX = 25
startTextY = 25
black = (0,0,0)
red = (0,0,255)
white = (255,255,255)


def cameraSizing(width,height):
     camera.set(cv2.CAP_PROP_FRAME_WIDTH,width)
     camera.set(cv2.CAP_PROP_FRAME_HEIGHT,height)


def cameraFps(fps):
     camera.set(cv2.CAP_PROP_FPS,fps)
                           ## lets windows know that the video captures intent is to show allowing for faster performace 





def returnFrame(camera):
      ignore,frame = camera.read()
      return frame

startInput = input(startQuestion)

if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cameraSizing(cameraWidth,cameraHeight)
    cameraFps(30)
    

    loopCounter = 0
    loopTime = 0
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    while True:
      startTime = time.time()   
      frame = returnFrame(camera)
      ##changes frame to add purple rectangle rectangle
      ##frame[140:220,250:390] = (255,000,255)
      #changes frame to add red rectangle
      cv2.rectangle(frame,topLeftCordinates,lowerRightCordinates,red,rectangleThickness)
      cv2.circle(frame,(int(cameraWidth/2),int(cameraHeight/2)),circleRadius,black)
      cv2.putText(frame,textContent,(startTextX,startTextY),textFont,textSize,white,textThickness)
      cv2.imshow("Camera window",frame)
      print(loopCounter)
      endTime = time.time()
      duration = endTime - startTime
      print(duration)
      fps = str(int(1/duration))
      
      textContent = "fps: " + fps      
      if cv2.waitKey(1) == ord("q"):
            break
    camera.release()
