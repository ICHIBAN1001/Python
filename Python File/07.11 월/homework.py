 #프로그램명: 야구 게임 만들기

# 0~9사이의 3개 정수를 random.randint() API를 이용하여 난수로 생성.
# -정수의 범위는 0~9사이
# -중복 값 없이 생성. 예) 2, 2, 6 X → 2중복

# 1) 0~9 사이의 3개 정수를 랜덤으로 난수 생성  
#     단.  중복 하면 안됨

import random

# 난수를 저장 할 리스트 작성
myList = []
# while 스위치
flag = True 

# 3개의 정수를 받기 위해 3번 반복 
for Value in range (3) :
    ransu = random.randint(0,9)
    if ransu not in myList:
        myList.append(ransu)
# 반복 되지 않게 작성
    else :
        while flag :
            # 리스트 안에 있을 때
            if ransu in myList :
                ransu = random.randint(0,9)
                myList.append(ransu)
            # 리스트 안에 없을 때
            else : 
                flag = False
        # 조건 ransu == element 같으면 다시 뺑뻉이
print(myList)