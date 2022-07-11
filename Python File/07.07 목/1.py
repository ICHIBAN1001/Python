# 랜덤 함수

# 1.  Clear   0000
#   1 ~ 20 사이의 양의 정수중 
#   난수 값 20 개 생성 후
#   List에 저장 
#----------------------------------------------------------------
# 2.
#   List 내 원소 값에 대한 
#   합계, 평균, 최대 값, 최소 값 출력  
#----------------------------------------------------------------
# 3. 
#   List 내 중복 값과 중복 횟수 정보 출력

# 4. 
#   구간 별 히스토그램 정보 출력


# < 1번 >

# random 함수를 쓰기위해 import 선언! 
import random
# List 공간 만들기
MyList = [ ]
# 1-1. 1~20 사이를 만들 반복문(for) 작성
for Value in range (20) :
# 1-2. 난수 값 무작위로 20개 생성
    ransuu=int(random.random() * 20) +1 
# 1-3.List 공간 만들기 
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

#2 번 으로 가기전에 띄워 쓰기 
print()
# < 2번 >

# 반복 적으로 list 안에 있는 값들을 추출
# 最小 값 
Max = MyList[RandomValue-1]
# 最大 값 
Min =  MyList[RandomValue-1]
# 합계 담을 변수 공간 
Sum = 0
for RandomValue in range(len(MyList)) :
    atai = MyList[RandomValue]
    Sum += atai
    # 最小
    if Min < MyList[RandomValue] :
       Min = Min
    else :
       Min = MyList[RandomValue]

    # 最大
    if Max >= MyList[RandomValue] :
       Max = Max 
    else :
       Max = MyList[RandomValue]
# for Value in MyList : 
    
#  2-1. 최소 값
print("최소 값\t:",Min)
#  2-2. 최대 값
print("최대 값\t:",Max)
#  2-3. 합계
print("합계\t:",Sum)
#  2-4. 평균
print("평균\t:",Sum/len(MyList))

#----------------------------------------------------------------

# < 3번 >


# 출력 단어 ->  중복 값   중복 회수
print("중복 값    중복 회수")

# while 스위치
flag = True
# 카운트
count = 0
# 중복 값 저장 할 변수 공간 만들기 
duplicated =0
# 반복문 :리스트안에 있는 요소들을 반복적으로 확인 
while flag :
# 조건문 : 리스트안의 원소가 같으면 몇 번 같은지 카운트 
    if MyList[count] in MyList == :
        # 중복일 경우 중복값 1씩 더하기 
        duplicated += 1
        # 중복 값 프린트 
        print("  ",MyList[count],"\t\t",end="" )
        print(duplicated)
        count +=1
        if count== 20:
            falg = False
    else : 
        count +=1
        if count== 20:
            falg = False