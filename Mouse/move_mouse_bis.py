#import win32api, win32con
#def click(x,y):
#    win32api.SetCursorPos((x,y))
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#click(10,10)


import sys
import time
import win32api

if (len(sys.argv) < 4):
	print ("Usage: python mousemove.py dx dy speed")
	sys.exit()

current = win32api.GetCursorPos()
cx = sx = current[0]
cy = sy = current[1]

mx = int(sys.argv[1])
my = int(sys.argv[2])
vx = vy = int(sys.argv[3])

print ("Moving", mx, my, "with", vx, "pixels per second")
print ("Press 'q' to quit")

last = time.time()

while(cx != sx+mx & cy != sy+my):
	if win32api.GetAsyncKeyState(ord('Q')):
		sys.exit()
		
	current = time.time()
	tick = current - last
	last = current
	
	if mx > 0:
		cx += vx * tick;
		if cx > mx + sx or cx < sx:
			vx = -vx;
			cx = max( sx, min( mx + sx, cx ) )
	if( my > 0 ):
		cy += vy * tick;
		if cy > my + sy or cy < sy:
			vy = -vy;
			cy = max( sy, min( my + sy, cy ) )
	
	win32api.SetCursorPos((int(cx),int(cy)))
	time.sleep(0.001)
