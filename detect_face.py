import cv2
import numpy as np
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-test')
args = parser.parse_args()
if args.test == 'hi':
	print("hello there !")
"""
# https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('data/vid.mp4')

while True:
	_, img = cap.read()
	img = cv2.resize(img, (600, 400))
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
	cv2.imshow('img', img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()"""
"""
img = cv2.imread('data/peter.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 3)
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('img', img)
cv2.waitKey(3000)"""

#cv2.destroyAllWindows()