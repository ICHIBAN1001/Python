# - 랜덤함수를 이용하여 아래 프로그램을 작성하라 
#  1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
#  2. List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값 출력
#  3. List 내 중복 값과 중복 횟수 정보 출력 [ 아래 출력 결과 참조 ]
#  4. 구간 별 히스토그램 정보 출력 [ 아래 출력 결과 참조 ]
# 랜덤 선언 
import random
# 리스트 / 변수 생성
mylist = []
count = 0 # -> 반복 횟수
sum_1 = 0 # -> 합계
count_1 = 0 # -> 1 ~ 5   "*"
count_2 = 0 # -> 6 ~ 10  "*"
count_3 = 0 # -> 11 ~ 15 "*"
count_4 = 0 # -> 16 ~ 20 "*"
# (1) 랜덤 값 프로그램 생성
# -> 반복문 생성 (20번 반복)  
# -> 난수 20개 생성 / 리스트에 난수 값 저장
for turn in range(20):
    random_num = random.randint(1,20)
    mylist.append (random_num)
# 리스트 수 만큼 반복 
# count+=1 -> 반복 횟수 증가 
# count 값이 10일 때 공백 생성 및 10번 째 반복 숫자 출력
print("랜덤 값:")
for random_num in mylist:
    count+=1
    if count == 10:
        print("\t",random_num)
    else:
        print("\t",random_num,end="")
print()
# (2) 최소/최대/합계/평균 프로그램 생성
# 랜덤 값 변수 생성 -> 리스트만 담을 수 없어서 [] 
min = mylist[random_num]
max = mylist[random_num]
# for문 이용해서 반복
for random_num in range(20):
# if문 이용 -> True 일시 최소/최대 값 고정 / False일시 최소/최대 값으로 변경
# -> 리스트안에 숫자는 난수 
    if min < mylist[random_num]:
        min = min
    else:
        min = mylist[random_num]
    if max > mylist[random_num]:
        max = max
    else:
        max = mylist[random_num]
# 합계 
    sum_2 = mylist[random_num]
    sum_1 += sum_2
# 평균 
    avg = sum_1 / len(mylist)
# 결과 값 출력
print("최소 값:",min)
print("최대 값:",max)
print("합계   :",sum_1)
print("평균   :",avg)
# (3) 중복 값 / 중복 횟수 프로그램 생성
print("중복 값","","중복 횟수")
# 중복 횟수를 나타내는 변수 생성
count = 0
# 중복 값을 나타내는 반복문 생성
# 난수를 담을 반복문 생성
for duplication in range(20):
    for random_num in mylist:
# if문(1) True일시 중복 횟수 +1
        if duplication == random_num:
# if문(2) True일시 True일시 값 출력
            count+=1
    if count >=2:
        print("  ",duplication,"\t   ",count)
# 전체 반복문 한 바퀴 돌았을 시 중복 횟수 초기화
    count = 0

# (4) 구간별 히스토리
# 난수 반복문 생성 
for random_num in mylist:
# -> if문 이용 -> 구간별 수에 맞을 시 (count) +1 증가 
    if random_num <=5:
        count_1+=1
    elif random_num >= 6 and random_num <=10: 
        count_2+=1
    elif random_num >= 11 and random_num <=15: 
        count_3+=1
    else:
        count_4+=1
# * X (count) <--- 각 구간별 갯수가 들어있음
# 결과 값 출력
print("구간별 히스토그램")
print("1  ~  5 :","*"*count_1)
print("6  ~ 10 :","*"*count_2)
print("11 ~ 15 :","*"*count_3)
print("16 ~ 20 :","*"*count_4)

