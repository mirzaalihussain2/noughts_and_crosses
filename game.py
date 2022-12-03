print("Hello world")

state_of_board = [["","",""], ["","",""], ["","",""]]

for row in state_of_board:
	for item in row:
		if item:
			print(item)
		else:
			print("__")
		if (row.index(item) == 0 or row.index(item) == 1):
			print(" | ")
