import os
import cv2
import face_recognition as FR

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

trainingFile = 'C:/Users/12403/coding/aiPract/familyFaces'
knownEncodings = []
knownNames = []

startQuestion = "Enter Key: "
startKey = "A!"

cameraWidth = 640
cameraHeight = 320

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
font = cv2.FONT_HERSHEY_SIMPLEX

if startInput == startKey:
    trainFaces(trainingFile,knownEncodings,knownNames)
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraHeight)
    cameraFps(30)
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
      cv2.imshow("Camera window",unknownFace)
      if cv2.waitKey(1) == ord("q"):
            break