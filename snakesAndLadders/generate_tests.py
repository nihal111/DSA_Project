import random

available = [i for i in xrange(1,10000)]

for i in xrange(0, 1000):
	with open("100x100inputs/input" + str(i) +".txt", "w") as f:
		num_ladders = random.randint(0, 1000)
		num_snakes = random.randint(0, 1000)
		f.write(str(num_ladders)+"\n")
		for ladder in xrange(0, num_ladders):
			ladder_bottom = random.choice(available)
			ladder_top = random.choice(list())
			available.remove(ladder_top)
			f.write(str(ladder_bottom))
