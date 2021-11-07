from enum import Enum


class result(Enum):
	draw = 1
	xWon = 2
	oWon = 3
	noResult = 4


def printCount(tttboard, tttsize):
	string = ""
	for i in range(tttsize*4+1):
		string += "-"
	count = 1
	print(string)
	for i in range(tttsize):
		print("|", end="")
		for j in range(tttsize):
			if tttboard[i][j] != "-":
				print(f" {tttboard[i][j]} ", end="|")
			else:
				print(f"00{count}" if count < 10 else f"0{count}", end="|")
			count += 1
		print("")
		print(string)
	print("")
	print("")


def checkForGameEnd(tttboard, tttsize):
	#! diagonal
	xCount = 0
	oCount = 0
	xCount1 = 0
	oCount1 = 0
	for i in range(tttsize):
		if tttboard[i][i] == "X": xCount += 1
		if tttboard[i][i] == "O": oCount += 1
		if tttboard[tttsize-i-1][i] == "X": xCount1 += 1
		if tttboard[i][tttsize-i-1] == "O": oCount1 += 1
	if(xCount == tttsize or xCount1 == tttsize): return result.xWon
	if(oCount == tttsize or oCount1 == tttsize): return result.oWon

	#! horizontal & vertical
	for i in range(tttsize):
		xCount = 0
		oCount = 0
		xCount1 = 0
		oCount1 = 0
		for j in range(tttsize):
			if tttboard[i][j] == "X": xCount += 1
			if tttboard[i][j] == "O": oCount += 1
			if tttboard[j][i] == "X": xCount1 += 1
			if tttboard[j][i] == "O": oCount1 += 1

		if(xCount == tttsize or xCount1 == tttsize): return result.xWon
		if(oCount == tttsize or oCount1 == tttsize): return result.oWon

	full = True
	for i in tttboard:
		for j in i:
			if(j == "-"):
				full = False
				break
	if full: return result.draw

	return result.noResult


size = 3
try:
	size = int(input("What size of the board do you want (maximum 100, minimum 3)?"))
except ValueError:
	print("That's not a number!")
	exit()
size = max(min(size, 100), 3)

print(f"Sure! You will be playing on a {size} by {size} board!")

board = []

for i in range(size):
	board.append([])
	for j in range(size):
		board[i].append("-")

player = 'O'

while True:
	if player == 'X':
		player = 'O'
	else:
		player = 'X'
	print("\n\n")
	print(f"It's {player}'s turn!")
	place = 0
	while True:
		try:
			print("Here is your board:\n\n")
			printCount(board, size)
			place = int(input("Which square do you want to put your marker on?")) - 1
			if(place >= size*size):
				print("Too large!")
				continue
			yCoordinate = place//size;
			xCoordinate = place - yCoordinate*size
			if board[yCoordinate][xCoordinate] == "-":
				#! Valid
				board[yCoordinate][xCoordinate] = player
				res = checkForGameEnd(board, size)
				if(res == result.noResult): break
				print("")
				print("Final Board!")
				printCount(board, size)
				if (res == result.draw): print("Draw!")
				elif(res == result.oWon): print("O Won!")
				elif(res == result.xWon): print("X Won!")
				exit()
				break
			else:
				print("Place has already been taken!")
		except ValueError:
			print("That's not a number!")
