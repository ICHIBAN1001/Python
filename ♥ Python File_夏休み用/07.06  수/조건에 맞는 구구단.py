# 1)	메뉴 우선 출력 후 키보드로부터 정수 값 입력
# 2)	메뉴에서 “1”선택 시 구구단 출력, “2”인 경우 잘못 입력하셨습니다. 다시입력하세요. 출력 후 프로그램 종료
# 3)	메뉴에서 “1” 또는 “2”이외의 값이 입력될 경우, Error Msg. 출력 후 재입력
# 4)	“구구단 출력” 메뉴 선택 시 출력 할 단을 키보드로부터 입력
# 4-1	출력 유효 단은 2 ~ 9
# 4-2	2 ~ 9단 이외의 값이 들어올 경우 Error Msg. 출력 후 재입력
# 5)	출력 값은 반드시 아래 형식 준수

# 스위치 작성
flag = True
# 전체 반복시킬 while 문 작성
while flag :
    # 메뉴 처음 시작 문구 작성
    print("------------------------")
    print("1. 구구단 출력"  )
    print("2. 프로그램 종료"  )
    print("------------------------")
# 
    # 키보드로 구구단 작성할 정수 값 입력 받기
    Menue = int(input("")) 

    # 조건식  1 or 2
    # 1. 메뉴 1 을 선택 : 구구단 출력
    if Menue == 1 :
        # 맞을경우 아닐경우를 반복적으로 돌릴 반복문
        while Menue == 1:    
        # 1-1. 출력할 단 키보드로 입력받기
            Dan = int(input("출력할 구구단의 단을 입력하세요. 구구단의 단은 2~9 사이 입력 : "))
        # 1-2. 출력 이외의 단 입력 : "2~9사이 정수를 입력해주세요."
            if 2<=Dan <=9 :
                # 구구단에서 1~9까지 반복할 반복문 만들기
                for Dan_value in range (1,9+1):
                    print(Dan ,"X" ,Dan_value ,"=", Dan*Dan_value )
                break
    # 2. 메뉴에 없는 숫자 선택 를 선택 : "잘못 입력하셨습니다. 다시입력하세요." 출력
            else :
                print("잘못 입력하셨습니다. 다시입력하세요.") 


    # 3. 2번 선택한경우 : "이용해 주셔서 감사합니다"
    else :
        print("이용해 주셔서 감사합니다")
        # 스위치 끄기
        flag = False