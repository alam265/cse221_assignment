data = open('LAB 2/input1(1).txt','r')
result = open('output1(1).txt','a')
first_line = data.readline().split(' ')

count = int(first_line[0])
target = int(first_line[1])


arr_str = data.readline().split(' ')

arr = [int(i) for i in arr_str]

flag = False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i] + arr[j]) == target:

            flag  = True

    if flag:
        break

if flag:
    result.write(f'{i+1} {j+1}')


if flag==False:
    result.write("IMPOSSIBLE")


result.close()


