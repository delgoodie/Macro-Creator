import PySimpleGUI as sg
import pyautogui as bot
from pynput.mouse import Listener as mouse
from pynput.keyboard import Key, Listener as keyboard

# bot.PAUSE = 0.1

# for i in range(24):
#     bot.typewrite(",")
#     bot.press("down")
#     bot.press("left")


def clickHandler(arg1, arg2, arg3, arg4):
    0


def keyPressHandler(key):
    key
    print(key)


def keyReleaseHandler(key):
    print(key)


layout = [[sg.Button("Record"), sg.Button("Playback"), sg.Input("1", key="iterations", size=(10, 10))]]
window = sg.Window(title="Micrsoft Office Generator", layout=layout, margins=(20, 20))
recording = False
while True:
    with mouse(on_click=clickHandler) as listener:
        listener.join()

    with keyboard(on_press=keyPressHandler, on_release=keyReleaseHandler) as listener:
        listener.join()

    event, values = window.read()

    if event == "Record" and values["iterations"]:
        print(values["iterations"])
    if event == sg.WIN_CLOSED:
        break
window.close()
