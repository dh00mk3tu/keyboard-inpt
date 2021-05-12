import pyautogui
import math
import time
import random 

while True:
# Radius 
    R = 500
    n = int(0.8)
    # measuring screen size
    (x,y) = pyautogui.size()
    # locating center of the screen 
    (X,Y) = pyautogui.position(x/2,y/2)
    # offsetting by radius 
    pyautogui.moveTo(X+R,Y)

    for i in range(360):
        time.sleep(random.randint(n, 2))
        # setting pace with a modulus 
        if i%6==0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))