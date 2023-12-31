data = open('input1.txt','r')
result = open('output1.txt','w')

length = int(data.readline())

arrStr = data.readline().split(' ')
arr = [int(n) for n in arrStr]



def merge(a, b):
    res = [] 

    i = j = 0 

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i+=1 
        else:
            res.append(b[j])
            j+=1 

    while i < len(a):
        res.append(a[i])
        i+=1 
    while j < len(b):
        res.append(b[j])
        j+=1 

    return res 

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])   
        a2 = mergeSort(arr[mid:])  
        return merge(a1, a2)     
    


Sorted_arr = mergeSort(arr)

for i in Sorted_arr:
    result.write(f"{i} ")

# Explanation:
# We just perform basic Merge Sort 