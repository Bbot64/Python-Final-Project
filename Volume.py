from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

from tkinter import *
from tkinter import messagebox

volume.GetMute()
volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(-0.0, None)
volume.GetVolumeRange()

vol = volume.GetMute()
if vol:
    print("Muted")
    volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(-10.0, None)
else:
    print("Not muted")
    #volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(-10.0, None)



window = Tk()
window.withdraw()
window.lift()
messagebox.showinfo("Mistake","You Shouldn't have done that", icon='warning')



##Code found https://github.com/AndreMiras/pycaw
