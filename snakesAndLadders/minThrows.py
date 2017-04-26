# Board stores the squaremappings - ladder bottom->top, snake mouth->tail
board = [i for i in range(0,101)]

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
snakes = int(inputFile[ladders+1].strip("\n"))
for x in range(ladders + 1, ladders + 1 + snakes):
	snakeHead = int(inputFile[x + 1].split(" ")[0])
	snakeTail = int(inputFile[x + 1].strip("\n").split(" ")[1])
	board[snakeHead] = snakeTail

isCalled = [0 for i in range(0,101)]

levels = []

def minThrows():
	for level in levels:
		neighbours = []
		for some_tuple in level:
			index, path, dice = some_tuple
			for x in range (index + 1, index + 7):
				if x <= 100:
					if not isCalled[board[x]]:
						isCalled[board[x]] = 1
						new_path = list(path)
						new_path.append(board[x])
						new_dice = list(dice)
						new_dice.append(x - index)
						some_other_tuple = (board[x], new_path, new_dice)
						neighbours.append(some_other_tuple)
						if board[x] == 100:
							a = str(new_path[0])
							for x in range (0, len(new_dice)):
								a += " --[" + str(new_dice[x]) + "]-> " + str(new_path[1 + x])
							print "Shortest path is " + str(len(new_dice)) + " steps"
							print a
							return
		if neighbours != []:
			levels.append(neighbours)

if __name__ == "__main__":
	isCalled[0] = 1
	levels.append([(0, [0], [])])
	minThrows()
	if not isCalled[100]:
		print "No path found"