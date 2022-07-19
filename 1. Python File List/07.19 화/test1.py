import random

MyList = []

duplicate = 0 

# while 로 같은거 안들어 오게 계속 무한 반복 
while  len(MyList)< 25 :    # 0 ~24 개
    Element = random.randint(1,50) 
    # 안에 안들어 있으면 넣기     
    if not Element in MyList :
        MyList.append(Element)

print(MyList)  
newlist = []
for index in range (1,50+1) :
    if index in MyList  :
        newlist.append(index)
      
print(newlist)