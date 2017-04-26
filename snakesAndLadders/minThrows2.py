go_to = [i for	 i in range(0,101)]
come_from = [i for i in range(0,101)]

with open("input.txt") as f:
    inputFile = f.readlines()

ladders = int(inputFile[0].strip("\n"))
for x in range(0, ladders):
	ladderBottom = int(inputFile[x + 1].split(" ")[0])
	ladderTop = int(inputFile[x + 1].strip("\n").split(" ")[1])
	go_to[ladderBottom] = ladderTop
	come_from[ladderTop] = ladderBottom

snakes = int(inputFile[ladders+1].strip("\n"))

for x in range(ladders + 1, ladders + 1 + snakes):
	snakeHead = int(inputFile[x + 1].split(" ")[0])
	snakeTail = int(inputFile[x + 1].strip("\n").split(" ")[1])
	go_to[snakeHead] = snakeTail
	come_from[snakeTail] = snakeHead

spath = [101 for i in range(0,101)]
spathfrom = []

def minpath(sq):
	for sq in range (1,7):
		spath[sq] = 1
		spathfrom[sq] = 0
	for sq in range (7,101):
	changed=0
		for step in range (1,7):
			if spath[sq-step]+1<spath[go_to[sq]]:
				spath[go_to[sq]] = spath[sq-step]+1
				spathfrom[go_to[sq]] = sq-step
				changed = 1
		if changed == 1 and go_to[sq]<sq:
			for sq2 in range (go_to[sq]+1,sq):
				for step in range (1,7):
					if spath[sq2-step]+1<spath[go_to[sq2]]:
						spath[go_to[sq2]] = spath[sq2-step]+1
						spathfrom[go_to[sq2]] = sq2-step
	print "Shortest path is " + str(spath[100]) + " steps."
	x=100
	a = ""
	while x>0:
		a = a + str(spathfrom[x]) + " -> "
		x = spathfrom[x]
	print a
