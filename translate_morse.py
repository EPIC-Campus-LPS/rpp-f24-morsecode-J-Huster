#Import nessesarylibraries
from pydub import AudioSegment
from pydub.playback import play

#Setup morse code dictionary
morse_code = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', '.':'.-.-.-', ',':'--..--', '?':'..--..', "'":'.----.', '!':'-.-.--', '/':'-..-.', '(': '-.--.', ')':'-.--.-', '&':'.-...', ':':'---...', ';':'-.-.-.', '=':'-...-', '+':'.-.-.', '-':'-....-', '_':'..--.-', '"':'.-..-.', '$':'...-..-', '@':'.--.-.', ' ': '/'}

#Setup song
morseShort = AudioSegment.from_mp3('/home/johaha/Desktop/morse_code/morseshort.mp3')
morseLong = AudioSegment.from_mp3('/home/johaha/Desktop/morse_code/morselong.mp3')

def translate():
    word = input("Enter message: ")
    #Make any letters in user iput uppercase
    word = word.upper()
    for w in word:
        if w in morse_code:
            for m in morse_code[w]:
                if m == '.':
                    play(morseShort)
                elif m == '-':
                    play(morseLong)

#Check if touch sensor has been triggered
translate()