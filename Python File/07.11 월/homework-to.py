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
print("정수 3개를 입력하세용~ ")


InputValue1 = int(input("")) #  <- 정수 3개 입력할 곳
InputValue2 = int(input("")) #  <- 정수 3개 입력할 곳
InputValue3 = int(input("")) #  <- 정수 3개 입력할 곳

List = [InputValue1 , InputValue2 , InputValue3]

# 3개의 정수를 담을 리스트 작성
RanSu = []

# 반복문으로 3개의 정수 뽑기 : 총 3개의 난수 생성 (범위는 3까지)
while len(RanSu) < 3 :
    value = random.randint(0,9)
    if value not in RanSu :
        RanSu.append(value)
# Game 의 정수가 안 겹치게    
print(RanSu)

###################################################################################################################

switch = True
# 변수  Strike
Strike = 0
# 변수  Ball
Ball = 0
# 변수  Out
Out = 0

# 1. 전체를 반복으로 흐름을 제어할 반복문 작성
while switch :
# 해당 값 입력받고 , 경우에 따른 조건  
    # for 문으로 안에 있는 수 뽑아내기 
    for value1 in range (len(RanSu)) :
        element1 = RanSu[value1]
        for value2 in range(len(List)) :
            element2 = List[element2] 
            if element1 == element2 :
                Strike += 1

    # Strike 일 경우   ,  Strike : 자릿수 AND “난수 값 == 입력 값” 일 경우
            
    # Ball 일 경우 
   
        Ball += 1
    # Out 일 경우 
    
        Out += 1
# 시도 횟수 초과일경우  ->  count >=5
    if  count >=5 :
        switch = False 

    # 반복문 횟수 제한    
    count += 1
