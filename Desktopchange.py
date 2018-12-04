import ctypes
import os
SPI_SETDESKWALLPAPER = 20

ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0,b'C:\Users\Austen Brownfield\Desktop\Sophomore Semester1\Python\Final\Images\Skulls.jpg', 3)
