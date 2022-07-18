# 1. 문자열 키보드로 입력 받기
# 2. 입력 받은 문자열 리스트에 저장
# 3. 키보드로 다시 입력 받아 1.에 있는 문자열 있는지 확인


# 문자열의 라인 수 입력 받기
Line_numer = int(input("입력 문자열의 줄(Line) 수를 입력하세요! : ")) 

# 입력 받은 문자열을 담을  ※1)包括  리스트 작성※
InputValue_list = []

# 입력 받은 라인 수 만큼 반복해서 
for inner_index in range (Line_numer) : # 0 1 2 
    InputValue_list.append([])   # ※2)內部 리스트 작성※

print(InputValue_list)