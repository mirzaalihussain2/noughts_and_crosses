state_of_board_list = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8]
	]

state_of_board_string = ["", "", ""]

i = 0
while i < len(state_of_board_list):
	j = 0
	while j < len(state_of_board_string):
		if j == 0:
			state_of_board_string[i] += "  "
		state_of_board_string[i] += str(state_of_board_list[i][j])
		if j < 2:
			state_of_board_string[i] += "  |  "
		j += 1
	i += 1

print("     |     |     ")

k = 0
while k < (len(state_of_board_string) - 1):
	print(state_of_board_string[k])
	print("-----|-----|-----")
	k += 1

print(state_of_board_string[-1])
print("     |     |     ")
print("\n\n")


"""
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
