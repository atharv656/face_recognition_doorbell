import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

from VideoCapture import Device

cam = Device ()
cam.Snapshot("john.jpg")