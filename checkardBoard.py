import cv2
print(cv2.__version__)
import numpy as np
red = (000,000,255)
black = (000,000,000)


def checkeredRow(board,squareSize,oldRange,rowStart,rowEnd,startColor,endColor):
   ogSize = squareSize
   for i in range(1,9):
         if i % 2 == 0:
          board[ rowStart:rowEnd , oldRange:squareSize] = endColor
          oldRange = squareSize
          squareSize = squareSize + ogSize

          print("Red")
          print("Square: ", i,"postion:",oldRange,squareSize)


         if i % 2 != 0:
          board[rowStart:rowEnd , oldRange:squareSize] = startColor
          oldRange = squareSize
          squareSize = squareSize + ogSize

          print("Black")
          print("Square: ", i,"postion:",oldRange,squareSize)
    

def makeCheckerBoard():
   board = np.zeros([640,640,3],dtype= np.uint8)
   squareSize = 80
   oldRange = 0
   checkeredRow(board,squareSize,oldRange,0,80,red,black)
   checkeredRow(board,squareSize,oldRange,80,160,black,red)
   checkeredRow(board,squareSize,oldRange,160,240,red,black)
   checkeredRow(board,squareSize,oldRange,240,320,black,red)
   checkeredRow(board,squareSize,oldRange,320,400,red,black)
   checkeredRow(board,squareSize,oldRange,400,480,black,red)
   checkeredRow(board,squareSize,oldRange,480,560,red,black)
   checkeredRow(board,squareSize,oldRange,560,640,black,red)
   return board


while True:
   frame = makeCheckerBoard()
   print(frame)
   cv2.imshow("Frame window",frame)

   if cv2.waitKey(1) == ord("q"):
        break
  