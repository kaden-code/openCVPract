import cv2
import face_recognition as FR


startQuestion = "Enter Key: "
startKey = "AI"

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

font = cv2.FONT_HERSHEY_SIMPLEX

karterMusardImg = FR.load_image_file("familyFaces/karter.jpg")
karterMusardEncoded = FR.face_encodings(karterMusardImg)[0]

kadenMusardImg = FR.load_image_file("familyFaces/kaden.jpg")
kadenMusardEncoded = FR.face_encodings(kadenMusardImg)[0]

knownEncodings = [karterMusardEncoded,kadenMusardEncoded]
names = ["Karter", "Kaden"]







startInput = input(startQuestion)

if startInput == startKey:
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
          name = names[matchIndex]
        cv2.putText(unknownFace,name,(left,top-20),font,1,(0,0,255),1)

      cv2.imshow("Camera window",unknownFace)
      if cv2.waitKey(1) == ord("q"):
            break






      
