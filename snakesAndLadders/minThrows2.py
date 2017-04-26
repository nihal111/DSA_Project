# Board stores the squaremappings - ladder bottom->top, snake mouth->tail
board = [i for	 i in range(0,101)]
come_from = [i for i in range(0,101)]

# Retrieve input from input.txt file
with open("input.txt") as f:
    inputFile = f.readlines()

# Get ladders and update board[bottom_of_ladder] to top_of_ladder
ladders = int(inputFile[0].strip("\n"))
for x in range(0, ladders):
	ladderBottom = int(inputFile[x + 1].split(" ")[0])
	ladderTop = int(inputFile[x + 1].strip("\n").split(" ")[1])
	board[ladderBottom] = ladderTop
	come_from[ladderTop] = ladderBottom

# Get snakes and update board[snake_mouth] to snake_tail
snakes = int(inputFile[ladders+1].strip("\n"))
for x in range(ladders + 1, ladders + 1 + snakes):
	snakeHead = int(inputFile[x + 1].split(" ")[0])
	snakeTail = int(inputFile[x + 1].strip("\n").split(" ")[1])
	board[snakeHead] = snakeTail
	come_from[snakeTail] = snakeHead

#Initialise minSteps for each block as 101
minStepsTo = [101 for i in range(0,101)]
# 0 is the starting position
minStepsTo[0] = 0
prevSquareFor = [101 for i in range(0,101)]

def solve():

	# Iterate over the first 6 squares and update minStepsTo, prevSquareFor for each
	for sq in range (1,7):
		minStepsTo[board[sq]] = 1
		prevSquareFor[board[sq]] = 0

	# Iterate over the remaining squares and update minStepsTo, prevSquareFor for each
	for sq in range (7,101):
		changed = 0
		# Check all 6 prior squares to find minimum steps
		for step in range (1,7):
			if minStepsTo[sq-step]+1<minStepsTo[board[sq]]:
				minStepsTo[board[sq]] = minStepsTo[sq-step]+1
				prevSquareFor[board[sq]] = sq-step
				changed = 1
		# If minSteps for a square has been changed and it is a snake mouth
		# then update all blocks from the corresponding snake's tail to that snake's mouth
		if changed == 1 and board[sq]<sq:
			for sq2 in range (board[sq]+1,sq):
				for step in range (1,7):
					if minStepsTo[sq2-step]+1<minStepsTo[board[sq2]]:
						minStepsTo[board[sq2]] = minStepsTo[sq2-step]+1
						prevSquareFor[board[sq2]] = sq2-step
	print "Shortest path is " + str(minStepsTo[100]) + " steps."
	x = 100
	a = "100"[::-1] + " >- "
	while minStepsTo[x]!=x:
		a = a + str(prevSquareFor[x])[::-1]
		x = prevSquareFor[x]
		if (x != 0):
			 a = a + " >- "
	print a[::-1]

if __name__ == "__main__":
	solve()
