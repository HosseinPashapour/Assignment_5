
row = int ( input (" Please enter the number of rows : "))
column = int ( input (" Please enter the number of columns : "))

def print_chess(row, column):
    for i in range(row):
        for j in range(column):
            if (i + j) % 2 == 0:
                print("⬜", end="")
            else:
                print("⬛", end="")
        print()

print_chess(row, column)
