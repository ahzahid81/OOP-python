import pyautogui

def pyramid(row):
    for i in range(1,row+1):
        pyautogui.typewrite("#" * i)
        pyautogui.typewrite("\n")


rows = int(input())
pyramid(rows)