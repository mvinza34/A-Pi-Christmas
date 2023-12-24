import pygame

class General(pygame.sprite.Sprite):
	def __init__(self, image, x, y, display_surface):
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = self.image.get_rect(center = (x,y))
		self.display_surface = display_surface

class Cloud(General):
	def __init__(self, image, x, y, display_surface):
		super().__init__(image, x, y, display_surface)

	def update(self, dt):
		self.rect.move_ip(-3, 0) # moves the clouds to the left
		if self.rect.right <= 0: # respawns the clouds once they exit the screen
			self.rect.left = self.display_surface.get_width()
	
class Star(General):
	def __init__(self, image, x, y, display_surface):
		super().__init__(image, x, y, display_surface)

	def update(self, dt):
		self.rect.move_ip(0,0) # holds the stars still
