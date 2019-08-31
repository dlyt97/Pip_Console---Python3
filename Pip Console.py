#Default path - c:\\py37

x=input('1-install or 2-unistall:')

from pynput.keyboard import Key,Controller                
import time
keyboard=Controller()

vreme=1/2
def cmd():
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(vreme)
    keyboard.type('cmd')
    time.sleep(vreme)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(vreme)
    keyboard.type('cd\\')
    time.sleep(vreme)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(vreme)
    keyboard.type('cd py37\\scripts')
    time.sleep(vreme)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

if x == '1':
    install=input('Module? : ')
    cmd()
    time.sleep(vreme)
    keyboard.type('pip install '+install)
    time.sleep(vreme)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
elif x == '2':
    unistall=input('Module? : ')
    cmd()
    time.sleep(vreme)
    keyboard.type('pip unistall '+unistall)
    time.sleep(vreme)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
else:
    quit()



