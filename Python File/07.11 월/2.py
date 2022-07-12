ransu = []

import random
# 반복문으로 3개의 정수 뽑기 : 총 3개의 난수 생성 (범위는 3까지)
while len(ransu) < 3 :
    value = random.randint(0,9)
    if value not in ransu :
        ransu.append(value)
# Game 의 정수가 안 겹치게    
# print(ransu)
ransu = [3,1,2]
print("난수",ransu)
################################################################
myList = [3,6 ,7]
print("입력값",myList)

Strike = 0
Ball = 0
Out = 0
count = 0
# 반복문
for index in range (len(myList)) :
    element = myList[index]
    # strike,ball  /조건문으로 판정 값 선택
    if element in ransu : 
        # strike
        if element == ransu[index] :
            Strike += 1
        #ball 
        elif element != ransu[index] : 
            Ball += 1
    # Out 
    else :
        if Strike == 0 and  Ball == 0 :
            Out += 1
    # count     
    count += 1
    if  count >=5 or Out ==2 :
        print()
        print("게임횟수 초과")
        print("아까비~~~졌네용..")
        print("정답은 : " ,ransu[0],ransu[1],ransu[2], "입니다." )
        switch = False 
    #조건에 따른 출력문
        Strike = 0 
        Ball = 0 
print("스트라이크 :", Strike)
print("볼 :", Ball)
print("아웃 :", Out)
