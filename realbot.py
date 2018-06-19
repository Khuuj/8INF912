from time import sleep
import traceback

from  live_parser import LiveLogParser
import live_utils as ut

# globalGameOn = False
# globalBotHP = -1
# globalBotArmor = 0
# globalOpponentHP = -1
# globalOpponentArmor = 0
# globalManaTotal = 1
# globalManaAvailable = 1
# globalFriendlyCreaturesOnBoard = [False, False,False,False,False,False,False]
# globalFriendlyCreaturesAtk = [0,0,0,0,0,0,0,0]
# globalFriendlyCreaturesHP = [0,0,0,0,0,0,0,0]
# globalFriendlyCreautresId = []
# globalOpponentCreaturesOnBoard = [False, False,False,False,False,False,False]
# globalOpponentCreaturesAtk = [0,0,0,0,0,0,0,0]
# globalOpponentCreaturesHP = [0,0,0,0,0,0,0,0]
# globalOpponentCreautresId = []
# globalIsFirstPlayer = True
# globalCardsInDeckCount = 30
# globalCardsInHandCount = 0
# globalCardsInHandId = []
# globalOptions = []
# globalGameState = "none" #lose/win



def main():
    try:
        file = 'E:\Battle.net\Hearthstone\Logs\Power.log'
        liveParser = LiveLogParser(file)
        liveParser.start()

        while True:
            sleep(1)
            ## calls the bot here
            ## voir methode_perso.txt (on met les rewards a jour en meme temps)
            ## pour mettre à jour l'état accessible par l'action, 
            ##                  si action == fin du tour meme etat (on boucle) [pour l'instant]
            ##                  sinon mettre a jour l'état des qu'une action nouvelle action est proposée en gardant une variable majWaiting=true
            ##                  cas special si majNotDone = true et game=win ET hpopponent<=0 mettre recompense à 100 et ajouter etat win aux etats accessibles
        
    except:
        print(traceback.format_exc())
        liveParser.stop()
    
    
if __name__ == "__main__":
    main()
