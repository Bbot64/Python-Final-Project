from Brighness import brightnessChange
from Brighness import brightnessChangeOld
from TextToSpeech import voice


index = 0
while index < 600:
    brightnessChangeOld(index)
    index += 8
    print(index)
    ##OLD! Don't use

##voice('Test')
    ##WORKS!

brightnessChange(1,1)
    ##Works!


