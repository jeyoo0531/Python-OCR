#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv
import sys
from PIL import Image
from pytesser import *

if __name__ == '__main__':
	capture = cv.CaptureFromCAM(0)

	cv.NamedWindow('Webcam')
	while True:
		frame = cv.QueryFrame(capture)
		cv.ShowImage('Webcam', frame)

		k = cv.WaitKey(10) % 256

		if k % 256 == 27: #esc button to exit the webcam
			break
		elif k == ord('s'): #press 's' keyboard button to save image into desktop
			cv.SaveImage('C:\Users\user\Desktop\image.jpg', frame)
			img = cv.LoadImage('C:\Users\user\Desktop\image.jpg')
			cv.ShowImage('Sample', img)
			img2= Image.open('C:\Users\user\Desktop\image.jpg')
			text = image_to_string(img2)
			print text
			
               #cv.LoadImage may be unnecessary...         			

	cv.DestroyWindow('Webcam')
	cv.DestroyWindow('Sample')
	capture = None

	# if __name__ == '__main__':
	#capture = cv.CaptureFromCAM(0)

	#cv.NamedWindow('Webcam')

	#while True:
	#	frame = cv.QueryFrame(capture)
	#	cv.ShowImage('Webcam', frame)

	#	k = cv.WaitKey(5) % 256

	#	if k % 256 == 27:
	#		break

              
