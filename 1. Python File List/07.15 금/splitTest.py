
msg = "h   king  car a       ab  fmlkgj  "

list = []
word = ""

count = 0
for value in msg:
    if value.isalpha():
        word += value
        
        if count == len(msg) - 1:
            list.append(word)
            word = ""
    else:
        if len(word) >= 1:
            list.append(word)
        
        word = ""

    count += 1

print(list)
