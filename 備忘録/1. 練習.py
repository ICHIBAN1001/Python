# 1. 문구 출력 : 입력 문자열의 줄(Line) 수를 입력하세요! 
LineNumber = int(input("입력 문자열의 줄(Line) 수를 입력하세요! : "))
# 영문의 문자열 키보드로 입력 받아 리스트에 저장
Word = ""           # 문자열로 계산
WordList = []       # 리스트로 계산
# 입력 받기  for 반복문 => 1의 수만큼 반복
for Value in range (LineNumber) :
    InputValue = input(str(Value+1) +" 번째 라인의 문자열을 입력하세요. : ")
    Word += InputValue               # 문자열로 계산
    WordList.append(InputValue)      # 리스트로 계산
    
#검색할 문자열 확인  (인덱스로 확인)
Search = input("검색 할 문자열을 입력하세요. : ")
print(Word)
print(WordList)
################################################  리스트 저장 

linesu = ""
# for 반복문으로 WordList 요소 하나씩 꺼내기 
for index in range (len(WordList)) :
    Element = WordList[index]  # ["qwwqw","qwwqw","qwwqw"]     Element = "qwwqw"
    if Element in WordList :
        linesu += (index+1)  
print(linesu)
# 검색된 라인수
    
# 검색된 횟수

#총 단어 수

    
