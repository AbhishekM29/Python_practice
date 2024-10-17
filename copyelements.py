list = [1, -1, 1, 2, 3, 3, 3, 4, 4, 4, 5]
result = {}

for i in list:
    if i in result:
        result[i] += 1  # result=reuslt+1

    else:
        result[i] = 1

print(result)
