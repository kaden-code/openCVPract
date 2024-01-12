import cv2

import cv2

startQuestion = "Enter Key: "
startKey = "AI"
window = "window"
window2 = "roi"


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

clickPostion = None
clickType = None


def onClick(event,xPos,yPos,params,flags):
    global clickPostion
    global clickType
    global showRoi
    if event == cv2.EVENT_LBUTTONDOWN:
     clickType = event 
     clickPostion = (xPos,yPos)
     print("left btn down")

    if event == cv2.EVENT_LBUTTONUP:
     clickType = event 
     clickPostion = (xPos,yPos)
     print("left btn up")

    if event == cv2.EVENT_RBUTTONDOWN:
      print(event)
      clickType = event


      print("right vutton lv")
     


    
showRoi = False
startCornerX = 0
startCornerY = 0
endCornerX = 0
endCornerY = 0


startInput = input(startQuestion)

if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraHeight)
    cameraFps(30)
    cv2.namedWindow(window)
    cv2.setMouseCallback(window,onClick)
    
    while True:
      frame = returnFrame(camera)
      if clickType == 1:
         startCornerX = int(clickPostion[0])
         startCornerY = int(clickPostion[1])
         
      if clickType == 4:
         endCornerX = int(clickPostion[0])
         endCornerY = int(clickPostion[1])
         print("Start x: ", startCornerX)
         print("Start Y: ", startCornerY)
         print("end X: ", endCornerX )
         print("end Y: ", endCornerY)
         roi = frame[startCornerY:endCornerY,startCornerX:endCornerX]
         showRoi = True
      
    

      if showRoi == True:
         cv2.imshow(window2,roi)
         print(showRoi)

      if clickType == 2:
         if showRoi == True:
           cv2.destroyWindow(window2)
           showRoi = False
           clickType = None
         else:
                print("No window to kill")
                clickType = None

            
      cv2.imshow(window,frame)
      if cv2.waitKey(1) == ord("q"):
            break
    