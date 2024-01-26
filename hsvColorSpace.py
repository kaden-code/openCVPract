import cv2
import numpy as np

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

clickType = None
clickPosition = None
def mouseClick(event,xPos,yPos,flags,params):
    global clickType
    global clickPosition
    clickType = event
    print("Event type: ", event)
    print("Cursor x: ", xPos)
    print("Cursor y: ", yPos)         
    print("Flags: ", flags)
    print("Params: ", params)
    clickType = event
    clickPosition = (xPos,yPos)

startInput = input(startQuestion)
window = "window"

bgrDisplayWindow = "bgrWindow"
hsvDisplayWindow = "hsvWindow"
black = (0,0,0)
displaySquare = 250
pixelEncoding = 3
textCordinates = (0,50)
font = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1
fontThickness = 1

if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraHeight)
    cameraFps(30)
    cv2.namedWindow(window)
    cv2.setMouseCallback(window,mouseClick)

    while True:
      frame = returnFrame(camera)
      if clickType == 0:
        
        bgrDisplayFrame = np.zeros([displaySquare,displaySquare,pixelEncoding],dtype = np.uint8)
        hsvDisplayFrame = np.zeros([displaySquare,displaySquare,pixelEncoding],dtype = np.uint8)
        ## converts this creates another matrix with same dimensions from bgr(blue,green,red) color sapce to hsv (hue saturation value) color space
        hsvFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        clickColorBGR = frame[clickPosition[1]][clickPosition[0]]
        clickColorHSV = hsvFrame[clickPosition[1]][clickPosition[0]]
        print(clickColorBGR)
        print(clickColorHSV)
        bgrDisplayFrame[:,:] = clickColorBGR
        hsvDisplayFrame[:,:] = clickColorHSV
        hsvDisplayFrame = cv2.cvtColor(hsvDisplayFrame,cv2.COLOR_HSV2BGR)
        cv2.putText(bgrDisplayFrame,str(clickColorBGR),textCordinates,font,fontScale,black,fontThickness)
        cv2.imshow(bgrDisplayWindow, bgrDisplayFrame)    
        cv2.putText(hsvDisplayFrame,str(clickColorHSV),textCordinates,font,fontScale,black,fontThickness)
        cv2.moveWindow(bgrDisplayWindow, cameraWidth,0)
        cv2.imshow(hsvDisplayWindow, hsvDisplayFrame)    
        cv2.moveWindow(hsvDisplayWindow, cameraWidth,displaySquare)
        clickType = None     
      cv2.imshow(window,frame)
      if cv2.waitKey(1) == ord("q"):
            break
    