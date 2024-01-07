import numpy as np


def spacePrint():
    print()
    print()
    print()
## defines ma
frame = np.zeros([5,5],dtype= np.uint8)
print(frame)
spacePrint()
## changes 1 pixel at a time
frame[3,1] = 255
print(frame)
spacePrint()

## changes multiple pixels at a time
frame[:,:] = 0
print(frame)
spacePrint()

frame[0:5,1:4] = 255
print(frame)
spacePrint()


## Creates color frame

colorFrame = np.zeros([3,3,3], dtype = np.uint8)
print(colorFrame)
spacePrint()
colorFrame[0,0] = (255,255,255)
print(colorFrame)
spacePrint()