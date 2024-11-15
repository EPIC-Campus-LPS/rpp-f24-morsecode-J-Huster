#Import nessesarylibraries
import RPi.GPIO as GPIO
import time
from pydub import AudioSegment
from pydub.playback import play
import tm1637

#Set up touch module
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Setup song
song = AudioSegment.from_wav('/home/johaha/Desktop/play_sound_folder/music5.wav')

#Check if touch sensor has been triggered
while True:
    if GPIO.input(23) == GPIO.HIGH:
        play(song)
