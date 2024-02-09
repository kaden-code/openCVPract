import cv2
import numpy as np

startQuestion = "Enter Key: "
startKey = "A!"

cameraWidth = 640
cameraHeight = 360

def cameraSizing(width,height):
     camera.set(cv2.CAP_PROP_FRAME_WIDTH,width)
     camera.set(cv2.CAP_PROP_FRAME_HEIGHT,height)


def cameraFps(fps):
     camera.set(cv2.CAP_PROP_FPS,fps)
                           ## lets windows know that the video captures intent is to show allowing for faster performace 


def onHueLow(val):
    global hueLow
    hueLow = val

def onHueHigh(val):
    global hueHigh
    hueHigh = val
def onSatLow(val):
    global satLow
    satLow = val
def onSatHigh(val):
    global satHigh
    satHigh = val
def onValLow(val):
    global valLow
    valLow = val
def onValHigh(val):
    global valHigh
    valHigh = val

colorTrackingWindow = "colorTrackingWindow"
cv2.namedWindow(colorTrackingWindow)
cv2.moveWindow(colorTrackingWindow,cameraWidth,0)

hueLow = 10
hueHigh = 20
satLow = 10
satHigh = 250
valLow = 10
valHigh = 250



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
  cv2.createTrackbar('Hue low',colorTrackingWindow,10,179,onHueLow)
  cv2.createTrackbar('Hue High',colorTrackingWindow,20,179,onHueHigh)
  cv2.createTrackbar('Sat low',colorTrackingWindow,10,255,onSatLow)
  cv2.createTrackbar('Sat High',colorTrackingWindow,250,255,onSatHigh)
  cv2.createTrackbar('Val',colorTrackingWindow,10,255,onValLow)
  cv2.createTrackbar('Val High',colorTrackingWindow,250,255,onValHigh)


  while True:
      frame = returnFrame(camera)
      frameHsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      lowerBound = np.array([hueLow,satLow,valLow])
      upperBound = np.array([hueHigh,satHigh,valHigh])
      ## converts pixels in the bounds to 1 or white and converts pixels out of bounds to 0 or black
      colorMask = cv2.inRange(frameHsv,lowerBound,upperBound)
      ## looks at which pixels on the mask is filled in with a 1 or b 0

      colorObject = cv2.bitwise_and(frame,frame,mask=colorMask)
      cv2.imshow("Mask window",colorMask)
      cv2.moveWindow("Mask window",0,cameraHeight)
      cv2.imshow("Object window",colorObject)
      cv2.moveWindow("Object window",cameraWidth,cameraHeight)
      cv2.imshow("Camera window",frame)
      cv2.moveWindow("Camera window",0,0)
      if cv2.waitKey(1) == ord("q"):
            break
    