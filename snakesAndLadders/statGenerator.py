from minThrows import modifiedDijkstra, createBoard
from minThrows2 import sequenceSolver
import os

if __name__ == "__main__":
	for file in os.listdir("./100x100inputs"):
	    if file.endswith(".txt"):
	        board = createBoard(10001)
	        sequenceSolver(10001, board)
