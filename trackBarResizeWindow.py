import cv2

startQuestion = "Enter Key: "
startKey = "AI"

cameraWidth = 1280
cameraHeight = 720

def cameraSizing(width,height):
     camera.set(cv2.CAP_PROP_FRAME_WIDTH,width)
     camera.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

def cameraFps(fps):
     camera.set(cv2.CAP_PROP_FPS,fps)
                           ## lets windows know that the video captures intent is to show allowing for faster performace 


def returnFrame(camera):
      ignore,frame = camera.read()
      return frame



cameraX = 0
cameraY = 0

cameraWindow = "Camera window"


trackWindow = "trackBars"
trackWindowHeight = 400
trackWindowWidth = 100
trackStart = 0 
resizeMax = int(cameraWidth/16)

xMax = 1920
yMax = 1080

def changeSize(val):
     global cameraWidth
     global cameraHeight
     cameraWidth = int(val * 16)
     cameraHeight = int(val * 9)
     print("Camera width: ", cameraWidth)
     print("Camera height: ", cameraHeight)
     cameraSizing(cameraWidth,cameraHeight)  
     

def changePostionX(val):
     global cameraX
     cameraX = val
     print("Camera x:", cameraX)
     cv2.moveWindow(cameraWindow,cameraX,cameraY)

def changePostionY(val):
     global cameraY
     cameraY = val
     print("Camera Y:", cameraY)
     cv2.moveWindow(cameraWindow,cameraX,cameraY)

sizeDisplayText = ""
textFont = cv2.FONT_HERSHEY_COMPLEX
textSize = 1
textThickness = 1
black = (0,0,0)
red = (0,0,255)
white = (255,255,255)

startInput = input(startQuestion)

if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cv2.namedWindow(trackWindow)
    cv2.namedWindow(cameraWindow)
    cv2.createTrackbar("Size",trackWindow,trackStart,resizeMax,changeSize)
    cv2.createTrackbar("x",trackWindow,trackStart,xMax,changePostionX)
    cv2.createTrackbar("y",trackWindow,trackStart,yMax,changePostionY)
    cameraFps(30)
    cameraSizing(cameraWidth,cameraHeight)

    
    while True:
      frame = returnFrame(camera)
      cv2.putText(frame,sizeDisplayText,(0,25),textFont,textSize,red,textThickness)
      cv2.imshow(cameraWindow,frame)
      sizeDisplayText = "Size: " + str(cameraWidth) + "," + str(cameraHeight)
      if cv2.waitKey(1) == ord("q"):
            break
    