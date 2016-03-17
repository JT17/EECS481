#!usr/bin/python

import sys, pygame, time

#the lower the buffer the less the sound latency
#the buffer must be a multiple of 2, default is 4096
pygame.mixer.pre_init(buffer=512)
pygame.init()
pygame.mixer.init()

numkeys = 12
flag = []
sound = []
mode = ["piano5", "piano4", "piano3", "piano2", "piano1"]
curmode = 0
flagmode = 0
flagmusic = 0
flagup = 0
flagdown = 0
flagright = 0
flagleft = 0
skip = 0
screen = pygame.display.set_mode()

#what to do when a keyboard key is pressed
def press(n):
	global flag, sound
	if (flag[n] == 1): return
	sound[n].stop()
	sound[n].play()
	flag[n] = 1

#what to do when a keyboard key is released
def release(n):
	global flag
	flag[n] = 0

#change mode on left mouse click
def change_mode():
	global flagmode, curmode, mode, numkeys, sound
	if (flagmode == 1): return
	flagmode = 1
	curmode = curmode + 1
	if (curmode >= len(mode)): curmode = 0
	i = 0
	while (i < numkeys):
		sound[i] = pygame.mixer.Sound("Sound/" + mode[curmode] + "_" + str(i) + ".wav")
		i = i + 1

#play music on right mouse click
def play_music():
	global flagmusic, curmode, mode
	if (flagmusic == 1): return
	flagmusic = 1
	#play music depending on current mode
	sample()

#fight song?
def sample():
	play(0, 0.7)
	play(0, 0.4)
	play(8, 0.4)
	play(10, 0.4)
	play(1, 0.4)
	play(3, 0.4)
	play(5, 0.4)

#play key n and leave a t second gap
def play(n, t):
	press(n)
	time.sleep(t)
	release(n)

def up():
	global flagup
	if (flagup == 1): return
	flapup = 1
	#do something for up

def down():
	global flagdown
	if (flagdown == 1): return
	flagdown = 1
	#do something for down

def right():
	global flagright
	if (flagright == 1): return
	flagright = 1
	#do something for right

def left():
	global flagleft
	if (flagleft == 1): return
	flagleft = 1
	#do something for left

#initialize sound array with 12 sounds
i = 0
while (i < numkeys):
	flag.append(0)
	sound.append(pygame.mixer.Sound("Sound/" + mode[0] + "_" + str(i) + ".wav"))
	i = i + 1

#main operation loop
while 1:
	#for some reason this is needed in order to close the program
	for e in pygame.event.get():
		if (e.type == pygame.QUIT): sys.exit()

	#keyboard input
	k = pygame.key.get_pressed()
	if k[pygame.K_ESCAPE]: sys.exit() #press Esc to end program
	if k[pygame.K_a]: press(0)
	else: release(0)
	if k[pygame.K_w]: press(1)
	else: release(1)
	if k[pygame.K_s]: press(2)
	else: release(2)
	if k[pygame.K_d]: press(3)
	else: release(3)
	if k[pygame.K_f]: press(4)
	else: release(4)
	if k[pygame.K_g]: press(5)
	else: release(5)
	if k[pygame.K_SPACE]: press(6)
	else: release(6)
	if k[pygame.K_RETURN]: press(7)
	else: release(7)
	if k[pygame.K_LEFT]: press(8)
	else: release(8)
	if k[pygame.K_UP]: press(9)
	else: release(9)
	if k[pygame.K_DOWN]: press(10)
	else: release(10)
	if k[pygame.K_RIGHT]: press(11)
	else: release(11)

	#mouse click input
	c = pygame.mouse.get_pressed()
	if c[0]: change_mode() #left click
	else: flagmode = 0
	if c[2]: play_music() #right click
	else: flagmusic = 0

	#mouse movement input
	#don't really need any of this
	#very sensitive
	m = pygame.mouse.get_rel()
	if (skip == 0):
		x, y = m
		if (y < 0): up()
		else: flagup = 0
		if (y > 0): down()
		else: flagdown = 0
		if (x > 0): right()
		else: flagright = 0
		if (x < 0): left()
		else: flagleft = 0

		#position mouse so it never runs off the window
		pygame.mouse.set_pos([300, 300])
		skip = 1
	else: skip = 0


