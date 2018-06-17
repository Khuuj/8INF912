import pyautogui as ptg 

#setting fail safes
ptg.FAIL_SAFE=True
ptg.PAUSE=1

#moving the pointer to screen center
screenWidth, screenHeight = ptg.size()
screenWidthMiddle = screenWidth / 2
screenHeightMiddle = screenHeight / 2

 
#ptg.moveTo(screenWidth / 2, screenHeight / 2)
# ptg.click() #click!!
i=0

#while (ptg.position() != (screenWidthMiddle, screenHeightMiddle)):
#	if (screenWidthMiddle > ptg.position()[0]):
#		xmove = 100
#	else:
#		xmove =-100
#	if screenHeightMiddle > ptg.position()[1]:
#		ymove =100
#	else:
#		ymove =-100
#	ptg.moveRel(xmove,ymove,1)

xmove = screenWidthMiddle - ptg.position()[0]
ymove = screenHeightMiddle - ptg.position()[1]
ptg.moveRel(xmove,ymove,0.5)

#moving mouse like in staircase pattern
