import PySimpleGUI as sg
import pyautogui as bot
from pynput.mouse import Listener as mouse
from pynput.keyboard import Key, Listener as keyboard

recording = False
actionQueue = []


class Action:
    def __init__(self, _type: str, _data: tuple):
        self.type = _type
        self.data = _data


def clickHandler(x, y, button, arg4):
    if recording and arg4:
        actionQueue.append(Action("click", bot.position()))


def keyPressHandler(key):
    if recording:
        if type(key) is Key:
            actionQueue.append(Action("key", (key.name, "down")))
        else:
            actionQueue.append(Action("key", (key.char, "down")))


def keyReleaseHandler(key):
    if recording:
        if type(key) is Key:
            actionQueue.append(Action("key", (key.name, "up")))
        else:
            actionQueue.append(Action("key", (key.char, "up")))


mListener = mouse(on_click=clickHandler)
mListener.start()

kListener = keyboard(on_press=keyPressHandler, on_release=keyReleaseHandler)
kListener.start()

layout = [[sg.Text("IDLE", key="status"), sg.Button("Record"), sg.Button("Playback"), sg.Input("1", key="iterations", size=(10, 10))]]
window = sg.Window(title="Micrsoft Office Generator", layout=layout, margins=(20, 20))
while True:
    event, values = window.read()

    if event == "Record":
        if not recording:
            actionQueue = []
            recording = True
            window.FindElement("status").update("REC")
        else:
            recording = False
            window.FindElement("status").update("IDLE")
    elif event == "Playback":
        window.FindElement("status").update("PLAY")
        actionQueue = actionQueue[0 : len(actionQueue) - 2]
        startingPos = bot.position()
        bot.PAUSE = 0.03
        for i in range(int(values["iterations"])):
            print("iting")
            for a in actionQueue:
                if a.type == "click":
                    bot.click(a.data[0], a.data[1], duration=0.1)
                elif a.type == "key":
                    k = a.data[0]
                    if "alt" in k:
                        k = "alt"
                    if "ctrl" in k:
                        k = "ctrl"
                    if len(k) == 1 and ord(k) < 65:
                        k = chr(ord(k) + 96)
                    print(k)
                    if a.data[1] == "down":
                        bot.keyDown(k)
                    elif a.data[1] == "up":
                        bot.keyUp(k)
        bot.moveTo(startingPos)
        window.FindElement("status").update("IDLE")
    elif event == sg.WIN_CLOSED:
        break
window.close()