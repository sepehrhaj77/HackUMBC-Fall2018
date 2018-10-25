import pygame

class Element:

	def __init__(self, image=None, x=0, y=0):
		try:
			if image == None:
				self.m_image = None
				self.m_width = 0
				self.m_height = 0
			else:
				self.m_image = image
				self.m_width, self.m_height = image.get_width(), image.get_height()
				self.m_xcord, self.m_ycord = x, y
		except Exception as e:
			print("At element constructor,",e)
			self.m_image = 0
			self.m_width = 0
			self.m_height = 0
			self.m_xcord = 0
			self.m_ycord = 0

	
	def getImage(self):
		return self.m_image

	def get_width(self):
		return self.m_width

	def get_height(self):
		return self.m_height

	def get_x(self):
		return self.m_xcord

	def get_y(self):
		return self.m_ycord

	def setImage(self, image):
		try:
			self.m_image = image
			pass
		except Exception as e:
			print("<element> class: setImage(self, image)", e)
			raise

	def set_width(self, new_width):
		try:
			self.m_width = new_width
		except Exception as e:
			print("<element> class: set_width(self, image)", e)
			raise

	def set_height(self, new_height):
		try:
			self.m_height = new_height
		except Exception as e:
			print("<element> class: set_height(self, image)", e)
			raise

	def set_x(self, new_x):
		try:
			self.m_xcord = new_x
		except Exception as e:
			print("<element> class: set_x(self, image)", e)
			raise

	def set_y(self, new_y):
		try:		
			self.m_ycord = new_y
		except Exception as e:
			print("<element> class: set_y(self, image)", e)
			raise

pygame.init()
knight  = pygame.image.load("knight.png")
x = Element(knight,1,1)
print(x.get_height(), x.get_width(), x.get_y(), x.get_x(), x.getImage())

pygame.quit()
			
