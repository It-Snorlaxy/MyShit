import pyautogui as pag
import time
import threading

def a():
    while True:
        time.sleep(2)
        pag.press('1')
        time.sleep(0.4)
        pag.press('1')
        time.sleep(0.4)
        pag.press('1')

def b():
    while True:
        time.sleep(0.4)
        pag.press('2')
        time.sleep(0.5)
        pag.press('2')
        time.sleep(0.4)
        pag.press('2')
        time.sleep(4)

def c():
    while True:
        time.sleep(0.4)
        pag.press('3')
        time.sleep(0.4)
        pag.press('3')
        time.sleep(0.4)
        pag.press('3')
        time.sleep(4)

def d():
    while True:
        time.sleep(0.4)
        pag.press('5')
        time.sleep(0.4)
        pag.press('5')
        time.sleep(0.4)
        pag.press('5')
        time.sleep(15)

threading.Thread(target=a).start()
threading.Thread(target=b).start()
threading.Thread(target=c).start()
threading.Thread(target=d).start()
