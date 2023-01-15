from wizAPI import *

class JadeOniFarmer(wizAPI):
    def __init__(self, handle=None):
        wizAPI.__init__(self, handle=None) 

    def clickObelisk(self):
        self.wait(1)
        self.press_key('x')
        self.wait(1)
        self.press_key(' ')
        self.wait(1)

    def centerFromObelisk(self):
        self.wait(1)
        self.hold_key('a', 0.31)

    def goToObelisk(self):
        self.hold_key('d', 0.1)
        self.hold_key('s', 7)
        self.hold_key('a', 0.397) 
        self.hold_key('w', 2.75)

    ''' Use it from the dungeon entrance'''
    def beforeFightMovement(self, inFight = False): 
        print('Moving to Oni')      
        if not inFight:
            self.hold_key('w', 3.3) # go to obelisk from entrance 
            self.clickObelisk() 
            self.centerFromObelisk() 
            self.hold_key('w', 9)

    def fightOni(self, inFight = True):
        print('Fighting Oni...')
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
            while not player.is_turn_to_play():
                if self.is_idle(): 
                    inFight = False
                    break 
                self.wait(0.5)

            end = time.time() 
            print('Done waiting')
            print(f"-- Spell round took {end - start} seconds -- ") 
    

if __name__ == "__main__":
    player = JadeOniFarmer().register_window()  
    start = time.time()

    COUNT = 0
    while True:
        player.enterDungeon()

        player.wait(15)

        player.beforeFightMovement()

        player.fightOni()
        
        player.exitDungeon()

        if player.checkBagFull():
            player.quickSell()
            player.closeBag()
            
        COUNT += 1
        player.use_potion_if_needed()
        end = time.time()
        elapsedMinutes = (end - start) / 60
        print(f"You have killed the Jade Oni {COUNT} times in {elapsedMinutes} minutes!")
        print(f"That is an average of {COUNT / elapsedMinutes} runs a minute!")