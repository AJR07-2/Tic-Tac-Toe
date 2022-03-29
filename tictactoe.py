from enum import Enum

# different results that could happen
class result(Enum):
	draw = 1
	xWon = 2
	oWon = 3
	noResult = 4

# code to manage formatting for board printing
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


# code that utilises the enum result to check whether the game has ended or not
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
# querying the size of the board
try:
	size = int(input("What size of the board do you want (maximum 9, minimum 3) ?"))
except ValueError:
	print("That's not a number!")
	exit()
size = max(min(size, 9), 3)

print(f"Sure! You will be playing on a {size} by {size} board!")

board = []

for i in range(size):
	board.append([])
	for j in range(size):
		board[i].append("-")

player = 'O'

# driver code
while True:
	if player == 'X':
		player = 'O'
	else:
		player = 'X'
	print("\n\n")
	print(f"It's {player}'s turn!")
	place = 0
	
	# validity checking using try catch
	while True:
		try:
			# main code to check for validity
			print("Here is your board:\n\n")
			printCount(board, size)
			place = int(input("Which square do you want to put your marker on?")) - 1
			if(place >= size*size):
				print("Too large!")
				continue
			yCoordinate = place//size;
			xCoordinate = place - yCoordinate*size
			if board[yCoordinate][xCoordinate] == "-":
				#! Valid Input
				board[yCoordinate][xCoordinate] = player
				res = checkForGameEnd(board, size)
				if(res == result.noResult): break
				print("")
				print("Final Board!")

				# printing the board
				printCount(board, size)

				# printing the results of the round (if there are one)
				if (res == result.draw): print("Draw!")
				elif(res == result.oWon): print("O Won!")
				elif(res == result.xWon): print("X Won!")
				exit()
				
			else:
				print("Place has already been taken!")
		except ValueError:
			print("That's not a number!")
