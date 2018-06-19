import pyautogui as ptg 
import numpy as np
from hearthstone.enums import GameTag


globalGameOn = False
globalBotHP = 30
globalBaseBotHP = 30
globalBotArmor = 0
globalOpponentHP = 30
globalBaseOpponentHP = 30
globalOpponentArmor = 0
globalBotManaTotal = 1
globalBotManaAvailable = 1
globalBotSecretCount = 0
globalOpponentSecretCount = 0
globalFriendlyCreaturesOnBoard = [False, False,False,False,False,False,False]
globalFriendlyCreaturesAtk = [-1,-1,-1,-1,-1,-1,-1,-1]
globalFriendlyCreaturesHP = [-1,-1,-1,-1,-1,-1,-1,-1]
globalFriendlyCreautresId = []
globalFriendlyCreaturesOnBoardCount = 0
globalOpponentCreaturesOnBoard = [False, False,False,False,False,False,False]
globalOpponentCreaturesAtk = [-1,-1,-1,-1,-1,-1,-1,-1]
globalOpponentCreaturesHP = [-1,-1,-1,-1,-1,-1,-1,-1]
globalOpponentCreautresId = []
globalOpponentCreaturesOnBoardCount = 0
globalIsFirstPlayer = True
globalCardsInDeckCount = 30
globalCardsInHandCount = 0
globalCardsInHandId = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,]
globalOptions = []
globalGameState = "none" #lose/win
globalLine = 0
globalCurrentOption = -1
globalOptionsInfos =[]
globalOptionsCardIds = []
globalCurrentOptionsRewards =[]
globalLastLine = ""


#mouse coordinates

globalPosEndTurn = [1572, 495]
globalPosBotHero_Confirm = [961, 843]
globalPosHeroPower = [1147, 828]
globalPosOpponentHero = [969, 191]
globalPosCenter = [960, 540]

#pos for a two choice situation
globalPosDoubleChoice = {
	1: (713, 520), #left choice
	2: (1189, 504), # right choice
}


#pos for a three choice situation
globalPosTripleChoice = {
	1 : (623, 507), #left choice
	2 : (966, 504), # middle choice
	3 : (1322, 510), #right choice
}

#pos for a four choice situation
globalPosQuadrupleChoice = {
	1 : (584, 484), #left most choice
	2 : (831, 498), # middle left choice
	3 : (1084, 502), #middle right choice
	4 : (1342, 493)#right most choice
}

#B1-B13 = all board positions on bot side
globalPosBotBoard = {
    1 :(590, 597),
    2 :(640, 590),
    3 :(710, 605),
    4 :(768, 584),
    5 :(837, 612),
    6 :(893,579),
    7 :(967, 613),
    8 :(1027, 585),
    9 :(1085, 592),
    10 :(1150, 584),
    11 :(1218, 603),
    12 :(1277, 608),
    13 :(1342, 592)
}

#E1-E13 = all board positions on opponent side
globalPosEnemyBoard = {
    1 :(590, 397),
    2 :(640, 397),
    3 :(710, 397),
    4 :(768, 397),
    5 :(837, 397),
    6 :(893,397),
    7 :(967, 397),
    8 :(1027, 397),
    9 :(1085, 397),
    10 :(1150, 397),
    11 :(1218, 397),
    12 :(1277, 397),
    13 :(1342, 397)
}

#h1-h10 = all hand positions on bot side
globalPosHand = {
	1:{
		1: (949, 1007),
	},
	2:{
		1: (851, 985),
		2: (999, 1000),
	},
	3:{
		1: (783, 997),
		2: (920, 991),
		3: (1057, 994),
	},
	4:{
		1 :(733, 1053),
		2 :(854, 1003),
		3 :(994, 1032),
		4 :(1125, 997),
	},
	5:{
		1 :(688, 1023),
		2 :(791, 998),
		3 :(924, 1001),
		4 :(1016, 1032),
		5 :(1100, 1009),
	},
	6:{
		1 : (681, 1039),
		2 : (748, 1040),
		3 : (872, 996),
		4 : (920, 1006),
		5 : (1043, 1018),
		6 : (1142, 1041),
	},
	7:{
		1 : (661, 1034),
		2 : (745, 988),
		3 : (824, 995),
		4 : (877, 997),
		5 : (968, 989),
		6 : (1045, 1011),
		7 : (1173, 1050),
	},
	8:{
		1 : (647, 1044),
		2 : (727, 1031),
		3 : (779, 1026),
		4 : (866, 995),
		5 : (927, 971),
		6 : (996, 994),
		7 : (1066, 992),
		8 : (1182, 1055),
	},
	9:{
		1 : (624, 1038),
		2 : (716, 1008),
		3 : (766, 1025),
		4 : (835, 984),
		5 : (876, 993),
		6 : (961, 1001),
		7 : (1025, 1027),
		8 : (1089, 1044),
		9 : (1165, 1047),
	},
	10: {
	    1 :(626, 1022),
		2 :(686, 1034),
		3 :(760, 1033),
		4 :(812, 996),
		5 :(831, 974),
		6 :(909, 974),
		7 :(973, 986),
		8 :(1047, 972),
		9 :(1078, 1042),
		10 :(1182, 1020)
	}
}


