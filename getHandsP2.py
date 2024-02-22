import cv2
startQuestion = "Enter Key: "
startKey = "A!"

cameraWidth = 640
cameraHeight = 320


class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2):
         self.hands=self.mp.solutions.hands.Hands(False,maxHands)

    def getHands(self,frame):
      myHands = []
      frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      results = self.hands.process(frameRGB)
      if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                 myHand=[]
                 for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*cameraWidth),int(landMark.y*cameraHeight)))
                 myHands.append(myHand)
                
      return myHands   


def getHands(ai,frame):
      myHands = []
      frame =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      results = ai.process(frame)
      if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                 myHand=[]
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
    handAi = mpHands()
    while True:
      frame = returnFrame(camera)
      myHands = handAi.getHands(frame)
      if myHands != None:
       for hand in myHands:
        for i in range(20):
                 cv2.circle(frame,hand[i],8,(255,0,0),3) 
             
    

      print(myHands)
      cv2.imshow("Camera window",frame)
      if cv2.waitKey(1) == ord("q"):
            break
      