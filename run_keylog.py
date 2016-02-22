import getch 
import pygame
logger = getch.getch
run = 1;

pygame.init();
pygame.mixer.init();
sounda = pygame.mixer.Sound('Sound/piano4_9.wav')

while(run == 1):
	next_char = logger();
	if(next_char == '\x03'):
		run = 0;
	elif(next_char == 'a'):
		channela = sounda.play();
	elif(next_char == 'w'):
		channela = pygame.mixer.Sound('Sound/piano4_2.wav').play();

