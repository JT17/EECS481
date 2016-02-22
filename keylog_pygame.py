import pygame;
import sys;
pygame.init();
pygame.mixer.init();
pygame.display.set_mode();
cur_pos = pygame.mouse.get_rel();
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit();
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				channela = pygame.mixer.Sound('Sound/piano5_0.wav').play();
			if event.key == pygame.K_w:
				channela = pygame.mixer.Sound('Sound/piano4_1.wav').play();
			if event.key == pygame.K_s: #d
				channela = pygame.mixer.Sound('Sound/piano4_2.wav').play();
			if event.key == pygame.K_d:
				channela = pygame.mixer.Sound('Sound/piano4_3.wav').play();
			if event.key == pygame.K_f:
				channela = pygame.mixer.Sound('Sound/piano4_4.wav').play();
			if event.key == pygame.K_g:
				channela = pygame.mixer.Sound('Sound/piano4_5.wav').play();
#		if event.type == pygame.MOUSEMOTION:
#			relx, rely = event.rel;
#			if relx < 0:
#				channela = pygame.mixer.Sound('Sound/piano4_6.wav').play();
#			elif relx > 0:
#				channela = pygame.mixer.Sound('Sound/piano4_7.wav').play();
#			elif rely < 0:
#				channela = pygame.mixer.Sound('Sound/piano4_8.wav').play();
#			elif rely > 0:
##				channela = pygame.mixer.Sound('Sound/piano4_9.wav').play();
#					
					
