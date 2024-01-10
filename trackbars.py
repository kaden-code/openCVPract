import cv2

startQuestion = "Enter Key: "
startKey = "AI"

cameraWidth = 1280
cameraHeight = 720

trackWindow = "trackBars"
trackBarWidth = 400
trackBarHeight= 150
trackXStart = 0
trackXMax = cameraWidth
trackYStart = 0
trackYMax = cameraHeight
trackRadiusStart = 0
trackRadiusMax = int(cameraHeight/2)
trackThicknessStart = 0
trackThicknessMax = 100

trackX = int(trackXMax/2)
trackY = int(trackYMax/2)



circleRadius = 25
circleThickness = 2
blue = (255,0,0)
def cameraSizing(width,height):
     camera.set(cv2.CAP_PROP_FRAME_WIDTH,width)
     camera.set(cv2.CAP_PROP_FRAME_HEIGHT,height)


def cameraFps(fps):
     camera.set(cv2.CAP_PROP_FPS,fps)
                           ## lets windows know that the video captures intent is to show allowing for faster performace 





def returnFrame(camera):
      ignore,frame = camera.read()
      return frame



def xBarFunction(val):
    global trackX
    trackX = val
    print("x: ",val)


def yBarFunction(val):
    global trackY
    trackY = val
    print("y: ", val)

def radiusBarFunction(val):
    global circleRadius
    circleRadius = val
    print("Radius: ", val)

def thicknessBarFunction(val):
    global circleThickness
    circleThickness = val
    print("Radius: ", val)


startInput = input(startQuestion)
if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraWidth)
    cameraFps(30)
    cv2.namedWindow(trackWindow)
    cv2.resizeWindow(trackWindow,trackBarWidth,trackBarHeight)
    cv2.moveWindow(trackWindow,cameraWidth,0)
    cv2.createTrackbar('xPos',trackWindow,trackXStart,trackXMax,xBarFunction)
    cv2.createTrackbar('yPos',trackWindow,trackYStart,trackYMax,yBarFunction)
    cv2.createTrackbar('Radius',trackWindow,trackRadiusStart,trackRadiusMax,radiusBarFunction)
    cv2.createTrackbar('Thickness',trackWindow,trackThicknessStart,trackThicknessMax,thicknessBarFunction)
    while True:
      frame = returnFrame(camera)
      cv2.circle(frame,(trackX,trackY),circleRadius,blue,circleThickness)
      cv2.imshow("Camera window",frame)
      if cv2.waitKey(1) == ord("q"):
            break
    