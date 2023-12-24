import pygame, sys 
from settings import *
from pygame.image import load
from random import randint
from sprites import Cloud, Star

class Animation:
	def __init__(self):
		# main setup 
		self.display_surface = pygame.display.get_surface()

		# cloud setup
		clouds = self.create_clouds()
		self.cloud_sprites = pygame.sprite.Group()
		self.draw_clouds = [self.cloud_sprites.add(cloud) for cloud in clouds]

		# star setup
		stars = self.create_stars()
		self.star_sprites = pygame.sprite.Group()
		self.draw_stars = [self.star_sprites.add(star) for star in stars]

		# combine all sprites
		self.all_sprites = pygame.sprite.Group()
		self.all_sprites.add(self.star_sprites, self.cloud_sprites)

	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

	def message(self, dt):
		# create the message
		font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

		text = font.render('Happy Holidays!', False, TEXT_COLOR)
		textRect = text.get_rect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)) # set the center of the rectangular object
		self.display_surface.blit(text, textRect) # draw the text

	def create_clouds(self):
		# top clouds
		self.top_cloud_surf = load('../graphics/clouds/top_cloud.png').convert_alpha()
		self.top_cloud1 = Cloud(self.top_cloud_surf, 300, 100, self.display_surface)
		self.top_cloud2 = Cloud(self.top_cloud_surf, 600, 100, self.display_surface)
		self.top_cloud3 = Cloud(self.top_cloud_surf, 1000, 100, self.display_surface)

		# middle clouds
		self.mid_cloud_surf = load('../graphics/clouds/middle_cloud.png').convert_alpha()
		self.mid_cloud1 = Cloud(self.top_cloud_surf, 600, 200, self.display_surface)
		self.mid_cloud2 = Cloud(self.top_cloud_surf, 900, 200, self.display_surface)
		self.mid_cloud3 = Cloud(self.top_cloud_surf, 1300, 200, self.display_surface)

		# bottom clouds
		self.bottom_cloud_surf = load('../graphics/clouds/bottom_cloud.png').convert_alpha()
		self.bottom_cloud1 = Cloud(self.top_cloud_surf, 200, 300, self.display_surface)
		self.bottom_cloud2 = Cloud(self.top_cloud_surf, 700, 300, self.display_surface)
		self.bottom_cloud3 = Cloud(self.top_cloud_surf, 1200, 300, self.display_surface)

		clouds = [self.top_cloud1, self.top_cloud2, self.top_cloud3, 
			self.mid_cloud1, self.mid_cloud2, self.mid_cloud3, 
			self.bottom_cloud1, self.bottom_cloud2, self.bottom_cloud3]
		
		return clouds

	def create_stars(self):
		self.tree_star_surf = load('../graphics/stars/tree_star.png').convert_alpha()
		self.tree_star_surf = pygame.transform.scale(self.tree_star_surf, (50, 50)).convert_alpha()

		self.sky_star_surf = load('../graphics/stars/sky_star.png').convert_alpha()
		self.sky_star_surf = pygame.transform.scale(self.sky_star_surf, (200, 200)).convert_alpha()

		# stars for the trees
		self.tree_star1 = Star(self.tree_star_surf, 85, 445, self.display_surface)
		self.tree_star2 = Star(self.tree_star_surf, 240, 455, self.display_surface)
		self.tree_star3 = Star(self.tree_star_surf, 395, 445, self.display_surface)
		self.tree_star4 = Star(self.tree_star_surf, 550, 455, self.display_surface)
		self.tree_star5 = Star(self.tree_star_surf, 705, 445, self.display_surface)
		self.tree_star6 = Star(self.tree_star_surf, 860, 455, self.display_surface)
		self.tree_star7 = Star(self.tree_star_surf, 1015, 445, self.display_surface)
		self.tree_star8 = Star(self.tree_star_surf, 1170, 455, self.display_surface)

		# star for the sky
		self.sky_star = Star(self.sky_star_surf, 1090, 100, self.display_surface)

		stars = [self.tree_star1, self.tree_star2, self.tree_star3, 
		   self.tree_star4, self.tree_star5, self.tree_star6,
		   self.tree_star7, self.tree_star8, self.sky_star]
		
		return stars

	def draw_ground(self, dt):
		pygame.draw.rect(self.display_surface, (240, 240, 240), [0, WINDOW_HEIGHT-60, WINDOW_WIDTH, 60]) 

	def create_tree(self, x, y, display_surface, dt):
		pygame.draw.rect(self.display_surface, (139,69,19), [x+60, y+400, 30, 45])
		pygame.draw.polygon(self.display_surface, (0,128,0), [[x+150, y+400], [x+75, y+250], [x+0, y+400]])
		pygame.draw.polygon(self.display_surface, (0,128,0), [[x+140, y+350], [x+75, y+230], [x+10, y+350]])

	def draw_trees(self, dt):
		self.create_tree(10,220, self.display_surface, dt)
		self.create_tree(165,230, self.display_surface, dt)
		self.create_tree(320,220, self.display_surface, dt)
		self.create_tree(475,230, self.display_surface, dt)
		self.create_tree(630,220, self.display_surface, dt)
		self.create_tree(785,230, self.display_surface, dt)
		self.create_tree(940,220, self.display_surface, dt)
		self.create_tree(1095,230, self.display_surface, dt)

	def run(self, dt):		
		self.event_loop()
		# drawing
		self.display_surface.fill(BACKGROUND_COLOR)
		self.draw_ground(dt)
		self.draw_trees(dt)
		self.message(dt)
		self.all_sprites.draw(self.display_surface)
		self.all_sprites.update(dt)

class Opening:
	def __init__(self, switch):
		# main setup 
		self.display_surface = pygame.display.get_surface()
		self.switch = switch

	# input
	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				self.switch()

	def message(self, dt):
		# create the message
		font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

		text1 = font.render('Welcome to the Raspberry Pi Christmas Show!', False, TEXT_COLOR)
		textRect1 = text1.get_rect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)) # set the center of the rectangular object
		self.display_surface.blit(text1, textRect1) # draw the text

		text2 = font.render('Press "Enter" to start!', False, TEXT_COLOR)
		textRect2 = text2.get_rect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 150))
		self.display_surface.blit(text2, textRect2)

	def run(self, dt):	
		self.event_loop()
		# drawing
		self.display_surface.fill(BACKGROUND_COLOR)
		self.message(dt)

class Snowflake:
	def __init__(self, position, radius, gravity):
		self.pos = position
		self.radius = radius
		self.gravity = gravity
		self.RADIUS_MAX = radius
		self.radius_change = True
		self.color = (255, 255, 255)

	def controller(self, height, width):
		self.update_pos(height, width)
		self.update_rad()
		self.update_color(height)

	def update_pos(self, height, width):
		if self.pos[1] < height + self.radius:
			self.pos = (self.pos[0] + randint(-1, 1), self.pos[1] + self.gravity)
		else:
			self.respawn(width)

	def update_rad(self):
		if self.radius_change:
			self.radius = randint(1, self.RADIUS_MAX)
			self.radius_change = False
		else:
			self.radius_change = True

	def update_color(self, height):
		rgb = 250 - 100 * (self.pos[1] / height) 
		self.color = (rgb, rgb, rgb)

	def respawn(self, width):
	 	self.pos = (randint(0, width), -1 * self.radius)
	
