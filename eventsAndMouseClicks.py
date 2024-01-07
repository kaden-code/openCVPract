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



window = "window"

def returnFrame(camera):
      ignore,frame = camera.read()
      return frame

startInput = input(startQuestion)

def mouseClick(event,xPos,yPos,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
     print("Mouse wheel down")
     print("Event type: ", event)
     print("Cursor x: ", xPos)
     print("Cursor y: ", yPos)
     print("Flags: ", flags)
     print("Params: ", params)
    
  
    if event == cv2.EVENT_MOUSEWHEEL:
     print("Mouse wheel down")
     print("Event type: ", event)
     print("Cursor x: ", xPos)
     print("Cursor y: ", yPos)
     print("Flags: ", flags)
     print("Params: ", params)
    if event == cv2.EVENT_RBUTTONDOWN:
     print("Roght mouse click")
     print("Event type: ", event)
     print("Cursor x: ", xPos)
     print("Cursor y: ", yPos)
     print("Flags: ", flags)
     print("Params: ", params)



if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraWidth)
    cameraFps(30)
    cv2.namedWindow(window)
    cv2.setMouseCallback(window,mouseClick)
    while True:
      frame = returnFrame(camera)
      cv2.imshow(window,frame)
      if cv2.waitKey(1) == ord("q"):
            break