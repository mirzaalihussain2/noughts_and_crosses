state_of_board_list = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8]
	]

state_of_board_list = [
	["","x","o"],
	["x","o","x"],
	["","x","o"]
	]

state_of_board_string = ["", "", ""]

i = 0
while i < len(state_of_board_list):
	for item in state_of_board_list[i]:
		if item:
			state_of_board_string[i] += item
		elif item == False:


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
"""
