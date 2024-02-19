import cv2
import mediapipe as mp
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

if startInput == startKey:
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
##formats how the video gets decoded (Set as moving jpeg)
    camera.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))
    cameraSizing(cameraWidth,cameraHeight)
    cameraFps(30)
    hands = mp.solutions.hands.Hands(False,2)
    mpDraw = mp.solutions.drawing_utils
    while True:
      frame = returnFrame(camera)
      frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      results = hands.process(frame)
      print(results)
      if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                 myHand=[]
                 print(handLandMarks)
                 #mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
                 for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*cameraWidth),int(landMark.y*cameraHeight)))
                 print(myHand)
                 cv2.circle(frame,myHand[20],2,(255,0,0),-1) 
      frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
      cv2.imshow("Camera window",frame)
      if cv2.waitKey(1) == ord("q"):
            break
      