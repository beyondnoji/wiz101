from JadeOni import *

class RaFarmer(JadeOniFarmer):
    def __init__(self, handle = None):
        JadeOniFarmer.__init__(self, handle = None) 
    
    def backAndForth(self):
        self.hold_key('s', 1) 
        self.hold_key('w', 1)

    def goToRa(self):
        print('Opening the key room...')
        self.hold_key('w', 3)
        self.press_key('x')
        self.wait(0.5)
        self.backAndForth()
        self.wait(5)
        print('Going to Ra...')
        self.hold_key('w', 6)

    def fightRa(self, inFight = True):
        print('Fighting Ra...')
        roundCount = 0
        enchCount = 0
        self.wait(2)
        while inFight:
            roundCount += 1
            print(f"--------ROUND {roundCount}--------") 

            while type(self.find_spell('epic')) == tuple and type(self.find_spell('meteor-strike')) == tuple and enchCount < 4:
                self.enchant('meteor-strike', 'epic')
                enchCount += 1
                if enchCount >= 4:
                    break

            if self.find_spell('meteor-strike-enchanted'):
                self.cast_spell('meteor-strike-enchanted')
            else:
                self.pass_turn()

            start = time.time() 
            print('Waiting..') 
            while not self.is_turn_to_play():
                if self.is_idle() or not (pyautogui.locateOnScreen('RaDialogue.png') == None): 
                    inFight = False
                    break 
                self.wait(0.5)

            end = time.time() 
            print('Done waiting')
            print(f"-- Spell round took {end - start} seconds -- ") 

    def skipDialogue(self):
        self.press_key(' ')
        self.wait(0.5)
        self.press_key(' ')
    
    def leaveReadingRoom(self):
        print('Leaving reading room...') 
        self.hold_key('w', 1)
        self.hold_key('a', 0.75)
        self.hold_key('w', 11)

if __name__ == "__main__":
    player = RaFarmer().register_window() 
    start = time.time() 
    while True:
        player.enterDungeon() 
        player.wait(15)
        player.goToRa() 
        player.fightRa()
        player.skipDialogue()
        player.leaveReadingRoom()