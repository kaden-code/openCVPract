import os
import time
import cv2
import face_recognition as FR
trainingFile = 'C:/Users/12403/coding/aiPract/familyFaces'
knownEncodings = []
knownNames = []
startQuestion = "Enter Key: "
startKey = "A!"
font = cv2.FONT_HERSHEY_SIMPLEX
cameraWidth = 640
cameraHeight = 320
window = " "
faceCascade = cv2.CascadeClassifier("haar\haarcascade_frontalface_default.xml")

def trainFaces(path,knownFaces,knownNames):
    for root,directories,files in os.walk(path):
       print("Training In" ,root)
       for file in files:
         fullFilePath = (root+"/"+file)
         name=os.path.splitext(file)[0]
         print("Training On ",name,"...")
         myPicture =FR.load_image_file(fullFilePath)
         myPicture = cv2.cvtColor(myPicture,cv2.COLOR_RGB2BGR)
         face = FR.face_encodings(myPicture)[0]
         knownFaces.append(face)
         knownNames.append(name)
    print("Opening eyes....")



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
    trainFaces(trainingFile,knownEncodings,knownNames)
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraHeight)
    cameraFps(30)
    cv2.namedWindow(window)
    while True:
      unknownFace = returnFrame(camera)
      unknownFace = cv2.cvtColor(unknownFace,cv2.COLOR_BGR2RGB)
      ##returns [(top right bottom left)]
      faceLocations = FR.face_locations(unknownFace)
      unknownEncodings = FR.face_encodings(unknownFace,faceLocations)
      unknownFace = cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
      for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left = faceLocation
        print(faceLocation)
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(0,0,255),3)
        name = "unknown person"
        matches = FR.compare_faces(knownEncodings,unknownEncoding)
        print(matches)
        if True in matches:
          matchIndex = matches.index(True)
          print(matchIndex)
          name = knownNames[matchIndex]
        cv2.putText(unknownFace,name,(left,top-20),font,1,(0,0,255),1)
      cv2.imshow(window,unknownFace)
      pressedKey = cv2.waitKey(1) & 0xFF
      ## camera loop for inspection,detect face in roi and take img of face,store img of face in filesytem with name,train on face in running program
      if pressedKey == ord('i'):
        print("Inspecting...")
        waitTime = 3
        while True:
              startTime = time.time()   
              frame = returnFrame(camera)
              cv2.rectangle(frame,(cameraWidth//4,cameraHeight//4) ,(cameraWidth*3//4,cameraHeight*3//4), (0,0,255), 4)
              frameRoi = frame[cameraHeight//4:cameraHeight*3//4,cameraWidth//4:cameraWidth*3//4]
              grayRoi = cv2.cvtColor(frameRoi,cv2.COLOR_BGR2GRAY)
              faces = faceCascade.detectMultiScale(grayRoi,1.3,5)
              endTime = time.time()
              if len(faces) == 0:
                  cv2.putText(frame,"Put Face in rectangle",(cameraWidth//4,cameraHeight//4),font,1,(0,0,255),1)

              else:
                  duration = endTime - startTime
                  waitTime = waitTime - duration
                  if waitTime <= 0:                        
                    name = input("Faces name: ")
                    if name == "breakQ":
                          break
                    face = FR.face_encodings(frameRoi)[0]
                    knownEncodings.append(face)
                    knownNames.append(name)

                    cv2.imwrite(os.path.join(trainingFile, name + '.jpg'), frameRoi)
                    break
                  cv2.putText(frame,str(int(waitTime)),(0,25),font,1,(0,0,255),1) 
              cv2.imshow(window,frame)
              quitIdentify = cv2.waitKey(1) & 0xFF
              if quitIdentify == ord('k'):
                    break

      elif pressedKey == ord('q'):
        print("quit")
        break    