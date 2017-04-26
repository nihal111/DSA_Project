def createBoard(N):
	# Board stores the squaremappings - ladder bottom->top, snake mouth->tail
	board = [i for	 i in range(0, N)]

	# Retrieve input from input.txt file
	with open("input.txt") as f:
	    inputFile = f.readlines()

	# Get ladders and update board[bottom_of_ladder] to top_of_ladder
	ladders = int(inputFile[0].strip("\n"))
	for x in range(0, ladders):
		ladderBottom = int(inputFile[x + 1].split(" ")[0])
		ladderTop = int(inputFile[x + 1].strip("\n").split(" ")[1])
		board[ladderBottom] = ladderTop

	# Get snakes and update board[snake_mouth] to snake_tail
	snakes = int(inputFile[ladders + 1].strip("\n"))
	for x in range(ladders + 1, ladders + 1 + snakes):
		snakeHead = int(inputFile[x + 1].split(" ")[0])
		snakeTail = int(inputFile[x + 1].strip("\n").split(" ")[1])
		board[snakeHead] = snakeTail
	return board

def sequenceSolver(N, board, verbose=True):
	# Initialise minSteps for each block as N
	minStepsTo = [N for i in range(0, N)]
	# 0 is the starting position
	minStepsTo[0] = 0
	# Initialise prevSquareFor each block. Contains previousSquare and diceRoll
	# If a dice roll of d takes the player from sq1 to sq2
	# prevSquareFor[sq2] = (sq1, dice roll)
	prevSquareFor = [(-1, -1) for i in range(0, N)]
	
	# Iterate over the first 6 squares and update minStepsTo, prevSquareFor for each
	for sq in range (1, 7):
		minStepsTo[board[sq]] = 1
		prevSquareFor[board[sq]] = (0, sq)

	# Iterate over the remaining squares and update minStepsTo, prevSquareFor for each
	for sq in range (7, N):
		changed = 0
		# Check all 6 prior squares to find minimum steps
		for step in range (1,7):
			if minStepsTo[sq-step] + 1 < minStepsTo[board[sq]]:
				minStepsTo[board[sq]] = minStepsTo[sq-step] + 1
				prevSquareFor[board[sq]] = (sq-step, step)
				changed = 1
		# If minSteps for a snake tail has been changed
		# then update all blocks from the corresponding snake's tail to that snake's mouth
		if changed == 1 and board[sq] < sq:
			for sq2 in range (board[sq] + 1,sq):
				for step in range (1, 7):
					if minStepsTo[sq2 - step] + 1 < minStepsTo[board[sq2]]:
						minStepsTo[board[sq2]] = minStepsTo[sq2 - step] + 1
						prevSquareFor[board[sq2]] = (sq2-step, step)
	
	# If path to N-1 exists
	if minStepsTo[N-1] < N:
		x = N-1
		a = str(N-1)
		while minStepsTo[x] != x:
			a = a + " --[" + str(prevSquareFor[x][1]) + "]-> " + str(prevSquareFor[x][0])
			x = prevSquareFor[x][0]
		if verbose:
			print "Shortest path is " + str(minStepsTo[N-1]) + " steps"
			print ' '.join(w[::-1] for w in a[::-1].split())
	else:
		if verbose:
			print "No path found"

if __name__ == "__main__":
	board = createBoard(101)
	sequenceSolver(101, board)
