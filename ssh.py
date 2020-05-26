import os
import pyautogui
import win32gui
import cv2
import autopy
import numpy as np
import time
import sys
import webbrowser

def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst

def click_on(pos):#pos = [x y]
    autopy.mouse.move(pos[0],pos[1])
    autopy.mouse.click()
    return 1


def open_SSH(dir):
    os.startfile('C:\\file_path\PuTTy')
    time.sleep(1) 
    #whnd = win32gui.FindWindow(0, 'PuTTy Configuration')
    pyautogui.write('ip_of_device_to_ssh_to')
    print("scanning for open button")    
    autopy.bitmap.capture_screen().save('screengrab.png')
    img_rgb = cv2.imread('screengrab.png')
    template = cv2.imread('open.png')
    w, h = template.shape[:-1]
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .71
    loc = np.where( res >= threshold)
    print(loc)
    print("loc 0")
    print(loc[0][0])
    print(loc[1][0])
    pos = loc[1][0]+10,loc[0][0]+10    #the regular amount is just slightly off for some reason
    click_on(pos)
    time.sleep(1) 
    pyautogui.write('username')
    pyautogui.press('enter')
    pyautogui.write('passwd')
    pyautogui.press('enter')
    time.sleep(1) 
    pyautogui.write('cd '+dir)
    pyautogui.press('enter')


#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))
#for directory in sys.argv[1:] :
open_SSH("path_to_desired_directory")
os.startfile('C:\\file_path\idea64.exe')

example = 'https://example.com/'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\\file_path\chrome.exe"))
webbrowser.get('chrome').open(example)
