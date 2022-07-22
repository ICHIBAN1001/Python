randNumList = [21, 14, 11, 3, 16, 48, 31, 41, 47, 30, 5, 28, 17, 22, 8, 38, 34, 23, 20, 49, 32, 25, 37, 2, 43]

N = 5
NUM_OF_ELEMENTS = N * N
RAND_NUM_FROM = 1
RAND_NUM_TO = 50

for index in range(NUM_OF_ELEMENTS):
    print(randNumList[index], "\t", end="")
    
    if (index + 1) % 5 == 0:
        print()