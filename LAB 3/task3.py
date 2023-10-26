data = open('input3.txt','r')
result = open('output3.txt','w')

length = int(data.readline())

arrStr = data.readline().split(' ')
arr = [int(n) for n in arrStr]


def merge(a, b):
    global count
    i = j = 0 
    res =[]

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i+=1 
        else:
            res.append(b[j])
            count+= len(a) - i
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
    

count=0
mergeSort(arr)
result.write(f"{count}")


""""
Explanation:
Here we add a condition and global count variable for this task. To elaborate, Whenerver a value of right array 
is greater than a value of left sub array we are counting for that right sub array's element and also for the rest.
because the array is sorted. 
"""