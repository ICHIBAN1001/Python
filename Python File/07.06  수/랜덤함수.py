# 랜덤함수
import random   # 랜덤함수를 사용하기위해 
                # 랜덤함수 모듈 import  <-필수

# 0 ~ 5 "실수" 랜덤 값
for value in range (10) :
    num = random.random() * 5
    print(num)

print("----------------------------------")

# 0 ~ 5 "정수" 랜덤 값
for value in range (10) :
    num = int(random.random() *5)
    print(num)


