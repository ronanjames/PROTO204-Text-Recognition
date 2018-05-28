#	Tested with python2.7 on raspberry PI 3 the 21/05/2018
#	Tested with Python2.7 on Ubuntu the 19 mai 2018
#	When the button is pressed it opens a picture file ("f1.jpg") and then speak it using google speech engine
#
#	$sudo pip2 install pytesseract
#	$sudo apt-get install tesseract-ocr
#	$pip instal SpeechRecognition
#	$sudo pip install gTTS
#	install pa_stable_v190600_20161030.tgz : ./configure && sudo make install
#	install PyAudio-0.2.11.tar.gz : sudo python setup.py install
#
#	$jackd -r -d alsa 44100

import cv2
import os
import time
import numpy as np
import pytesseract
import picamera
from gtts import gTTS
from PIL import Image
import RPi.GPIO as GPIO

############################################################################
def get_string(img_path):

    # Read image
  with picamera.PiCamera() as camera:
    camera.resolution = (1024, 720)
    camera.capture("f1.jpg")   
    print("picture taken.")

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(img_path))
    return result
  

############################################################################
def read_picture():
    print ('--- Start recognize text from image ---')

    result1=get_string("f1.jpg")

    print (result1)
    time.sleep(1)

    tts = gTTS(text=result1 , lang='en')
    tts.save("result.mp3")
    os.system("mpg123 result.mp3")

    print ("------ Done -------")

############################################################################
if __name__ == "__main__":

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    while 1:
        bouton = GPIO.input(3)
        if bouton==0 :
            print("Button was pushed")
            read_picture()
            time.sleep(1)
        else:
            time.sleep(1)
    
