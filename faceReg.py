import cv2
import face_recognition as FR

font = cv2.FONT_HERSHEY_SIMPLEX
donaldTrumpImg = FR.load_image_file('demoimgs/known/Donald Trump.jpg')
donaldTrumpEncoded = FR.face_encodings(donaldTrumpImg)[0]

nancyPelosiImg = FR.load_image_file('demoimgs/known/Nancy Pelosi.jpg')
nancyPelosiEncoded = FR.face_encodings(nancyPelosiImg)[0]



knownEncodings = [donaldTrumpEncoded,nancyPelosiEncoded]
names = ["Donald Trump", "Nancy Pelosi"]

unknownFace = FR.load_image_file("demoimgs/unknown/u3.jpg")
##returns [(top right bottom left)]
faceLocations = FR.face_locations(unknownFace)
unknownEncodings = FR.face_encodings(unknownFace,faceLocations)
unknownFace = cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)

for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
    top,right,bottom,left = faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFace,(left,top),(right,bottom),(0,0,255),3)
    name ="unknown person"
    matches = FR.compare_faces(knownEncodings,unknownEncoding)
    print(matches)
    if True in matches:
        matchIndex =matches.index(True)
        print(matchIndex)
        name = names[matchIndex]
    cv2.putText(unknownFace,name,(left,top-20),font,1,(0,0,255),1)

while True:
    cv2.imshow("Unknown face",unknownFace)
    if cv2.waitKey(1) == ord('q'):
        break
