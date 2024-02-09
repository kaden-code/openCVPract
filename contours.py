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

def onHueLow2(val):
    global hueLow2
    hueLow2 = val

def onHueHigh2(val):
    global hueHigh2
    hueHigh2 = val

def onSatLow2(val):
    global satLow2
    satLow2 = val
    
def onSatHigh2(val):
    global satHigh2
    satHigh2 = val

def onValLow2(val):
    global valLow2
    valLow2 = val

def onValHigh2(val):
    global valHigh2
    valHigh2 = val

colorTrackingWindow = "colorTrackingWindow"
cv2.namedWindow(colorTrackingWindow)
cv2.moveWindow(colorTrackingWindow,cameraWidth,0)

color2TrackingWindow = "color2TrackingWindow"
cv2.namedWindow(color2TrackingWindow)
cv2.moveWindow(color2TrackingWindow,cameraWidth + (cameraWidth//2),0)

hueLow = 10
hueHigh = 20
satLow = 10
satHigh = 250
valLow = 10
valHigh = 250

red = (0,0,255)



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

  cv2.createTrackbar('Hue low 2',color2TrackingWindow,10,179,onHueLow2)
  cv2.createTrackbar('Hue High 2',color2TrackingWindow,20,179,onHueHigh2)
  cv2.createTrackbar('Sat low 2',color2TrackingWindow,10,255,onSatLow2)
  cv2.createTrackbar('Sat High 2',color2TrackingWindow,250,255,onSatHigh2)
  cv2.createTrackbar('Val 2',color2TrackingWindow,10,255,onValLow2)
  cv2.createTrackbar('Val High 2',color2TrackingWindow,250,255,onValHigh2)


  while True:
      frame = returnFrame(camera)
      frameHsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      lowerBound = np.array([hueLow,satLow,valLow])
      upperBound = np.array([hueHigh,satHigh,valHigh])

      lowerBound2 = np.array([hueLow2,satLow2,valLow2])
      upperBound2 = np.array([hueHigh2,satHigh2,valHigh2])
      ## converts pixels in the bounds to 1 or white and converts pixels out of bounds to 0 or black
      colorMask = cv2.inRange(frameHsv,lowerBound,upperBound)
      colorMask = colorMask + cv2.inRange(frameHsv,lowerBound2,upperBound2)
      contours,bin = cv2.findContours(colorMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
      for contour in contours:
            area = cv2.contourArea(contour)
            if area>= 200:
             ##cv2.drawContours(frame,[contour],0,red,3)
               x,y,w,h = cv2.boundingRect(contour)
               cv2.rectangle(frame,(x,y),(x+w,y+h),red,3)
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
    