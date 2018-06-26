from time import sleep
import traceback

from  live_parser import LiveLogParser
import live_utils as utils
import json
import numpy as np
import pyautogui as ptg



#utils.globalQ = {}
#utils.globalR = {}
#utils.globalMajWaiting =False
#utils.globalActionWaiting = []
#utils.globalStateWaiting = []

def choose_action():

#    global utils.globalMajWaiting
#    global utils.globalActionWaiting
#    global utils.globalStateWaiting

    utils.globalMajWaiting = False

    gamma = 0.8 #affect l'influence des actions futures

    available_actions = utils.globalOptionsInfos
    cards_ids_actions = utils.globalActionsInfos
    actions_rewards = []
    print(available_actions)


    state = [utils.globalBotManaTotal, utils.globalBotManaAvailable, utils.globalBotHP, utils.globalOpponentHP, utils.globalFriendlyCreaturesInfos, utils.globalOpponentCreaturesInfos]
    stringState =  str(state)

    print(stringState)

    #add state with empty action_list
    if not utils.globalR.__contains__(stringState):
        utils.globalQ[stringState] = {}
        utils.globalR[stringState] = {}


    #print(utils.globalQ)
    for action in cards_ids_actions:
        strAction = str(action)
        nextState = ""
        new_reward = 5

        #cas action = fin de tour
        if action == []:
            new_reward = 1 #discrimine le fin de tour (pour explorer) ; pas 0 pour permettre d'être sélectionnée
            nextState = stringState

        if not utils.globalR[stringState].__contains__(strAction):
            utils.globalQ[stringState][strAction] = [0,nextState]
            utils.globalR[stringState][strAction] = [new_reward,nextState]

            actions_rewards.append(5)

        else:

            "print(utils.globalQ)"
            max = 0
            if utils.globalR[stringState][strAction][1] != "":
                for x in utils.globalQ[utils.globalR[stringState][strAction][1]]:
                    print(x)
                    if utils.globalQ[utils.globalR[stringState][strAction][1]][x][0] > max:
                        max = utils.globalQ[utils.globalR[stringState][strAction][1]][x][0]


            #Idée pour favoriser l'exploration : si une action n'a pas d'état suivant connu: doubler sa valeur (reward)
            reward = utils.globalR[stringState][strAction][0] + gamma*max
            utils.globalQ[stringState][strAction][0] = reward
            actions_rewards.append(reward)


    np_actions_rewards = np.asarray(actions_rewards)

#    #choisi l'acction avec la récompense max
#    actions_rewards_max = np.where(np_actions_rewards == np.max(np_actions_rewards))[0]
#
#    index = actions_rewards_max[0]
#
#    if np.size(actions_rewards_max)>1:
#        index = np.random.choice(actions_rewards_max)


    #choisi l'action de maniere probabiliste pondérée
    actions_sum = np.sum(np_actions_rewards)
    actions_probabilities = np.zeros(len(np_actions_rewards))
    for i in range (0, len(np_actions_rewards)):
        actions_probabilities[i] = np.sum(np_actions_rewards[0:i+1])/actions_sum

    random_value = np.random.uniform(0,1)
    index = 0
    while actions_probabilities[index] < random_value:
        index += 1


    if nextState!=stringState:
        if utils.globalR[stringState][str(cards_ids_actions[index])][1] == "":
            utils.globalStateWaiting = stringState
            utils.globalActionWaiting =str(cards_ids_actions[index])
            utils.globalMajWaiting = True

    #useless
    else:
        utils.globalMajWaiting = False

    args = [None, None, None, None]
    

    for i in range(0,len(available_actions[index])):
        args[i] = available_actions[index][i]

    utils.choiceToMake = False

    if (args[0] == "hand"):
        if (args[1] < 5) & (utils.globalCoin != 0):
            utils.globalCoin.tags['GameTag.ZONE_POSITION'] -=1

    utils.globalEndTurnListed = False

    print("action:", args)
    utils.play_option(args[0], args[1],args[2],args[3])

    
    




def main():
    try:
        file = 'E:\Battle.net\Hearthstone\Logs\Power.log'
        
        #global utils.globalQ
        #global utils.globalR

        with open('q.json') as qfile:  
            utils.globalQ = json.load(qfile)

        with open('r.json') as rfile:
            utils.globalR = json.load(rfile)
        
        liveParser = LiveLogParser(file)
        liveParser.start()

        while True:
            sleep(1)

            can_play = False
            im = ptg.screenshot()

            #pixel_confirm = im.getpixel(966, 876)
            #if pixel_confirm == ()

            yellow_endturn = im.getpixel((1561, 476))
            green_endturn = im.getpixel((1556, 507))

            print(yellow_endturn)
            print(green_endturn)

            if ( (green_endturn[2] < 10) | (yellow_endturn[2] < 10) ) :
                can_play = True

            print(utils.globalEndTurnListed)
            print(can_play)

            if can_play & utils.globalEndTurnListed:
                sleep(7)
                print("chosing action")
                choose_action()


            #"""print(utils.globalGameStarted, utils.globalMouseMoving)
            #if utils.globalGameStarted & (not utils.globalMouseMoving) & utils.globalChoiceToMake:
            #    if utils.globalOpponentIsplayingHisTurn:
            #        sleep(30)
            #    print("chosing action")
#
            #    choose_action()
            #    utils.globalOpponentIsplayingHisTurn = False"""



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
