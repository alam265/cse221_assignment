data = open('input2_(2).txt','r')
result = open('output2_(2).txt','a')

size1 = int(data.readline())
arr1_str = data.readline().split(' ')

size2 = int(data.readline())
arr2_str = data.readline().split(' ')



arr1 = [int(num) for num in arr1_str]
arr2 = [int(num) for num in arr2_str]




def merge(arr1,arr2):
    p1 = p2 = 0 
    res =[]
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            res.append(arr1[p1])
            p1+=1

        else:
            res.append(arr2[p2])
            p2+=1 
    while p1 < len(arr1):
        res.append(arr1[p1])
        p1+=1
    while p2 < len(arr2):
        res.append(arr2[p2])
        p2+=1
    return res

merged_arr = merge(arr1,arr2)

for i in merged_arr:
    result.write(f"{i} ")

result.close()

