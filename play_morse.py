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

#Setup morse code dictionary
morse_code = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', '.':'.-.-.-', ',':'--..--', '?':'..--..', "'":'.----.', '!':'-.-.--', '/':'-..-.', '(': '-.--.', ')':'-.--.-', '&':'.-...', ':':'---...', ';':'-.-.-.', '=':'-...-', '+':'.-.-.', '-':'-....-', '_':'..--.-', '"':'.-..-.', '$':'...-..-', '@':'.--.-.', ' ': '/'}

#Setup song
morseShort = AudioSegment.from_mp3('/home/johaha/Desktop/morse_code/morseshort.mp3')
morseLong = AudioSegment.from_mp3('/home/johaha/Desktop/morse_code/morselong.mp3')

#Check if touch sensor has been triggered
while True:
    if GPIO.input(23) == GPIO.HIGH:
        play(morseShort)
        play(morseLong)