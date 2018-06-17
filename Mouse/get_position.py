import pyautogui as ptg 
from time import sleep

#setting fail safes
ptg.FAIL_SAFE=True
ptg.PAUSE=1

xpos = ptg.position()[0]
ypos = ptg.position()[1]


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

ptg.moveTo(globalPosBotBoard[1][0], globalPosBotBoard[1][1], 0.8)

#print("xpos: ",xpos)
#print("ypos: ",ypos)

#globalPosBotBoard = {
#    "b1":(590, 597),
#    "b2":(640, 590),
#    "b3":(710, 605),
#    "b4":(768, 584),
#    "b5":(837, 612),
#    "b6":(893,579),
#    "b7":(967, 613),
#    "b8":(1027, 585),
#    "b9":(1085, 592),
#    "b10":(1150, 584),
#    "b11":(1218, 603),
#    "b12":(1277, 608),
#    "b13":(1342, 592)
#}
#
#globalPosOpponentHero = [969, 191]
#
##xpos = ptg.position()[0]
##ypos = ptg.position()[1]
#
#sleep(1)
#
#ptg.moveTo(globalPosBotBoard["b9"][0],globalPosBotBoard["b9"][1],0.8)
#ptg.click()
#
#ptg.dragTo(globalPosOpponentHero[0], globalPosOpponentHero[1],0.8)
##ptg.mouseUp()
#ptg.click()


#a =[(1,2),(3,4)]
#print(a[1][1])