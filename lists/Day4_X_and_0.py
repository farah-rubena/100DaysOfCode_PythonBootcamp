row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

x_input = input("Where do you want to put the mark 'X'?: ")
vertical_x = int(x_input[0])
horizontal_x = int(x_input[1])
map[vertical_x - 1][vertical_x - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

y_input = input("Where do you want to put the mark 'Y'?: ")
vertical_y = int(y_input[0])
horizontal_y = int(y_input[1])
map[vertical_y - 1][vertical_y - 1] = "Y"
print(f"{row1}\n{row2}\n{row3}")
