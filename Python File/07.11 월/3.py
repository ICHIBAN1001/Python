#乱数

# 1. 

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
# 2. 합계, 평균, 최대 값, 최소 값 출력

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
