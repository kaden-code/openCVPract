import cv2 
import numpy as np

startKey = "A!"
startMsg = "Enter Pass: "
userInput = None

rows = 256
columns = 720
hsvWindow = "HSV Window"
hsvWindow2 = "HSV Window 2"
hsvDisplayFrame = np.zeros([rows,columns,3],dtype=np.uint8)
hsvDisplayFrame2 = np.zeros([rows,columns,3],dtype=np.uint8)
userInput = input(startMsg)


for rowPixel in range(0,256):
      for columnPixel in range(0,720):
            hsvDisplayFrame[rowPixel,columnPixel] = (int(columnPixel/4),rowPixel,255)
hsvDisplayFrame= cv2.cvtColor(hsvDisplayFrame,cv2.COLOR_HSV2BGR)

for rowPixel in range(0,256):
      for columnPixel in range(0,720):
            hsvDisplayFrame2[rowPixel,columnPixel] = (int(columnPixel/4),255,rowPixel)
hsvDisplayFrame2 = cv2.cvtColor(hsvDisplayFrame2,cv2.COLOR_HSV2BGR)


if startKey == userInput:
  while True:
    cv2.imshow(hsvWindow,hsvDisplayFrame)
    cv2.moveWindow(hsvWindow,0,0)
    cv2.imshow(hsvWindow2,hsvDisplayFrame2)
    cv2.moveWindow(hsvWindow2,0,256)
    if cv2.waitKey(1) == ord("q"):
     break 
    



