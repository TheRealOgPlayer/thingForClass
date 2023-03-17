import pyautogui
import time


startApplication = input('Start: ')
distance = 500
duration = 0.0002
counter = 4

#pyautogui.moveTo(52, 298 )

def drawer(distanceTwo):
    pyautogui.drag(distanceTwo, 0, duration)   # move right
    distanceTwo -= 5
    pyautogui.drag(0, distanceTwo, duration)   # move down
    pyautogui.drag(-distanceTwo, 0, duration)  # move left
    distanceTwo -= 5
    pyautogui.drag(0, -distanceTwo, duration)  # move up
    return distanceTwo
    

while distance >= 0:
    if startApplication.upper() == "Y" and counter <= 0:
        distance = drawer(distance)
    elif counter >= 0:
        time.sleep(1)
        counter = counter - 1 
        print("Time Remaing: ", counter)
