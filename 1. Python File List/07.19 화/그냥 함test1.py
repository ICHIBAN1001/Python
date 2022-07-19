import random

MyList = []

newlist = []


# while 로 같은거 안들어 오게 계속 무한 반복 
while len(MyList)< 25 :    # 0 ~24 개
    # 1,50 사이 수를 무작위로 돌리기
    Element_1 = random.randint(1,50) 
    # 리스트안에 요소가 안들어 있으면 넣기     
    if not Element_1 in MyList :
        MyList.append(Element_1)

# 1,50사이 순서대로 크기 잡아가면서 정렬
for index in range (1,50+1) :
    if index in MyList :
        newlist.append(index)

# 화면에 보이게 하기 
for value in range (len(newlist)) :
    Element_2 = newlist[value]
    print(Element_2, "\t", end= "" )
    if (value+1) %5 == 0 :
        print()

##### 출력부 
print()
print("最小値 : ",newlist[0])
print("中間地 : ",newlist[12])
print("最大値 : ",newlist[len(newlist)-1])