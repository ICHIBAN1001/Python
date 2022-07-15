# 2차원 배열(리스트)

temp = [ "hello", "king", "car" ]

print(len(temp)) 

print(len(temp[0])) 
print(len(temp[1])) 
print(len(temp[2])) 

print(temp[1][3])

for row in range(len(temp)): # row 0 -> 2
    for col in range(len(temp[row])): # row : 0, row : 1, row : 2
        print(temp[row][col], " : ", end="")
        
    print()



