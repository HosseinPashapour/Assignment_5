
row = int ( input (" Please enter the number of rows : "))
column = int ( input (" Please enter the number of columns : "))
def multi_table (row, column):

    count = 1

    for i in range (row+1):
        print ('\033[2m' + str(i) + '\033[0m', end=" ")

    while count <= row:
        print ("")
        for i in range (column+1):
            if i==0:
                print ('\033[2m' + str(count) + '\033[0m', end=" ")
            else:
                ans = i * (count)
                print (ans, end=" ")
                
        count = count+1

multi_table (row, column)