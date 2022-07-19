import random

MyList = []         # 무작위로 받는 리스트
SortingList = []    # 정렬 리스트
row_List = [[],[],[],[],[]]   # [ [0] , [1] , [2] , [3] , [4] ]   -> 5개


# 1. while 로 같은거 안들어 오게 계속 무한 반복 
while len(MyList)< 25 :    # 0 ~24 개
    # 1,50 사이 수를 무작위로 돌리기
    Element_1 = random.randint(1,50) 
    # 리스트안에 요소가 안들어 있으면 넣기     
    if not Element_1 in MyList :
        MyList.append(Element_1)
#################################################

# 2. 1,50사이 순서대로 크기 잡아가면서 정렬
# == MyList.sort()
for index in range (1,50+1) :
    if index in MyList :
        SortingList.append(index)


#################################################
# 3. 화면 출력용 
for value in range (len(SortingList)) :
    # 원소 추출
    Element_2 = SortingList[value]

    print(Element_2, "\t", end= "" )

    if (value+1) %5 == 0 :
        print()
#################################################


# 4. 2차원 리스트 
count = 0  # 전체 카운트
sorting_count = 0 # 솔팅 카운트

# 리스트 안에 리스트가 5개 까지 반복
while count < len(SortingList) :
    # 요소 뽑기
    row_List[sorting_count].append(SortingList[count])
    if len(row_List[sorting_count]) == 5 :
        sorting_count += 1
    count += 1
###################################



##### ##############출력부 ############################

####### 열 ######
print()
print("열")
# 최소 값
print("최소값","\t",end="" )
for index in range (len(row_List[0])) :
    print(row_List[0][index],"\t" , end="")
print()

#최대 값
print("최대값","\t",end="" )
for index in range (len(row_List[4])) :
    print(row_List[4][index],"\t" , end="")
print()   
#  중간 값
print("중간값","\t",end="" )
for index in range (len(row_List[4])) :
    print(row_List[len(row_List)//2][index],"\t" , end="")
print()

####### 열 ######
print()
print("행")
print("최소값", "\t\t","최대값", "\t","중간값")



# for row in range (len(row_List)) :  # 0 ~ 4  ->  5개
#     for col in range (len(row_List)) :
#         if row == 0 or 
#         print (row_List[row][col])  
    
# print("最小値 : ",SortingList[0])
# print("中間値 : ",SortingList[12])
# print("最大値 : ",SortingList[len(SortingList)-1])