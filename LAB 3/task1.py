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
        a1 = mergeSort(arr[:mid])  # write the parameter 
        a2 = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2)     
    


print(mergeSort([9 ,5 ,4, 6 ,1 ,3 ,2, 9]))