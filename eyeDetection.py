import cv2
import time
startQuestion = "Enter Key: "
startKey = "A!"

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

faceCascade = cv2.CascadeClassifier("haar\haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haar\haarcascade_eye.xml")
textContent = ""
red = (0,0,255)
startInput = input(startQuestion)

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
      faces = faceCascade.detectMultiScale(greyFrame,1.3,5)
      eyes = eyeCascade.detectMultiScale(greyFrame,1.3,5)
      for face in faces:
               x,y,w,h = face
               cv2.rectangle(frame,(x,y),(x+w,y+h),red,3)
               cv2.putText(frame,"Face detected:",(x-20,y-20),cv2.FONT_HERSHEY_COMPLEX,1,red,1)
               faceROI = greyFrame[y:y+h,x:x+w] 
               eyes = eyeCascade.detectMultiScale(faceROI)
               for eye in eyes:
                eyex,eyey,eyeWidth,eyeHeight = eye
                cv2.rectangle(frame[y:y+h,x:x+w],(eyex,eyey),(eyex+eyeWidth,eyey+eyeHeight),red,3)
      
      
            
      cv2.putText(frame,textContent,(20,20),cv2.FONT_HERSHEY_COMPLEX,1,red,1)
      cv2.imshow("Camera window",frame)
      endTime = time.time()
      duration = endTime - startTime
      fps = str(int(1/duration))
      textContent = "fps: " + fps      
      
      if cv2.waitKey(1) == ord("q"):
            break