# # 1. 문구 출력 : 입력 문자열의 줄(Line) 수를 입력하세요! 
# LineNumber = int(input("입력 문자열의 줄(Line) 수를 입력하세요! : "))

# # 1.1. 영문의 문자열 키보드로 입력 받아 리스트에 저장
# Word = ""           # "문자열"로  담을  변수
# WordList = []       # "리스트"로  담을  변수

# # 2. 입력 받기  for 반복문 => 1의 수만큼 반복
# for Value in range (LineNumber) :
#     InputValue = input(str(Value+1) +" 번째 라인의 문자열을 입력하세요. : ")
#     Word += InputValue+" "               # 문자열로 계산
#     WordList.append(InputValue)      # 리스트로 계산
    
# # 3. 검색할 문자열 확인  (인덱스로 확인)
Search = input("검색 할 문자열을 입력하세요. : ")

Word = "hello world hello worldddd hello kkk"           # "문자열"로  담을  변수

WordList = ['hello world', 'hello worldddd hello', 'kkk']       # "리스트"로  담을  변수

################################################  리스트 저장  ################################################ 


indexlist = ""   # 알파벳 담을 변수

search_count = 0 # 검색횟수 변수

# 4. for 반복문으로 WordList 요소 하나씩 꺼내기 
for row in range (len(WordList)) :  # index = [0] [1] [2]
    for col in range (len(WordList[row])) :
        indexlist += WordList[row][col]  

# 6. 검색된 횟수
# WordList 리스트 각 요소안에 Search가 있으면
        # 알파벳 담을 변수 / 한번 드가면 카운팅 
        if Search in WordList or Search in indexlist :
            search_count += 1

print(search_count)

########################################################################
# 7. 총 단어 수
# WordList 안에 " " 에 +1

########################################################################
#     # 5. 검색된 라인수
#     # WordList 안에 Search 가 있으면 
#         if " " in indexlist and Search in indexlist:
#             if (row+1) not in linesu :
#                 linesu += str(row+1)
#             if Search  in WordList[(-row+1)] :
#                 if "," not in linesu :
#                     linesu += ","    
#     # for 로 한 바퀴 돌면 해당 변수 리셋 시키기  
#     indexlist = "" 
# print(linesu)
       
 










#################################################################################################################


# temp = [ "hello", "king", "car" ]

# print(len(temp)) 

# print(len(temp[0])) 
# print(len(temp[1])) 
# print(len(temp[2])) 

# print(temp[1][3])

# for row in range(len(temp)): # row 0 -> 2
#     for col in range(len(temp[row])): # row : 0, row : 1, row : 2
#         print(temp[row][col], " : ", end="")
        
#     print()

    
#################################################################################################################
