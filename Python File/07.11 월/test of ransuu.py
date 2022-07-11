#乱数



# 4. 
#   구간 별 히스토그램 정보 출력


# 1.  1 ~ 20 사이의 양의 정수중 난수 값 20 개 생성 후 List에 저장

import random

malist = []
for value in range (20):
    ran=int(random.random()*20)+1 
    malist.append(ran)
print(malist)

print("랜덤함수 :")
for value in range (len(malist)):
    element = malist[value]
    print("\t",element,end="")
    if value == (len(malist))//2-1: 
        print()
# ---------------------------------------------------------------------------------------------------------
print()
# 2. List 내 원소 값에 대한  합계, 평균, 최대 값, 최소 값 출력 

# 最小値 변수
Min = malist[value-1]
# 最大値 변수
Max = malist[value-1] 
# 合計 변수
sum = 0
# 반복적으로 리스트 안의 내용들을 뽑아낼 반복문 작성
for value in range (len(malist)) : 
    element = malist[value]
    sum += element

# 조건 식으로 最小 , 最大 구분하기
    # 最小 
    if Min < malist[value] :
        Min = Min
    else :
        Min = malist[value]

    # 最大
    if Max > malist[value] :
        Max = Max
    else :
        Max = malist[value]
   
print("最小値 : ",Min)
print("最大値 : ",Max)
print("合計 : ", sum)
print("平均 : ", sum/len(malist))

# ----------------------------------------------------------------------------------------------------------
# 3. List 내 중복 값과 중복 횟수 정보 출력

# 임의의 리스트 공간 작성 
elist1 = []
elist2 = []

# for 반복문으로 malist 안에 있는 원소들 하나씩 뽑기
# 뽑힌 원소들이 빈리스트와 대조를 이뤄


# ----------------------------------------------------------------------------------------------------------
# 4. List 내 중복 값과 중복 횟수 정보 출력



# c1 = 0
# c2 = 0
# c3 = 0
# c4 = 0

# for value in range (len(malist)) : 
#     element = malist[value]
#     if 0< element < 6 : 
#         c1 += 1
#     elif 5< element < 11 : 
#         c2 += 1
#     elif 10< element < 16 : 
#         c3 += 1
#     elif 15< element < 21 : 
#         c4 += 1

# print("1~5 : ", "*"*c1 )
# print("6~10 : ", "*"*c2 )
# print("11~15 : ", "*"*c3 )
# print("16~20 : ", "*"*c4 )