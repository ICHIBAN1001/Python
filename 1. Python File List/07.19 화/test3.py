mylist = [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 20, 24, 26, 27, 28, 29, 34, 36, 37, 41, 45, 49, 50]

sortinglist = [[],[],[],[],[] ]  # 5개 칸

# 전체 카운트
count = 0

# 솔팅 카운트
sorting_count = 0

# 리스트 안에 리스트가 5개 까지 반복
while count < len(mylist) :
    # 요소 뽑기
    sortinglist[sorting_count].append(mylist[count])
    if len(sortinglist[sorting_count]) == 5 :
        sorting_count += 1
    count += 1
print(sortinglist)
