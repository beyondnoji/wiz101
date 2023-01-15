from JadeOni import * 

player = JadeOniFarmer().register_window()
SPEED = 0.1
while True: 
    count = 0
    while pyautogui.locateOnScreen('empower.png', region = (290, 230, 220, 220), confidence=0.8) == None: # while no empower on screen 
        player.click(580, 485, speed = SPEED) # check next tab 
        count += 1 # add to count 
        if count > 8: # after 8 tries refresh 
            player.click(428, 176, speed = SPEED)
            count = 0


    x, y  = pyautogui.locateCenterOnScreen('empower.png', region = (290, 230, 220, 220), confidence=0.8)
    player.click(x, y, speed = SPEED)
    player.click(193, 513, speed = SPEED) # click "Buy More"
    player.click(493, 385, speed = SPEED) # select all of them 
    player.click(320, 500, speed = SPEED) # Click buy

    # Select OK twice 
    player.click(514, 399, speed = SPEED)
    player.click(514, 399, speed = SPEED)
