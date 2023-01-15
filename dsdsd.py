from wizAPI import *
import pyautogui 
class JadeOniFarmer(wizAPI):
    def __init__(self, handle=None):
        wizAPI.__init__(self, handle=None) 

    def clickObelisk(self):
        self.wait(0.5)
        self.press_key('x')
        self.wait(0.5)
        self.press_key(' ')
        self.wait(0.25)

    def centerFromObelisk(self):
        self.wait(0.5)
        self.hold_key('a', 0.3)

    def goToObelisk(self):
        self.hold_key('d', 0.1)
        self.hold_key('s', 7)
        self.hold_key('a', 0.397) 
        self.hold_key('w', 2.75)

    ''' Use it from the dungeon entrance'''
    def beforeFightMovement(self, inFight = False): 
        if not inFight:
            self.hold_key('w', 3.3) # go to obelisk from entrance 
            self.clickObelisk() 
            self.centerFromObelisk() 
            #self.hold_key('w', 9)

    def fightOni(self,   inFight = True):
        self.wait(2)
        while not self.is_idle():
            while type(self.find_spell('epic')) == tuple and type(self.find_spell('meteor-strike')) == tuple:
                self.enchant('meteor-strike', 'epic')

            if self.find_spell('meteor-strike-enchanted'):
                self.cast_spell('meteor-strike-enchanted')
            else:
                self.pass_turn()

            self.wait_for_end_of_round()
            
    def enterDungeon(self):
        self.hold_key('s', 1)
        self.wait(0.25)
        self.press_key('x')

    def exitDungeon(self):
        self.hold_key('a', 0.725)
        self.hold_key('w', 10.5)
        self.wait(2)


player = JadeOniFarmer().register_window()
player.set_active()

player.exitDungeon()