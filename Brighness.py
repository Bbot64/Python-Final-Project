"""This program adjusts the brightness of the monitor. Right now, there is a loop, which makes the screen's brightness go from 0 to 100, 4 times.
This program does not check what the operating system is. Look into it?
https://www.reddit.com/r/learnpython/comments/3ikewf/setting_screen_brightness_in_windows/
above is URL for where I learned what to do."""
import wmi

def brightnessChangeOld(x):
    while x > 100:
        x = x - 100
    c = wmi.WMI(namespace = 'wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(x, 0)

def brightnessChange(numIterations = 6, amtIncrease = 1):
    c = wmi.WMI(namespace = 'wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    maxNum = 100 * numIterations
    index, num = 0, 0
    if amtIncrease < 1:
        raise Exception('Value should increase by atleast 1.')
    while index < maxNum:
        if num > 100:
            num = num - 100
        methods.WmiSetBrightness(num, 0)
        index += amtIncrease
        num += amtIncrease
    
#installed pywin32 and WMI
