from JadeOni import * 
import pyautogui

player = JadeOniFarmer().register_window()
player.set_active()
player.wait(1)
im = pyautogui.screenshot(region = (290, 230, 220, 220))
im.save('img.png')