import os
import subprocess as sp

paths = {
    'notepad': "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad.exe",
    'discord': "C:\\Users\\user\\AppData\\Local\\Discord\\app-1.0.9175\\Discord.exe",
    'chrome': "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_chrome():
    os.startfile(paths['chrome'])

def open_calculator():
    sp.Popen(paths['calculator'])
