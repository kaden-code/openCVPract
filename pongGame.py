import numpy as np
import cv2
import time
startQuestion = "Enter Key: "
startKey = "A!"

cameraWidth = 640
cameraHeight = 320

paddleWidth = 125
paddleHeight = 25
paddleColor = (0,255,0)
paddleX = None
paddleY = None

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


''' def displayDeath(): '''


    


def cameraFps(fps):
     camera.set(cv2.CAP_PROP_FPS,fps)
                           ## lets windows know that the video captures intent is to show allowing for faster performace 


ballX,ballY = cameraHeight - 12,cameraWidth - 24
ballCordinates = (ballX,ballY)

def createBall(frame,ballCordinates):
    cv2.circle(frame,ballCordinates,3,(255,255,255),25)

def moveBall(ballCordinates):

  return ballCordinates

        


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
    ballXRight = True
    ballYUp = True
    lives = 3
    death = False
    ballSpeed = 5
    font = cv2.FONT_HERSHEY_SIMPLEX
    handAi = mpHands()
    deathScreen = cv2.imread("pongImgs/You died.png")
    while True:
      frame = returnFrame(camera)
      myHands = handAi.getHands(frame)
      if ballXRight == True:
          ballX = ballX +  ballSpeed
          ballCordinates = (ballX,ballY)
        
      if ballXRight == False:
        ballX = ballX -  ballSpeed
        ballCordinates = (ballX,ballY)
        
      if ballX >= cameraWidth - 12:
        ballXRight = False

      if ballX <= 12:
        ballXRight = True

      if ballYUp == True:
        ballY += - ballSpeed
        ballCordinates = (ballX,ballY)
        
      if ballYUp == False:
        ballY +=  ballSpeed
        ballCordinates = (ballX,ballY)
        
      if ballY >= cameraHeight + 24:
        ballYUp = True

      if ballY <= 12:
        lives += -1
        ballY = cameraHeight + 24
      if lives == 0: 
       death = True
      createBall(frame,ballCordinates)
      if myHands != None:
           for hand in myHands:
             cv2.rectangle(frame,(hand[8][0] - paddleWidth//2 ,0),(hand[8][0] + paddleWidth//2,paddleHeight),paddleColor,-1)
             # Given rectangle parameters
             rectX = hand[8][0] - paddleWidth // 2  # X-coordinate of the left edge
             rectY = 24                            # Y-coordinate of the top edge
             rectWidth = paddleWidth               # Width of the rectangle
             rectHeight = paddleHeight             # Height of the rectangle

             # Check for collision
             if rectX <= ballX <= rectX + rectWidth and rectY <= ballY <= rectY + rectHeight:
               ballYUp = False
               ballSpeed += 1
      if death == False:
        cv2.imshow("Camera window", frame)
      else:
        cv2.imshow("Camera window", deathScreen)
      cv2.moveWindow("Camera window",0,0)
    

      if cv2.waitKey(1) == ord("q"):
            break