import cv2
import face_recognition as FR



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



font = cv2.FONT_HERSHEY_SIMPLEX
kadenMusardImg = FR.load_image_file("familyFaces/kaden.jpg")
kadenMusardEncoded = FR.face_encodings(kadenMusardImg)[0]

serenityMusardImg = FR.load_image_file("familyFaces/serenity.jpg")
serenityMusardEncoded = FR.face_encodings(serenityMusardImg)[0]



karterMusardImg = FR.load_image_file("familyFaces/karter.jpg")
karterMusardEncoded = FR.face_encodings(karterMusardImg)[0]

tyvinMusardImg = FR.load_image_file("familyFaces/tyvin.jpg")
test = FR.face_locations(tyvinMusardImg)
tyvinMusardEncoded = FR.face_encodings(tyvinMusardImg)[0]
print(test) 
##tyvinMusardEncoded = FR.face_encodings(tyvinMusardImg)[0]


knownEncodings = [kadenMusardEncoded,serenityMusardEncoded,karterMusardEncoded,tyvinMusardEncoded]
names = ["Kaden","Serenity","Karter","tyvin"]




startInput = input(startQuestion)

if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraHeight)
    cameraFps(30)
    # Resize factor for the frame of video
    resize_factor = 0.2
# Scale factor for the face locations
    scale_factor = int(1 / resize_factor)

    while True:
      frame = returnFrame(camera)
##      faceLocations = FR.face_locations(frame)
  ##    unknownEncodings = FR.face_encodings(frame,faceLocations)
      # Resize the frame of video to a smaller size
      small_frame = cv2.resize(frame, (0, 0), fx=resize_factor, fy=resize_factor)
      small_frame = small_frame[:, :, ::-1]
      faceLocations = FR.face_locations(small_frame)
      unknownEncodings = FR.face_encodings(small_frame, faceLocations)
# Scale back up the face locations
      faceLocations = [(top * scale_factor, right * scale_factor, bottom * scale_factor, left * scale_factor) for top, right, bottom, left in faceLocations]

      for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left = faceLocation
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),3)
        name ="unknown person"
        matches = FR.compare_faces(knownEncodings,unknownEncoding,0.5)
        print(matches)
        if True in matches:
          matchIndex = matches.index(True)
          name = names[matchIndex]
          cv2.putText(frame,name,(left,top-20),font,1,(0,0,255),1)
      cv2.imshow("Camera window",frame)
      if cv2.waitKey(1) == ord("q"):
            break