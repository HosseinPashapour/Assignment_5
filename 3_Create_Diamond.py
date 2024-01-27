n = int(input("Enter the size  : "))
def star(n):
    for i in range(n+1):
        print(" " * (n - i), end="")
        print("* " * i)

    for i in range(n-1,0,-1):
        print(" " * (n - i), end="")
        print("* " * i)
        
star(n)
