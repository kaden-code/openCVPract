import cv2
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
startQuestion = "Enter key:"
key = "A!"
cameraWidth = 530
cameraHeight = 300

startInput = input(startQuestion)

def returnFrame(camera):
    ignore,frame = camera.read()
    return frame

def cameraSizing(width,height):
     camera.set(cv2.CAP_PROP_FRAME_WIDTH,width)
     camera.set(cv2.CAP_PROP_FRAME_HEIGHT,height)



def cameraFps(fps):
     camera.set(cv2.CAP_PROP_FPS,fps)





cameraWindows = [1,2,3,4,5,6]
windowY = 400

def multiWindows(frame):
  windowX = -530
  windowXB = windowX
  for i in cameraWindows:
        windowName = str(cameraWindows[i-1])
        if i <= 3:
          cv2.imshow(windowName,frame)
          windowX = windowX + cameraWidth
          print(windowX)
          print(windowName)
          cv2.moveWindow(windowName, windowX,0)
        
        if i > 3:
          cv2.imshow(windowName,frame)
          windowXB = windowXB + cameraWidth
          print(windowXB)
          print(windowName)
          cv2.moveWindow(windowName,windowXB,windowY)
           
              

       
        
     

cameraFps(30)
cameraSizing(cameraWidth,cameraHeight)





if startInput == key:
    while True:
      frame = returnFrame(camera)
      multiWindows(frame)
      if cv2.waitKey(1) == ord("q"):
        break

