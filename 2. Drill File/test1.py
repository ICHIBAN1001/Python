import random 

mylist = []  # 25개 입력 받기 

# 숫자 리스트에 정렬 
while len(mylist) < 25 :
    element = random.randint(1,50) 
    if not element in mylist :
        mylist.append(element)
mylist.sort()

# 5 x 5 만들기
for index in range (len(mylist)) : 
    element = mylist[index] 
    print(element,"\t", end="")
    if (index+1) % 5 == 0 :
        print()  

# mylist = []
# 2차원 리스트 만들기
Dimensionlist = [[],[],[],[],[]] # 1 2 3 4 5

count = 0
Lcount = 0
while count <len(mylist) :

    mylist.append(Dimensionlist[Lcount])

    if len(Dimensionlist[Lcount]) == 5 :
        Lcount += 1
    count += 1
    
print(Dimensionlist)

# 열

# 행

# 전체
print()
print("最小値","\t",mylist[0])
print("最大値""\t",mylist[12])
print("中間値""\t",mylist[len(mylist)-1])