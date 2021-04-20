import random,time
from pynput.keyboard import Controller

keyboard = Controller()

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def type_string_with_delay():
    for character in alphabet_list:
        keyboard.type(random.choice(alphabet_list))
        delay = random.uniform(0, 2)
        time.sleep(1.7)  

type_string_with_delay()
