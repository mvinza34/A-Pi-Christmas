import pygame, os
from settings import *
from pygame.image import load
from pygame.math import Vector2 as vector
from random import randint
from animation import Animation, Snowflake, Opening

import RPi.GPIO as GPIO 
from machine import Pin
from buzzer_music import music
from time import sleep

# Ensures that all assets will import properly 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Main:
	def __init__(self):
		# main setup
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption("A Pi Christmas")
		self.clock = pygame.time.Clock()

		# opening screen, transition, and animation setup
		self.opening = Opening(self.switch)
		self.opening_active = True
		self.transition = Transition(self.toggle)
		self.animation = Animation()

		# cursor
		surf = load('../graphics/cursor/cursor.png').convert_alpha()
		cursor = pygame.cursors.Cursor((0,0), surf)
		pygame.mouse.set_cursor(cursor)

	def toggle(self):
		self.opening_active = not self.opening_active

	def switch(self):
		self.transition.active = True
   
	def run(self):
		# create the snowflakes
		snowflakes = []
		for i in range(0, 500):
			snowflakes.append(Snowflake(
				position = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)), 
				radius = randint(2, 4), 
				gravity = randint(1, 2))) 
			
		while True:
			dt = self.clock.tick() / 1000 # delta time

			if self.opening_active:
				self.opening.run(dt) # run the opening screen
			else:
				self.animation.run(dt) # run the animation
				# Draw the snowflakes
				for snowflake in snowflakes:
					pygame.draw.circle(self.display_surface, snowflake.color, snowflake.pos, snowflake.radius)
					snowflake.controller(WINDOW_HEIGHT, WINDOW_WIDTH) 

			self.transition.display(dt) # run the transition from the opening screen to the animation
			pygame.display.update()

class Xmas:
	def __init__(self):
		# Flowing LEDs
		self.leds = [Pin(i) for i in range(2,20)]

		# buzzers
		self.buzzers = [Pin(22),Pin(27),Pin(20),Pin(21)]

		# Christmas songs
		self.songs = [song1,song2,song3]

		# time limits for each of the 3 songs
		self.song1_time = len(song1)
		self.song2_time = len(song2)
		self.song3_time = len(song3)
	
	def lights_on(self):
		for pin in self.leds:
			GPIO.output(pin,GPIO.HIGH)
			sleep(0.1)

	def lights_off(self):
		for pin in reversed(self.leds):
				GPIO.output(pin,GPIO.LOW)
				sleep(0.1)

	def play(self):
		# We Wish You A Merry Christmas
		mySong = music(self.songs[0], pins=self.buzzers)
		mySong.stop() # keeps the buzzers from annoyingly beeping when first running the code			
		self.lights_on()
		mySong.resume()
		while self.song1_time >= 0: # counts down the time it takes for the song to play 
			mySong.tick()
			sleep(0.05)
			self.song1_time -= 5  # countdown rate (varies depending on the song) (figured out through trial and error)        
		mySong.stop() # stops the buzzers once the countdown is finished
		sleep(1)
		self.lights_off()
		sleep(1)

		# Jingle Bells		
		mySong = music(self.songs[1], pins=self.buzzers)
		self.lights_on()			
		mySong.resume()
		while self.song2_time >= 0:
			mySong.tick()
			sleep(0.08)
			self.song2_time -= 3.65 # countdown rate  
		mySong.stop()  
		sleep(1)
		self.lights_off()
		sleep(1)

		# Silent Night
		mySong = music(self.songs[2], pins=self.buzzers)
		self.lights_on()
		mySong.resume()
		while self.song3_time >= 0:
			mySong.tick()
			sleep(0.1)
			self.song3_time -= 12.25 # countdown rate  
		mySong.stop()
		sleep(1)
		self.lights_off()
		sleep(1)

# switch from the opening screen to the animation	 
class Transition:
	def __init__(self, toggle):
		self.display_surface = pygame.display.get_surface()
		self.toggle = toggle
		self.active = False

		self.xmas = Xmas()

		self.border_width = 0
		self.direction = 1
		self.center = (WINDOW_WIDTH /2, WINDOW_HEIGHT / 2)
		self.radius = vector(self.center).magnitude()
		self.threshold = self.radius + 100

	# creates a circle that closes off the opening screen, and then opens to the animation
	def display(self, dt):
		if self.active:
			self.border_width += 1000 * dt * self.direction
			if self.border_width >= self.threshold:
				self.direction = -1
				self.toggle()
				
				self.xmas.play() # play the christmas show before ending with the animation
			
			if self.border_width < 0:
				self.active = False
				self.border_width = 0
				self.direction = 1
			pygame.draw.circle(self.display_surface, TRANSITION_COLOR, self.center, self.radius, int(self.border_width))

if __name__ == '__main__':
	main = Main()
	main.run()
