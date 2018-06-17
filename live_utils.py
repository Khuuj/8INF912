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


#mouse coordinates

globalPosEndTurn = [1572, 495]
globalPosBotHero_Confirm = [961, 843]
globalPosHeroPower = [1147, 828]
globalPosOpponentHero = [969, 191]

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

#h1-h13 = all hand positions on bot side
globalPosEnemyBoard = {
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

	#initiate game
	if (msg_type == "ENTITY CREATED") & (obj.__class__.__name__ == "LiveGame"):
		globalBotHP = 30
		globalBaseBotHP = 30
		globalBotArmor = 0
		globalBaseOpponentHP = 30
		globalBaseOpponentHP = 30
		globalOpponentArmor = 0 
		#globalFriendlyCreaturesOnBoard = [False, False,False,False,False,False,False]
		globalFriendlyCreaturesAtk = [-1,-1,-1,-1,-1,-1,-1,-1]
		globalFriendlyCreaturesHP = [-1,-1,-1,-1,-1,-1,-1,-1]
		globalFriendlyCreautresId = [-1,-1,-1,-1,-1,-1,-1,-1]
		#globalOpponentCreaturesOnBoard = [False, False,False,False,False,False,False]
		globalFriendlyCreaturesOnBoardCount = 0
		globalOpponentCreaturesAtk = [-1,-1,-1,-1,-1,-1,-1,-1]
		globalOpponentCreaturesHP = [-1,-1,-1,-1,-1,-1,-1,-1]
		globalOpponentCreautresId = [-1,-1,-1,-1,-1,-1,-1,-1]
		globalOpponentCreaturesOnBoardCount = 0
		globalCardsInDeckCount = 30
		globalCardsInHandCount = 0
		globalCardsInHandId = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,]
		globalBotSecretCount = 0
		globalOpponentSecretCount = 0
		print("Starting new game")

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
			print("zklsjeljkz")




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


		# updates opponent creatures 





	#####debug tests 
	#if (obj.__class__.__name__ != "LiveGame") & (obj.__class__.__name__ != "LivePlayer"):
	#	print(obj.card_id)
	globalLine +=1

	return "{} | {} | {} | {} | {}".format(
		align(msg_type, 15),
		align(repr(obj), 120),
		align(repr(attr), 40),
		align(value, 30),
		align(globalLine, 10)
	)


def debug_player_names(player_manager):
	print("{} | {} | {}".format(
		align(player_manager.actual_player_names, 40),
		align(player_manager.names_used, 40),
		align(player_manager.name_assignment_done, 10),
	))