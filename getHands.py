import cv2
import mediapipe as mp
startQuestion = "Enter Key: "
startKey = "A!"

cameraWidth = 640
cameraHeight = 320



def getHands(ai,frame):
      myHands = []
      frame =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      results = ai.process(frame)
      if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                 myHand=[]
                 print(handLandMarks)
                 #mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
                 for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*cameraWidth),int(landMark.y*cameraHeight)))
                 myHands.append(myHand)
                
            return myHands
      

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
    handAi = mp.solutions.hands.Hands(False,2)
    mpDraw = mp.solutions.drawing_utils
    while True:
      myHands = []
      frame = returnFrame(camera)
      myHands = getHands(handAi,frame)
      if myHands != None:
       for hand in myHands:
        for i in range(20):
                 cv2.circle(frame,hand[i],8,(255,0,0),3) 
             
    

      print(myHands)
      cv2.imshow("Camera window",frame)
      if cv2.waitKey(1) == ord("q"):
            break
      