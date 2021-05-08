import os
import time
import pynput.keyboard as kb
import pyautogui
from utils import sleeper, merger
from model import counter
from pynput import mouse


class MyException(Exception): pass


print("Keys:\n Cmd - takes screenshot\n Right ctrl - end program\n Shift - creates pdf from taken shots")

keyboard = kb.Controller()

path = input("provide path where operations should be made: ")
#  TODO temporary - to delete
path = "/Users/pawel.szalawinski/Pictures/Shoots/"

print(">>Path recorded")
print(">>Provide coordinates:")

NumberOfMouseClicks = 0
coordinates = list()


def on_click(x, y, button, released):
    global NumberOfMouseClicks
    print(x, y)
    coordinates.append(x)
    coordinates.append(y)

    NumberOfMouseClicks += 1
    if (NumberOfMouseClicks == 8):
        raise MyException(button)


with mouse.Listener(on_click=on_click) as listener:
    try:
        listener.join()
    except MyException as e:
        pass

print("Coordinates: " + str(coordinates))
sleeper.print_dots()

licznik = counter.Counter(0, path, coordinates[0], coordinates[1], coordinates[4], coordinates[5], coordinates[8],
                          coordinates[9], coordinates[12], coordinates[13])

print(licznik.__dict__)

print("Ready to taking shots!")


def key_shooter(x, y, button, pressed):
    screen_shooter()


def add_counter(obj):
    licznik = obj.get_licz()
    counter2 = licznik + 1
    obj.set_licz(counter2)


def screen_shooter(licznik):
    # t = time.localtime()
    # timestamp = time.strftime('%b-%d-%Y_%H%M%S', t)
    click = licznik.get_licz()
    file_name = (str(click) + ".png")
    print("Shot taken: " + file_name)
    path = licznik.get_pth()
    savepath = path + file_name

    myScreenshot = pyautogui.screenshot(region=(licznik.get_txl(), licznik.get_tyl(), licznik.get_bxr(), licznik.get_byl()))
    myScreenshot.save(savepath)
    add_counter(licznik)


def exit():
    print("Bye bye")
    time.sleep(0.3)
    os._exit(0)


def on_press(key):
    if key == kb.Key.ctrl: exit()
    if key == kb.Key.cmd: screen_shooter(licznik)
    if key == kb.Key.shift: merger.createPdfFile(licznik)
    # if key == kb.Key.ctrl.a: listdir_nohidden('/Users/pawel.szalawinski/Pictures/Shoots/')


with kb.Listener(
        on_press=on_press) as listener:
    listener.join()
