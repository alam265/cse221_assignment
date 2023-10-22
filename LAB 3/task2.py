def merge(a, b):
    if a > b:
        return a 
    return b

   
     

def mergeSort(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  
        a2 = mergeSort(arr[mid:])  
        return merge(a1, a2)     
    


print(mergeSort([1, 7, 13, 4, 5, 7, 13, 12]))