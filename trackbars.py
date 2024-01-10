import cv2

startQuestion = "Enter Key: "
startKey = "AI"

cameraWidth = 1280
cameraHeight = 720

trackWindow = "trackBars"
trackBarWidth = 400
trackBarHeight= 100
trackXStart = 860
trackXMax = 1920
trackYStart = 540
trackYMax = 1080

def cameraSizing(width,height):
     camera.set(cv2.CAP_PROP_FRAME_WIDTH,width)
     camera.set(cv2.CAP_PROP_FRAME_HEIGHT,height)


def cameraFps(fps):
     camera.set(cv2.CAP_PROP_FPS,fps)
                           ## lets windows know that the video captures intent is to show allowing for faster performace 





def returnFrame(camera):
      ignore,frame = camera.read()
      return frame



def trackBarFunction(val):
    print(val)

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
    cv2.createTrackbar('xPos',trackWindow,trackXStart,trackXMax,trackBarFunction)
    cv2.createTrackbar('yPos',trackWindow,trackYStart,trackYMax,trackBarFunction)
    while True:
      frame = returnFrame(camera)
      cv2.imshow("Camera window",frame)
      if cv2.waitKey(1) == ord("q"):
            break
    