import random
import copy

for i in xrange(0, 1000):
	available = [a for a in xrange(1,10000)]
	with open("100x100inputs/input" + str(i) +".txt", "w") as f:
		num_ladders = random.randint(0, 1000)
		num_snakes = random.randint(0, 1000)
		f.write(str(num_ladders) + "\n")
		for ladder in xrange(0, num_ladders):
			ladder_bottom_index = len(available)-1
			while ladder_bottom_index == len(available)-1:
				ladder_bottom = random.choice(available)
				ladder_bottom_index = available.index(ladder_bottom)
			print "Input file ", i, "ladder bottom index", ladder_bottom_index
			ladder_top = random.choice([available[j] for j in xrange(ladder_bottom_index + 1, len(available))])
			available.remove(ladder_bottom)
			available.remove(ladder_top)
			f.write(str(ladder_bottom) + " " + str(ladder_top) + "\n")
		f.write(str(num_snakes) + "\n")
		for snake in xrange(0, num_snakes):
			snake_mouth_index = 0
			while snake_mouth_index == 0:
				snake_mouth = random.choice(available)
				snake_mouth_index = available.index(snake_mouth)
			print "Input file ", i, "snake mouth index", snake_mouth_index
			snake_tail = random.choice([available[k] for k in xrange(0, snake_mouth_index)])
			available.remove(snake_mouth)
			available.remove(snake_tail)
			f.write(str(snake_mouth) + " " + str(snake_tail) + "\n")
