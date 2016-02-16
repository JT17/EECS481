import getch 
logger = getch.getch
run = 1;
while(run == 1):
	next_char = logger();
	if(next_char == '\x03'):
		run = 0;
	elif(next_char == 'a'):
		print "you pressed a!"

