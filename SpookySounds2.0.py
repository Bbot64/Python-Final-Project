import pygame.mixer, pygame.time
from tkinter import *
from tkinter import messagebox
import time

Cont = True

mixer = pygame.mixer
mixer.init()
music = mixer.Sound("that one wind sound from undertale (tm).wav")

while Cont:
    channel = music.play()
    print("Would you like the music to stop?")

    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    result = messagebox.askyesno("Question", "Would you like the music to stop?", icon = 'warning')
    if result == True:
        print("Sure!")
        channel = music.fadeout(3000)
        Cont = False
    else:
        print("You'll change your mind.")
        time.sleep(3)
    continue
