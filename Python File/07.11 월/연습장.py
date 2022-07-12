#연습장

# [난수 값] 과 [입력 값] 비교
# 2. [난수 값] 을 for 반복문으로 하나씩 추출
        # 1. [입력 값] 을 for 반복문으로 하나씩 추출
    for index_inp in range (len(myList)) :
        inp = myList[index_inp]
    for index_ran in range (len(ransu)) :
        ran = ransu[index_ran]
        # < Strike >    
        # 2.1) 만약 "(난수)자릿수" and "난수 값" == "입력 값" 이면  -> Strike    
          # 2.1-1) 난수 값 = 입력 값
            if inp in ransu :    
                if ran == inp :
                    if index_inp == index_ran :
                        Strike += 1 
                if ran != inp :
                    if inp in ransu :        
                        if index_inp != index_ran :
                            Ball += 1
            if Strike>=1 or Ball>=1:
                continue
    if Strike == 0 and Ball == 0 :
        Out += 1