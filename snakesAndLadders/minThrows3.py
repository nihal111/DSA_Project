def createBoard(N):
	# Board stores the squaremappings - ladder bottom->top, snake mouth->tail
	board = [i for i in range(0, N)]

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

def modifiedDijkstra(N, board, verbose=True):
	# List to maintain if an element has been visited
	isCalled = [0 for i in range(0, N)]

	# List of list of tuples
	# Each tuple has 3 elements: (the board element, list(path to that element from 0), list(dice rolls))
	levels = []
	isCalled[0] = 1
	levels.append([(0,0,0)])
	# For each level in the list of levels. Go step wise on each level
	for level in levels:
		# Maintain a list of neighbours for all squares (tuples) in a level
		neighbours = []
		for index, parent, dice in level:
			# Add all subsequent 6 elements on the board to neighbours, after computing the list(new path) and list (new dice)
			for x in range (index + 1, index + 7):
				if x <= N-1:
					if not isCalled[board[x]]:
						isCalled[board[x]] = 1
						# Add the tuple to a list
						neighbours.append((board[x], index, x - index))
						if board[x] == N-1:
							a = "100 --[" + str(x-index) + "]-> " + str(index)
							steps = len(levels)
							origin = index
							while (origin!=0):
								origin = [item for item in levels[steps - 1] if item[0] == origin][0]
								dice = origin[2]
								origin = origin[1]
								steps = steps - 1
								a = a + " --[" + str(dice) + "]-> " + str(origin)
							if verbose:
								print str(len(levels)) + "steps"
								print ' '.join(w[::-1] for w in a[::-1].split())
							return
		if neighbours != []:
			# Keep adding the list of neigbour tuples, to levels
			levels.append(neighbours)
	if not isCalled[N-1] and verbose:
		print "No path found"

if __name__ == "__main__":
	board = createBoard(101)
	modifiedDijkstra(101, board)
	