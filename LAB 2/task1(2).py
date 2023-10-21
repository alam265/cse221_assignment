data = open('input1(2).txt','r')
result = open('output1(2).txt','a')

size,target =data.readline().split(' ')
size = int(size)
target = int(target)

arr_str = data.readline().split(' ')
arr = [int(num) for num in arr_str]
p1 = 0 
p2 = size-1 

while p1 < p2 :
    sum = arr[p1] + arr[p2]
    if sum == target:
        result.write(f"{p1+1} {p2+1}")
        break
    elif sum < target:
        p1+=1
    else:
        p2-=1 
result.write(f"IMPOSSIBLE")

result.close()



    

