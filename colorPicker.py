import cv2
import numpy as np
startQuestion = "Password: "
startPass = "A!"
displaySquare = 720
userAnswer = None 
pixelEncoding = 3
bgrBlueValue = 0
bgrGreenValue = 0
bgrRedValue = 0

hsvHueValue = 0
hsvSaturationValue = 0
hsvValueValue = 255



bgrDisplayWindow = "bgr color"
bgrTrackWindow = "Customize Blue Green Red"
valueStart = 0
bgrColorValueMax = 255
hueMax = 179
saturationMax = 255
valueMax = 255
hsvDisplayWindow = "hsv color"
hsvTrackWindow = "Customize Hue Saturation Value"






def changeBlueValueBGR(val):
   global bgrBlueValue
   bgrBlueValue = val
   

def changeRedValueBGR(val):
   global bgrRedValue
   bgrRedValue = val

def changeGreenValueBGR(val):
   global bgrGreenValue
   bgrGreenValue = val



def changeHSVHue(val):
   global hsvHueValue
   hsvHueValue = val

def changeHSVSaturation(val):
   global hsvSaturationValue
   hsvSaturationValue = val

def changeHSVValue(val):
   global hsvValueValue
   hsvValueValue = val
   
   
   


def makeColorBGR():
    frame = np.zeros([displaySquare,displaySquare,pixelEncoding], dtype = np.uint8)
   ## cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    bgrColor = (bgrBlueValue,bgrGreenValue,bgrRedValue)

    frame[:,:] = bgrColor
    return frame


def makeColorHSV():
    frame = np.zeros([displaySquare,displaySquare,pixelEncoding], dtype = np.uint8)
    cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsvColor = (hsvHueValue,hsvSaturationValue,hsvValueValue)
    
    frame[:,:] = hsvColor
    cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
    return frame

userAnswer = input(startQuestion)
if userAnswer == startPass:
    cv2.namedWindow(bgrDisplayWindow)
    cv2.namedWindow(bgrTrackWindow)
    cv2.namedWindow(hsvDisplayWindow)
    cv2.namedWindow(hsvTrackWindow)
    cv2.createTrackbar("Blue: ", bgrTrackWindow,valueStart,bgrColorValueMax, changeBlueValueBGR)
    cv2.createTrackbar("Green: ", bgrTrackWindow,valueStart,bgrColorValueMax, changeGreenValueBGR)
    cv2.createTrackbar("Red: ", bgrTrackWindow,valueStart,bgrColorValueMax, changeRedValueBGR)

    cv2.createTrackbar("Hue: ", hsvTrackWindow,valueStart,hueMax, changeHSVHue)
    cv2.createTrackbar("Saturation: ", hsvTrackWindow,valueStart,saturationMax, changeHSVSaturation)
    cv2.createTrackbar("Value: ", hsvTrackWindow,valueStart,valueMax, changeHSVValue)  
    while True:
      bgrFrame = makeColorBGR()
      cv2.imshow(bgrDisplayWindow, bgrFrame)
      hsvFrame = makeColorHSV()
      cv2.imshow(hsvDisplayWindow, hsvFrame)

      if cv2.waitKey(1) == ord("q"):
         break