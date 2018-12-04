from tqdm import tqdm_gui
import tqdm
from random import random, randint
from time import sleep

for i in tqdm_gui(range(0,50)):
    #tqdm_gui.set_description()
    sleep(.03)

##t = tqdm.__init__(self, iterable=None, desc=None, total=None, leave=True, file=None, ncols=None, mininterval=0.1, maxinterval=10.0, miniters=None, ascii=None, disable=False, unit='it', unit_scale=False, dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0, position=None, postfix=None, unit_divisor=1000, gui=False, **kwargs)
