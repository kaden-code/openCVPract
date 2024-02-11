import cv2
import time
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



 

def returnFrame(camera):
      ignore,frame = camera.read()
      return frame

faceFrontCascade = cv2.CascadeClassifier("haar\haarcascade_frontalface_default.xml")
faceSideCascade = cv2.CascadeClassifier("haar\haarcascade_profileface.xml")
eyeCascade = cv2.CascadeClassifier("haar\haarcascade_eye.xml")
smileCascade = cv2.CascadeClassifier("haar\haarcascade_smile.xml")


faceAngle = ""
fpsText = ""
red = (0,0,255)
startInput = input(startQuestion)
faceDetected = False
if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraHeight)
    cameraFps(30)
    
    while True:
      startTime = time.time()   
      frame = returnFrame(camera)
      greyFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      facesFront = faceFrontCascade.detectMultiScale(greyFrame,1.3,5)
      is_front_face_detected = False
      smileStatus = "False"
      for faceFront in facesFront:
        is_front_face_detected = True
        faceAngle = "Front"
        x, y, w, h = faceFront
        cv2.rectangle(frame, (x, y), (x + w, y + h), red, 3)
        faceROI = greyFrame[y:y+h,x:x+w] 
        smiles = smileCascade.detectMultiScale(faceROI,1.6,8)
        for smile in smiles:
                smileStatus = "True"
                smilex,smiley,smileWidth,smileHeight = smile
                cv2.rectangle(frame[y:y+h,x:x+w],(smilex,smiley),(smilex+smileWidth,smiley+smileHeight),red,3)
        
      if not is_front_face_detected:
            
          facesSide = faceSideCascade.detectMultiScale(greyFrame, 1.3, 5)
          for faceSide in facesSide:
            faceAngle = "Side"
            x, y, w, h = faceSide
            cv2.rectangle(frame, (x, y), (x + w, y + h), red, 3)
            faceROI = greyFrame[y:y+h,x:x+w] 
            for smile in smiles:
                smileStatus = "True"
                smilex,smiley,smileWidth,smileHeight = smile
                cv2.rectangle(frame[y:y+h,x:x+w],(smilex,smiley),(smilex+smileWidth,smiley+smileHeight),red,3)

      cv2.putText(frame,fpsText,(0,30),cv2.FONT_HERSHEY_COMPLEX,1,red,1)
      cv2.putText(frame,"Face ViewPoint: "+faceAngle,(0,60),cv2.FONT_HERSHEY_COMPLEX,1,red,1)
      cv2.putText(frame,"Smile Status: "+smileStatus,(0,90),cv2.FONT_HERSHEY_COMPLEX,1,red,1)
      
      cv2.imshow("Camera window",frame)
      endTime = time.time()
      duration = endTime - startTime
      fps = str(int(1/duration))
      fpsText = "fps: " + fps      
      
      if cv2.waitKey(1) == ord("q"):
            break