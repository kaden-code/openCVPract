import os
import cv2

# Get the base directory of the cv2 module
cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))

# Construct the full path to the Haar cascade XML file
haar_model_path = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')

print("Path to Haar cascade for face detection:", haar_model_path)