def align(text, size, char=" "):
	"""
		Format text to fit into a predefined amount of space

		Positive size aligns text to the left
		Negative size aligns text to the right
	"""
	text = str(text).strip()
	text_len = len(text)
	if text_len > abs(size):
		text = f"{text[:size-3]}..."
	offset = "".join(char * (abs(size) - text_len))
	if size < 0:
		return f"{offset}{text}"
	else:
		return f"{text}{offset}"


def color():
	def color_decorator(func):
		colors = {
			"LivePlayer": 93,
			"red": 31,
			"green": 32,
			"LiveGame": 33,
			"blue": 34,
			"purple": 35,
			"cyan": 36,
			"grey": 37,
		}

		def func_wrapper(msg_type, obj, *args):
			class_name = obj.__class__.__name__
			color_key = class_name if class_name in colors else "green"
			line = "{}".format(func(msg_type, obj, *args))
			print(line)

		return func_wrapper

	return color_decorator


@color()
def terminal_output(msg_type, obj, attr=None, value=None):
	global globalGameOn
	global globalBotHP
	global globalBaseBotHP
	global globalBotArmor
	global globalOpponentHP
	global globalBaseOpponentHP
	global globalOpponentArmor
	global globalBotManaTotal
	global globalBotManaAvailable
	global globalFriendlyCreaturesOnBoard
	global globalFriendlyCreaturesAtk
	global globalFriendlyCreaturesHP
	global globalFriendlyCreautresId
	global globalFriendlyCreaturesOnBoardCount
	global globalOpponentCreaturesOnBoard
	global globalOpponentCreaturesAtk
	global globalOpponentCreaturesHP
	global globalOpponentCreautresId
	global globalOpponentCreaturesOnBoardCount
	global globalIsFirstPlayer
	global globalCardsInDeckCount
	global globalCardsInHandCount
	global globalCardsInHandId
	global globalOptions
	global globalGameState
	global globalLine
	global globalBotSecretCount
	global globalOpponentSecretCount
	global globalCurrentOption
	global globalOptionsInfos
	global globalLastLine
	global globalOptionsCardIds

	#initiate game
	if (msg_type == "ENTITY CREATED") & (obj.__class__.__name__ == "LiveGame"):
		globalBotHP = 30
		globalBaseBotHP = 30
		globalBotArmor = 0
		globalBaseOpponentHP = 30
		globalBaseOpponentHP = 30
		globalOpponentArmor = 0 
		#globalFriendlyCreaturesOnBoard = [False, False,False,False,False,False,False]
		#globalFriendlyCreaturesAtk = [-1,-1,-1,-1,-1,-1,-1,-1]
		#globalFriendlyCreaturesHP = [-1,-1,-1,-1,-1,-1,-1,-1]
		#globalFriendlyCreautresId = [-1,-1,-1,-1,-1,-1,-1,-1]
		globalFriendlyCreaturesAtk =[]
		globalFriendlyCreaturesHP = []
		globalFriendlyCreautresId = []
		#globalOpponentCreaturesOnBoard = [False, False,False,False,False,False,False]
		globalFriendlyCreaturesOnBoardCount = 0
		#globalOpponentCreaturesAtk = [-1,-1,-1,-1,-1,-1,-1,-1]
		#globalOpponentCreaturesHP = [-1,-1,-1,-1,-1,-1,-1,-1]
		#globalOpponentCreautresId = [-1,-1,-1,-1,-1,-1,-1,-1]
		globalOpponentCreaturesAtk =[]
		globalOpponentCreaturesHP = []
		globalOpponentCreautresId = []
		globalOpponentCreaturesOnBoardCount = 0
		globalCardsInDeckCount = 30
		globalCardsInHandCount = 0
		globalCardsInHandId = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,]
		globalBotSecretCount = 0
		globalOpponentSecretCount = 0
		globalCurrentOption = -1
		globalOptionsInfos =[]
		globalCurrentOptionsRewards = []
		print("Starting new game")

		if obj.id>68:
			globalOpponentCreautresId.append(obj)

	#updates stats
	if (msg_type == "TAG UPDATED"):

		#updates hand cards
		if attr == 263:
			globalCardsInHandId[value-1] == obj.card_id
			globalCardsInHandCount +=1
		
		#updates number cards in deck
		if attr == 399:
			globalCardsInDeckCount -= value

		if (attr == 49) & (value == 1):
			obj.tags['GameTag.ZONE'] = 1



		# updates bot stats
		if (obj.id == 64):

			#updates HP
			if attr == 44:
				globalBotHP = globalBaseBotHP-value

			#updates armor
			if (attr == 292):
				globalBotArmor = value

			#updates mana at the start of the turn
			if attr == 26:
				globalBotManaTotal = value
				globalBotManaAvailable = value
			
			#updates mana available after mana usage
			if attr == 25:
				globalBotManaAvailable = globalBotManaTotal-value

		# updates opponent stats
		if (obj.id == 66):

			#updates HP
			if attr == 44:
				globalOpponentHP = globalBaseOpponentHP-value

			#updates armor
			if (attr == 292):
				globalOpponentArmor = value

		# updates bot creatures
		#if (obj.id < 34 
		#not especially needed : partly contained in actions


		# updates opponent creatures 

	if msg_type == "END TURN":
		zoneOrigin = "endturn"
		globalOptionsInfos = []
		globalOptionsInfos.append([zoneOrigin])
		globalCurrentOption = 0
		globalOptionsCardIds = []
		globalOptionsCardIds.append([])

	if msg_type == "OPTION LISTED":
		if (obj== 0) | (obj== 3) | (obj == 2):
			zoneOrigin = "hand"
		if obj == 65:
			zoneOrigin = "heropower"
			originPos = -1
		if obj == 64:
			zoneOrigin = "play"
			originPos = 0
		if obj == 1:
			zoneOrigin = "play"

		if attr:
			originPos = attr
		elif (obj != 65) & (obj != 64):
			originPos = globalFriendlyCreaturesOnBoard.index(obj)

		globalLastLine = "OPTION"

		globalOptionsInfos.append([zoneOrigin, originPos])

		#add OptionscardIds origin info
		if value:
			originCardId = value.card_id
		else:
			originCardId = obj

		globalOptionsCardIds.append([originCardId])
		print(globalOptionsCardIds)
		globalCurrentOption += 1

	if msg_type == "TARGET LISTED":
		
		if value == "The Innkeeper":
			zoneDest = "opponent"
			if attr:
				targetPos = attr
			else:
				targetPos = globalOpponentCreaturesOnBoard.index(obj)

		if value == "Learner#11393":
			zoneDest = "friendly"
			if attr:
				targetPos = attr
			else:
				targetPos = globalFriendlyCreaturesOnBoard.index(obj)

		if obj == 64:
			zoneDest = "friendly"
			targetPos = 0
		if obj == 66:
			zoneDest = "opponent"
			targetPos = 0

		#add OptionscardIds origin info
		if value:
			targetCardId = obj.card_id
		else:
			targetCardId = obj
		
		if globalLastLine == "OPTION":
			print(globalOptionsInfos)
			globalOptionsInfos[globalCurrentOption].extend([zoneDest, targetPos])
			globalOptionsCardIds[globalCurrentOption].append(targetCardId)


		else:
			suboption = globalOptionsInfos[globalCurrentOption].copy()
			suboptionCardId = globalOptionsCardIds[globalCurrentOption].copy()
			print("avant :", globalOptionsInfos)
			suboption[2] = zoneDest
			suboption[3] = targetPos
			globalOptionsInfos.append(suboption)
			print("apres :", globalOptionsInfos)
			

			suboptionCardId[1] = targetCardId
			globalOptionsCardIds.append(suboptionCardId)
			print(globalOptionsCardIds)

			globalCurrentOption+=1
		globalLastLine = "TARGET"
		

	globalLine +=1

	return "{} | {} | {} | {} | {}".format(
		align(msg_type, 15),
		align(repr(obj), 120),
		align(repr(attr), 40),
		align(value, 30),
		align(globalLine, 10)
	)

