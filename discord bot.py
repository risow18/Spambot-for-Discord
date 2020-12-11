from win32api import Sleep, GetAsyncKeyState
from keyboard import press_and_release
from pyperclip import copy
from sys import exit
from random import randint, seed
Sleep(2000)
run = 1
xree = input("Watcha spamming?: ")
copy(xree)
print("""
Have fun ;)
(you can click on Discord now. Press esc to stop the spam)
""")
while True:
    #seed()
    #copy(randint(1, 100))
    press_and_release("ctrl+v")
    press_and_release("enter")
    Sleep(1000)
    if GetAsyncKeyState(0x1B):
        exit()
            
