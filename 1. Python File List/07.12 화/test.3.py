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
#------------------------------------------------------------------------------------------------------------------

# import random 으로 random 함수 부르기
import random

# random 함수를 담을 리스트 변수 작성 (2개 이상)
ransulist = []
# 반복문으로 범위 지정 개수 만큼 생성
while len(ransulist) < 3 :
    betty = int(random.random()*10)
    if betty not in ransulist :
        ransulist.append(betty)


# 시도횟수 변수
count = 1
# while 반복문 스위치 
flag = True 
# while 전체 반복 흐름 제어 
while flag :

    #출력기
    print("시도횟수 : ",count)
    print("정수 3개를 입력 하세요")

    # 3개의 정수를 입력 받기 
    mylist = []
    for value in range (len(ransulist)) :   # len(ransulist) = 3
        mylist.append(int(input(str(value+1)+"번째 정수를 입력하세요 :")))

    # Strike, Ball, Out 변수 공간
    Strike = 0
    Ball = 0
    Out = 0
    # 입력 받은 값들을 ransulist 의 요소 값들과 비교
    for index in range (len(mylist)) :
        element = mylist[index]
    # Strike, Ball, Out 조건식 만들기 
        # Strike / Ball
        if element in ransulist :
            # Strike
            if element == ransulist[index] :
                Strike += 1
            # Ball    
            else :
                Ball += 1
        # Out        
        else :
            Out += 1

    # Strike, Ball 리셋 
    Strike = 0
    Ball = 0

    
                