import os
import cv2
import face_recognition as FR
imgDir = 'C:/Users/12403/coding/aiPract/familyFaces'
for root,dirs,files in os.walk(imgDir):
    print("root:" ,root)
    print("dirs in root:" ,dirs)
    print("files in root:" ,files)
    for file in files:
        print("Person: ",file)
        fullFilePath = (root+"/"+file)
        print("Persons Path: ", fullFilePath)
        name=os.path.splitext(file)[0]
        print(name)
        myPicture =FR.load_image_file(fullFilePath)
        myPicture = cv2.cvtColor(myPicture,cv2.COLOR_RGB2BGR)
        cv2.imshow(name,myPicture)
        cv2.moveWindow(0,0)
        cv2.waitKey(2500)
