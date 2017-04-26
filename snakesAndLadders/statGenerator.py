from minThrows import modifiedDijkstra, createBoard
from minThrows2 import sequenceSolver
import os
import time

if __name__ == "__main__":
	algo1 = []
	algo2 = []
	x = 1
	for file in os.listdir("./100x100inputs"):
	    if file.endswith(".txt"):
	    	while (x != 10):
	    		start = time.time()
		        board = createBoard(10001)
		        modifiedDijkstra(10001, board, False)
		        timeTaken = time.time() - start
		        algo1.append(timeTaken)
		        start = time.time()
		        board = createBoard(10001)
		        sequenceSolver(10001, board, False)
		        timeTaken = time.time() - start
		        algo2.append(timeTaken)
		        x = x+1
	print reduce(lambda x, y: x + y, algo1) / len(algo1)
	print reduce(lambda x, y: x + y, algo2) / len(algo2)