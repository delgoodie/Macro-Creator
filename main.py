import PySimpleGUI as sg
import pyautogui as bot
import pynput

# bot.PAUSE = 0.1

# for i in range(24):
#     bot.typewrite(",")
#     bot.press("down")
#     bot.press("left")


layout = [[sg.Button("Record"), sg.Button("Playback"), sg.Input("1", key="iterations", size=(10, 10))]]
window = sg.Window(title="Micrsoft Office Generator", layout=layout, margins=(20, 20))
recording = False
while True:
    event, values = window.read()

    if event == "Record" and values["iterations"]:
        print(values["iterations"])
    if event == sg.WIN_CLOSED:
        break
window.close()