
n = int (input("Please enter the number of this triangle's rows you want to be showen as an input: "))

Khayyam_triangle = [[1]]

for i in range (n+1):
    
    if i > 1:
        Khayyam_triangle.append(i*[1])

        for j in range (len(Khayyam_triangle)):
            
            if j > 1:
        
                Khayyam_triangle [i-1][j-1] = Khayyam_triangle [i-2][j-2] + Khayyam_triangle [i-2][j-1]

for row in Khayyam_triangle:
    print(row)