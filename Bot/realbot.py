from time import sleep
import traceback

from  import LiveLogParser

globalGameOn = False
globalBotHP = -1
globalBotArmor = 0
globalOpponentHP = -1
globalOpponentArmor = 0
globalManaTotal = 1
globalManaAvailable = 1
globalFriendlyCreaturesOnBoard = [False, False,False,False,False,False,False]
globalFriendlyCreaturesAtk = [0,0,0,0,0,0,0,0]
globalFriendlyCreaturesHP = [0,0,0,0,0,0,0,0]
globalFriendlyCreautresId = []
globalOpponentCreaturesOnBoard = [False, False,False,False,False,False,False]
globalOpponentCreaturesAtk = [0,0,0,0,0,0,0,0]
globalOpponentCreaturesHP = [0,0,0,0,0,0,0,0]
globalOpponentCreautresId = []
globalIsFirstPlayer = True
globalCardsInDeckCount = 30
globalCardsInHandCount = 0
globalCardsInHandId = []
globalOptions = []
globalGameState = "none" #lose/win

def main():
    try:
        file = 'E:\Battle.net\Hearthstone\Logs\Power.log'
        liveParser = LiveLogParser(file)
        liveParser.start()
        
        while True:
            sleep(1)
        
    except:
        print(traceback.format_exc())
        liveParser.stop()
    
    
if __name__ == "__main__":
    main()