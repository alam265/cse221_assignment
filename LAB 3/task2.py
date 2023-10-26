data = open('input2.txt','r')
result = open('output2.txt','w')

length = int(data.readline())

arrStr = data.readline().split(' ')
arr = [int(n) for n in arrStr]



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
    


result.write(f"{mergeSort(arr)}")

# Time Complexity: nlog2(n)

'''
Explanation:
Here we just modified the Merge Sort algorithm. Instead of Sorting and merging back the the subarrays here we returned the bigger element.
'''