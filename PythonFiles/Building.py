import pygame
from pygame.locals import *
from element import element
FPS = 50

pygame.init()
clock = pygame.time.Clock()





class Screen:
		#each screen holds the objects that needs to be printed and the window
	def __init__(self, window = None):
		self.m_window = window
		self.m_object = {}
	
	#update the window
	def windowUpdate(self, window):
		self.m_window = window
	#put the object into the dictionary
	#default x  = 0
	#default y = 0
	def addItem(self, nameOfObejct, Object, x=None, y=None):
		if x == None:
			x= 0
		if y == None:
			y = 0
		if type(Object) == type(element()):
			Object = Object.getImage()
		item = []
		item.append(Object)
		item.append(x)
		item.append(y)
		self.m_object[nameOfObejct] = item

		#return the data value of object
	def getItem(self, nameOfObejct):
		return self.m_object[nameOfObejct][0]

	def getItemPos(self, nameOfObejct):
		return tuple([self.m_object[nameOfObejct][1], self.m_object[nameOfObejct][2]])

	#put all the objects into the screen
	def ScreenLoad(self):
		for i in self.m_object:
			self.m_window.blit(self.m_object[i][0],(self.m_object[i][1], self.m_object[i][2]))

	#update the position of certain object
	def itemUpdate(self, nameOfObejct, x, y):
		self.m_object[nameOfObejct][1] = x
		self.m_object[nameOfObejct][2] = y

	#return xdirection
	#return yDirection
	def ItemZigZag(self, nameOfObejct, xDirection, yDirection, xSpeed=1, ySpeed=1):
		xcord = self.m_object[nameOfObejct][1]
		ycord = self.m_object[nameOfObejct][2]
		if xcord > abs(self.m_window.get_width() - self.m_object[nameOfObejct][0].get_width()) or xcord < 0:
			xDirection = not xDirection
		if ycord > abs(self.m_window.get_height() - self.m_object[nameOfObejct][0].get_height()) or ycord < 0:
			yDirection = not yDirection
		if xDirection == 1:
			xcord += xSpeed
		if xDirection == 0:
			xcord -= xSpeed
		if yDirection == 1:
			ycord += ySpeed
		if yDirection == 0:
			ycord -= ySpeed
		self.m_object[nameOfObejct][1] = xcord
		self.m_object[nameOfObejct][2] = ycord

		return xDirection, yDirection
			

clock.tick(FPS)

window = pygame.display.set_mode((800, 600))

myScreen = Screen(window)

knight  = pygame.image.load("knight.png")
First = pygame.image.load("python_blue.png")
Second = pygame.image.load("python_white.png")
Final = pygame.image.load("god_emperor_pythonos.png")

mySecond = element(Second)

myScreen.addItem("mySecond", mySecond)
myScreen.addItem("Final", Final, 200, 0)
myScreen.addItem("knight", knight, 600, 350)
#myScreen.addItem("knight", knight)
#myScreen.addItem("Final", Final)
#myScreen.itemUpdate("Final", myScreen.getItem("Final").get_width()+800, 200)
myScreen.ScreenLoad()
pygame.display.update()

xcounter = 0
ycounter = 0
game = 1
xDirection = True
yDirection = True
x2Direction = True
y2Direction = True
x3Direction = True
y3Direction = True
xcord = 0
ycord = 0
xSpeed = 1
ySpeed = 3

while game == 1:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				game = 0
	
	xDirection, yDirection = myScreen.ItemZigZag("mySecond",xDirection,yDirection)
	x2Direction, y2Direction = myScreen.ItemZigZag("Final", x2Direction, y2Direction)
	x3Direction, y3Direction = myScreen.ItemZigZag("knight", x3Direction, y3Direction)
	window.fill((0,0,0))
	myScreen.ScreenLoad()
	pygame.display.flip()
	xcounter+=1
	ycounter+=1
	
pygame.quit()