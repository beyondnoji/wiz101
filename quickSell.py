from JadeOni import * 

player = JadeOniFarmer().register_window()

player.set_active()
player.wait(1)

print(pyautogui.pixel(27, 573))
print(pyautogui.pixel(90, 600))
print(player.is_health_low())
print(player.is_mana_low())
