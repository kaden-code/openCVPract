import cv2

startQuestion = "Enter Key: "
startKey = "AI"

cameraWidth = 640
cameraHeight = 360



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

startInput = input(startQuestion)

if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraHeight)
    cameraFps(30)
    
    while True:
      frame = returnFrame(camera)
      frameROI = frame[140:260, 240:360]
      frameROIGray = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
      frameROIBGR = cv2.cvtColor(frameROIGray,cv2.COLOR_GRAY2BGR)
      frame[140:260,240:360] = frameROIBGR
      cv2.imshow("Region of intrest", frameROI)
      cv2.moveWindow("Region of intrest", 650,0 )
      cv2.imshow("Region of intrest gray", frameROIGray)
      cv2.moveWindow("Region of intrest gray", 650,150)
      cv2.imshow("Region of intrest BGR", frameROIBGR)
      cv2.moveWindow("Region of intrest BGR", 650,300)
      cv2.imshow("Camera window",frame)
      cv2.moveWindow("Camera window", 0,0)
      if cv2.waitKey(1) == ord("q"):
            break
    