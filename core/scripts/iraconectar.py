
import pyautogui
import pydirectinput

    
def conectar():
        try: 
            pydirectinput.moveTo(237, 968) # Move the mouse to the x, y coordinates 100, 150.
            pydirectinput.click()
            pydirectinput.moveTo(1244,601) # Click the mouse at its current location.
            pydirectinput.click() # Click the mouse at the x, y coordinates 200, 220.

        except: pass
    