#zoneOrigin corresponds either to hand or play or end turn or heroPower
#originPos corresponds to the position of the entity acting 0-7 (hero included) for play, 1-10 (0-9) for hand
#zoneDest is either own friendly or opponent
#targetPos corresponds to the position of the target :  (how to do for playing creatures); none if card played is a spell
#secondTargetPos corresponds to the position of the target if creature with a battlecry needing a target
def play_option(zoneOrigin, originPos = None, zoneDest = None, targetPos = None, secondTargetZone = None, secondTargetPos = None):

	"""defining the origin positions """
	#ending the turn
	if zoneOrigin == "endturn":
		ptg.moveTo(globalPosEndTurn[0], globalPosEndTurn[1] )
		ptg.click()

	else :

		if zoneOrigin == "play":

			#hero attacking
			if originPos == 0:
				xorigin = globalPosBotHero_Confirm[0]
				yorigin = globalPosBotHero_Confirm[1]

			elif originPos != -1:
				trueOriginPos = 6+originPos*2-1-globalFriendlyCreaturesOnBoardCount
				xorigin = globalPosBotBoard[trueOriginPos][0]
				yorigin = globalPosBotBoard[trueOriginPos][1]

		if zoneOrigin == "hand":
			xorigin = globalPosHand[globalCardsInHandCount][originPos-1][0]
			yorigin = globalPosHand[globalCardsInHandCount][originPos-1][1]

		if zoneOrigin == "heropower":
			xorigin = globalPosHeroPower[0]
			yorigin = globalPosHeroPower[1]
			
		"""defining the target positions """
		
		if not zoneDest :
			xdest = globalPosCenter[0]
			ydest = globalPosCenter[1]

		else:
			if zoneDest == "friendly":
				if targetPos == 0:
					xdest = globalPosBotHero_Confirm[0]
					ydest = globalPosBotHero_Confirm[1] 

				else :
					trueTargetPos = 6+targetPos*2-1-globalFriendlyCreaturesOnBoardCount
					xdest = globalPosBotBoard[trueTargetPos][0]
					ydest = globalPosBotBoard[trueTargetPos][1]
			
			if zoneDest == "opponent":
				if targetPos == 0:
					xdest = globalPosOpponentHero[0]
					ydest = globalPosOpponentHero[1] 

				else :
					trueTargetPos = 6+targetPos*2-1-globalOpponentCreaturesOnBoardCount
					xdest = globalPosEnemyBoard[trueTargetPos][0]
					ydest = globalPosEnemyBoard[trueTargetPos][1]

		ptg.moveTo(xorigin, yorigin, 0.75)
		ptg.click()
		ptg.dragTo(xdest, ydest)
		ptg.click()

		if secondTargetPos:
			if secondTargetZone == "friendly":
				if secondTargetPos == 0:
					xdestbis = globalPosBotHero_Confirm[0]
					ydestbis = globalPosBotHero_Confirm[1] 

				else :
					if targetPos > secondTargetPos:
						shift=0
					else:
						shift=1

					trueTargetPos = 6 + (secondTargetPos+shift)*2 -1 -(globalFriendlyCreaturesOnBoardCount+1)

					xdestbis = globalPosBotBoard[secondTargetPos][0]
					ydestbis = globalPosBotBoard[secondTargetPos][1]
			
			if zoneDest == "opponent":
				if secondTargetPos == 0:
					xdestbis = globalPosOpponentHero[0]
					ydestbis = globalPosOpponentHero[1] 

				else :
					trueDestBis = 6+originPos*2-1-globalFriendlyCreaturesOnBoardCount
					xdestbis = globalPosEnemyBoard[trueDestBis][0]
					ydestbis = globalPosEnemyBoard[trueDestBis][1]

			ptg.moveTo(xdestbis, ydestbis)
			ptg.click()








def debug_player_names(player_manager):
	print("{} | {} | {}".format(
		align(player_manager.actual_player_names, 40),
		align(player_manager.names_used, 40),
		align(player_manager.name_assignment_done, 10),
	))
