import random,time
from pynput.keyboard import Controller

keyboard = Controller()

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def type_string_with_delay():
    while True: 
        for character in alphabet_list:
            keyboard.type(random.choice(alphabet_list))
            delay = randomkb.uniform(0, 2)
            time.sleep(.3)
        
        
type_string_with_delay()
