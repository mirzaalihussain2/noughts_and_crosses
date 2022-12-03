state_of_board_list = [["","",""], ["","",""], ["","",""]]
state_of_board_string = ["", "", ""]

for row in state_of_board_list:
	for item in row:
		if item:
			state_of_board_string[state_of_board_list.index(row)] += item
		elif item == False:
			state_of_board_string[state_of_board_list.index(row)] += "--"
		if (row.index(item) == 0 or row.index(item) == 1):
			state_of_board_string[state_of_board_list.index(row)] += " | "

print("State of board list")
print(state_of_board_list)

print("\nState of board string")
print(state_of_board_string)
