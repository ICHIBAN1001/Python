# 랜덤 함수

# 1.  Clear   0000
#   1 ~ 20 사이의 양의 정수중 
#   난수 값 20 개 생성 후
#   List에 저장 
#----------------------------------------------------------------
# 2.
#   List 내 원소 값에 대한 
#   합계, 평균, 최대 값, 최소 값 출력  
# 
# 3. 
#   List 내 중복 값과 중복 횟수 정보 출력

# 4. 
#   구간 별 히스토그램 정보 출력


# < 1번 >

# random 함수를 쓰기위해 import 선언! 
import random
# 3.List 공간 만들기

MyList = [ ]
# 1. 1~20 사이를 만들 반복문(for) 작성
for Value in range (20) :
# 2. 난수 값 무작위로 20개 생성
    ransuu=int(random.random() * 20) +1 
# 3. 3.List 공간 만들기 
    MyList.append(ransuu)   # ex) MyList = [16, 15, 9, 9, 9,..... ]

# 출력문 :랜덤 값       
print("랜덤 값 : ")
# 반복해서 랜덤 값을 뽑을 
for RandomValue in range(len(MyList)) :
    result = MyList[RandomValue]
    print("\t ",result, " ", end="")
    if RandomValue == len(MyList)//2-1 :
        print ()

#----------------------------------------------------------------

# < 2번 >

#   List 내 원소 값에 대한 
#   합계, 평균, 최대 값, 최소 값 출력  

# 最小 값 
Max = 0
# 最大 값 
Min = 0
# 합계 담을 변수 공간 
Sum = 0
# 반복 적으로 list 안에 있는 값들을 추출
# for Value in MyList : 
    
#  1. 합계, 2. 평균, 3. 최대 값, 4. 최소 값