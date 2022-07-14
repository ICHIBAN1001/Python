row = 5 # 층 변수 

count = 0

for value in range (2): 
# 층
    for floor in range (1,row+1) :
        # 별 원소
        for star in range(1,row+1) :
            # 별 뽑을 때 
            if value == 0 :
                if floor %2 != 0  or star %2 !=0 :
                    print("*",end="")
                # 아닐 때 
                else : 
                    print(" ",end="")
         
            else :       
                if floor!=star :
                    print("*",end="")
                else : 
                    print(" ",end="")
        print()  
    print()  
