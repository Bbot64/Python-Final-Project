import pygame.mixer, pygame.time
import time
mixer = pygame.mixer

mixer.init()

sound = mixer.Sound("that one wind sound from undertale (tm).wav")
#channel = sound.play()
#channel = sound.play(loops = -1) This will make the audio loop indefinitely
##
##while channel.get_busy():
##    pygame.time.wait(100)
##    print("Playing...")
##print("finished")

channel = sound.play(loops = -1, maxtime = 0, fade_ms = 10000)
time.sleep(5)
channel = sound.stop()
