# 1. 문자열 키보드로 입력 받기
# 2. 입력 받은 문자열 리스트에 저장
# 3. 키보드로 다시 입력 받아 1.에 있는 문자열 있는지 확인


# 문자열의 라인 수 입력 받기
Line = int(input("입력 문자열의 줄(Line) 수를 입력하세요! : ")) 

# 입력 받은 문자열을 담을  ※1)包括  리스트 작성※
Line_list = []
Word = "" # 단어로 만들어지면 단어를 담을 변수

Blank = " " # 공백 변수

Total_words = 0 

# 입력 받은 "Line" 만큼 반복해서 
for inner_index in range (Line) : # 0 1 2 
    Line_list.append([])   # [] [] []
    # 입력받은 알파벳들 하나의 문자로 저장하기 
    Word = ""

    # 문자열 입력 받기 
    Letter = input(str(inner_index+1)+"번째 라인의 문자열을 입력하세요. : ")

   

  

    # ※2)內部 리스트 작성※
    for Letter_index in range (len(Letter)) :
        # Letter 원소 알파벳 하나 씩 추출 
        Element = Letter[Letter_index]
        # 조건식 : 만약에 Word 안에 글자면
        if Element.isalpha() :
            Word += Element
        
            # 마지막 요소일 경우
            if Letter_index == len(Letter)-1 :
                Line_list[inner_index].append(Word)
                Total_words += 1

        # 조건식 : 만약에 Word 안에 공백이면       
        else :
            # 문자 들어오고나서 공백이 들어올 경우 
            if len(Word) >= 1 :
                Line_list[inner_index].append(Word)
                Total_words += 1
            #처음에 바로 공백이 들어올 경우    
            Word = ""
################################################################################################        
Searching = input("探したい単語は？ : ")      


################################################################################################
             
print(Line_list)
print("라인 수 ", )
print("Total_words : ",Total_words)

