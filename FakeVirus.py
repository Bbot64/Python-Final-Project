from tkinter import *
from tkinter import messagebox

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import pygame.mixer, pygame.time
import time

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

mixer = pygame.mixer
mixer.init()
music = mixer.Sound("_____")  ##Insert specific wav file within here. Make sure the path to the file is correct.
music2 = mixer.Sound("_____")   ##Insert specific wav file within here. Make sure the path to the file is correct.

from TextToSpeech import voice

import ctypes
import os
SPI_SETDESKWALLPAPER = 20

from Brighness import brightnessChangeOld
import wmi
##---------------------------------------------------------
def changeVol(volume):
    vol = volume.GetMute()
    if vol:
        #muted
        volume.SetMute(0, None)
        volume.SetMasterVolumeLevel(-10.0, None)
    else:
        #not muted
        volume.SetMasterVolumeLevel(-10.0, None)

##---------------------------------------------------------

window = Tk()
window.withdraw()
window.lift()
messagebox.showinfo("Mistake1","You Shouldn't have done that", icon='warning')

changeVol(volume)

channel = music.play(loops = -1, maxtime = 0, fade_ms = 8000)
time.sleep(4)
voice('Prepare to get hacked.')
time.sleep(1)

ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0,b'C:\Users\Austen Brownfield\Desktop\Sophomore Semester1\Python\Final\Images\Skulls.jpg', 3)

messagebox.showinfo("Mist","Nice Background Image", icon = 'warning')

index = 0
while index < 400:
    brightnessChangeOld(index)
    index += 4
    
messagebox.showinfo("01100110","Downloading Files...", icon = 'warning')
time.sleep(1)

changeVol(volume)
volume.SetMasterVolumeLevel(-10.0, None)
voice('HA')
time.sleep(.05)
volume.SetMasterVolumeLevel(-5.0, None)
voice('HA')
time.sleep(.05)
volume.SetMasterVolumeLevel(0.0, None)
voice('HA')
volume.SetMasterVolumeLevel(-10.0, None)

messagebox.showinfo("01101000 01100001 01100011 01101011","Deleting Files...", icon = 'warning')

c = wmi.WMI(namespace = 'wmi')
methods = c.WmiMonitorBrightnessMethods()[0]
methods.WmiSetBrightness(0, 0)
time.sleep(2)

channel = music.stop()
messagebox.askyesno("01100100 01100101 01100001 01110100 01101000","Goodbye?", icon = "question")
time.sleep(3)

methods.WmiSetBrightness(100, 0)
changeVol(volume)
volume.SetMasterVolumeLevel(-10.0, None)
channel = music2.play(loops = -1, maxtime = 0, fade_ms = 4000)
messagebox.showinfo("Prank!","This was all a prank. No damage was done. Don't mess with unknown programs in the future.", icon = "info")
time.sleep(1)
voice('You just got pranked')

ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0,b'C:\Users\Austen Brownfield\Desktop\Sophomore Semester1\Python\Final\Images\Frank.jpg', 3)
messagebox.showinfo("End","Exit this box to end the music, and the program.", icon = "info")
channel = music2.stop()

ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0,b'C:\Users\Austen Brownfield\Desktop\Sophomore Semester1\Python\Final\Images\endScreen.jpg', 3)
