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




trackWindow = "trackBars"
trackWindowHeight = 400
trackWindowWidth = 100
trackStart = 0 
trackMax = 80

def changeWidth(val):
     global cameraWidth
     print("Camera width: ", val)
     cameraWidth = int(val * 16)
     cameraSizing(cameraWidth,cameraHeight)  
     


def changeHeight(val):
     global cameraHeight
     cameraHeight = int(val * 9)
     cameraSizing(cameraWidth,cameraHeight)  
     print("Camera height: ", cameraHeight)





startInput = input(startQuestion)

if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cv2.namedWindow(trackWindow)
    cv2.createTrackbar("camera width",trackWindow,trackStart,trackMax,changeWidth)
    cv2.createTrackbar("camera height",trackWindow,trackStart,trackMax,changeHeight)
    cameraFps(30)
    cameraSizing(cameraWidth,cameraHeight)

    
    while True:
      frame = returnFrame(camera)
      cv2.imshow("Camera window",frame)
      if cv2.waitKey(1) == ord("q"):
            break
    