# #프로그램명: 야구 게임 만들기
#------------------------------------------------------------------------------------------------------------------
# 0~9사이의 3개 정수를 random.randint() API를 이용하여 난수로 생성.
# -정수의 범위는 0~9사이
# -중복 값 없이 생성. 예) 2, 2, 6 X → 2중복
#------------------------------------------------------------------------------------------------------------------
#  게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
#  • 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력 (예외처리 X)
#  • 아래 경우 게임 Lose
#   – 시도 횟수 >= 5
#   – Strike out == 2
#  • 아래 경우 게임 Win
#   – 컴퓨터에서 생성 한 난수 값을 자리 순서대로 맞출 경우

import random

# 시도 횟수 카운트 ,입력문
count = 1

###################################################################################################################
#시도 횟수 알림 
print("시도횟수 :",count)
#0~9 사이 정수 입력 받기

print()
# 3개의 정수(난수)를 담을 리스트 작성
ransu = []

# 반복문으로 3개의 정수 뽑기 : 총 3개의 난수 생성 (범위는 3까지)
while len(ransu) < 3 :
    value = random.randint(0,9)
    if value not in ransu :
        ransu.append(value)
# Game 의 정수가 안 겹치게    
# print(ransu)
ransu = [3,1,2]
print(ransu)

###################################################################################################################

# 변수  Strike
Strike = 0
# 변수  Ball
Ball = 0
# 변수  Out
Out = 0

#while 전체 반복문 스위치 
switch = True

# 1. 전체를 반복으로 흐름을 제어할 반복문 작성
while switch :
    print("정수 3개를 입력하세용~ ")
    # InputValue1 = int(input("첫 번째 정수 : ")) #  <- 정수 3개 입력할 곳
    # InputValue2 = int(input("두 번째 정수 : ")) #  <- 정수 3개 입력할 곳
    # InputValue3 = int(input("세 번째 정수 : ")) #  <- 정수 3개 입력할 곳
# 위의 입력 받은 값들을 리스트로 정렬
    # myList = [InputValue1 , InputValue2 , InputValue3]
    myList = [3 , 1 , 2]
    
# [난수 값] 과 [입력 값] 비교
# 2. [난수 값] 을 for 반복문으로 하나씩 추출
        # 1. [입력 값] 을 for 반복문으로 하나씩 추출
    for index_inp in range (len(myList)) :
        inp = myList[index_inp]
        for index_ran in range (len(ransu)) :
            ran = ransu[index_ran]
        # < Strike >    
        # 2.1) 만약 "(난수)자릿수" and "난수 값" == "입력 값" 이면  -> Strike    
          # 2.1-1) 난수 값 = 입력 값
            if inp in ransu :    
                if ran == inp :
                    if index_inp == index_ran :
                        Strike += 1 
                if ran != inp :
                    if inp in ransu :        
                        if index_inp != index_ran :
                            Ball += 1
            if Strike>=1 or Ball>=1:
                continue
    if Strike == 0 and Ball == 0 :
        Out += 1

    # 반복문 횟수 제한    
    count += 1

# 시도 횟수 초과일경우  ->  count >=5  "or" Out == 2
    if  count >=5 or Out ==2 :
        print()
        print("게임횟수 초과")
        print("아까비~~~졌네용..")
        print("정답은 : " ,ransu[0],ransu[1],ransu[2], "입니다." )
        switch = False 
    #조건에 따른 출력문
    print("스트라이크 :", Strike)
    print("볼 :", Ball)
    print("아웃 :", Out)
    Strike = 0 
    Ball = 0 