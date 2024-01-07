import cv2

startQuestion = "Enter Key: "
startKey = "AI"

mainWindow = "mainWindow"
dvdWindow = "dvdWindow"
pixelX = 1280
pixelY = 720

cameraWidth = pixelX
cameraHeight = pixelY

rowEDGE = cameraWidth
columnEDGE = cameraHeight
rows = 0
columns = 0

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

def showWindow(name,frame,x,y):
     cv2.imshow(name,frame)
     cv2.moveWindow(name,x,y)
    
roiRowStart = int(rowEDGE/2 - 200)
roiRowEnd= int(rowEDGE/2 + 200)
roiColumnStart = int(columnEDGE/2 - 100)
roiColumnEnd = int(columnEDGE/2 + 100)

dvdBackState = False

textContent = "DVD"
textFont = cv2.FONT_HERSHEY_COMPLEX
textSize = 1
textThickness = 1

black = (0,0,0)
red = (0,0,255)
white = (255,255,255)


if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraWidth)
    cameraFps(30)
    
    while True:
      frame = returnFrame(camera)
      rangeOfIntrest = frame[roiColumnStart:roiColumnEnd,roiRowStart:roiRowEnd]
      frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)


      if dvdBackState == False:
        roiColumnStart = roiColumnStart + 5
        roiColumnEnd = roiColumnEnd + 5
        roiRowStart = roiRowStart + 5
        roiRowEnd = roiRowEnd + 5
        print(roiColumnEnd)
        if roiColumnEnd == cameraHeight - 5:
          dvdBackState = True

        if roiRowEnd == cameraWidth - 5:
          dvdBackState = True
        startTextX = roiRowStart +5
        startTextY = roiColumnStart +5
        cv2.putText(frame,textContent,(startTextX,startTextY),textFont,textSize,white,textThickness)
        frame[roiColumnStart:roiColumnEnd,roiRowStart:roiRowEnd] = rangeOfIntrest



      if dvdBackState == True:
        roiColumnStart = roiColumnStart - 5
        roiColumnEnd = roiColumnEnd - 5
        roiRowStart = roiRowStart - 5
        roiRowEnd = roiRowEnd - 5
        print(roiColumnStart)
        if roiColumnStart == 5:
          dvdBackState = False

        if roiRowStart == 5:
          dvdBackState = False
        startTextX = roiRowStart - 5
        startTextY = roiColumnStart - 5
        cv2.putText(frame,textContent,(startTextX,startTextY),textFont,textSize,white,textThickness)
        frame[roiColumnStart:roiColumnEnd,roiRowStart:roiRowEnd] = rangeOfIntrest
     
      
      showWindow(mainWindow,frame,0,0)
      showWindow(dvdWindow,rangeOfIntrest,cameraWidth + 5,0)
      
      if cv2.waitKey(1) == ord("q"):
            break
else:
     print("wrong password")