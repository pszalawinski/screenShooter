import os
import time
import pynput.keyboard as kb
import pyautogui
from utils import sleeper, merger
from model import counter, pyguiposition
from pynput import mouse


class MyException(Exception): pass


print("Controls: Keys:\n Cmd - takes screenshot\n "
      "Right ctrl - ends program\n Shift - creates pdf from taken shots"
      " \nAvailable after providing necessary data")

keyboard = kb.Controller()

path = input("provide path where operations should be made: ")

print(">>Path recorded: " + str(path))
print("size of your main screen: ")
print(pyautogui.size())

print("Click in left top corner and then in right bottom corner of desired screen area:")

NumberOfMouseClicks = 0
coordinates = list()


def on_click(x, y, button, pressed):
    global NumberOfMouseClicks

    coordinates.append(pyautogui.position().x)
    coordinates.append(pyautogui.position().y)

    NumberOfMouseClicks += 1
    if NumberOfMouseClicks == 4:
        raise MyException(button)


with mouse.Listener(on_click=on_click) as listener:
    try:
        listener.join()
    except MyException as e:
        pass

counterHolder = counter.Counter(0, path)
positions = pyguiposition.ClickPositions(coordinates[0], coordinates[1], coordinates[4], coordinates[5])
sleeper.print_dots()
print("Positions provided and saved")

print("Ready to taking shots!")


def add_counter(obj):
    counterHolder = obj.get_licz()
    counter2 = counterHolder + 1
    obj.set_licz(counter2)


def screen_shooter(licznik):
    click = counterHolder.get_licz()
    file_name = (str(click) + ".png")
    print("Shot taken: " + file_name)
    path = counterHolder.get_pth()
    savepath = path + file_name

    myScreenshot = pyautogui.screenshot(
        region=(
            int(positions.get_pos1x()), int(positions.get_pos1y()),
            int(positions.get_pos2x()) - int(positions.get_pos1x()),
            int(positions.get_pos2y()) - int(positions.get_pos1y())))

    myScreenshot.save(savepath)
    add_counter(licznik)


def exit():
    print("Bye bye")
    time.sleep(0.3)
    os._exit(0)


def on_press(key):
    if key == kb.Key.ctrl: exit()
    if key == kb.Key.cmd: screen_shooter(counterHolder)
    if key == kb.Key.shift: merger.createPdfFile(counterHolder)


with kb.Listener(
        on_press=on_press) as listener:
    listener.join()
