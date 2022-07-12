#1. 전체를 반복으로 흐름을 제어할 반복문 작성
# while switch :
#     print("시도횟수 :",count)
#     print("정수 3개를 입력하세용~ ")
#     InputValue1 = int(input("첫 번째 정수 : ")) #  <- 정수 3개 입력할 곳
#     InputValue2 = int(input("두 번째 정수 : ")) #  <- 정수 3개 입력할 곳
#     InputValue3 = int(input("세 번째 정수 : ")) #  <- 정수 3개 입력할 곳
#     # 위의 입력 받은 값들을 리스트로 정렬
#     myList = [InputValue1 , InputValue2 , InputValue3]
#     print()




# n 수 만큼 입력 값을 받아 출력문 만들기

# n 번 변수 공간 작성
Number = int(input("몇개 입력 할래? : "))
malist = []

# 반복문 작성 
for value in range (1,Number+1) :
     kazu = input(str(value)+"번째 정수 :")
     malist.append(kazu)
# 입력받을 문장 만들기
print(malist)