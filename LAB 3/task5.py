data = open('input5.txt','r')
result = open('output5.txt','w')

length = int(data.readline())

arrStr = data.readline().split(' ')
arr = [int(n) for n in arrStr]

def partition(A, start ,end):
    pivot = A[end]
    i = start - 1 
    for j in range(start,end):
        if A[j] <= pivot:
            i+=1 
            A[i] , A[j] = A[j], A[i]
    A[i+1] , A[end] = A[end], A[i+1]
    return i+1 

def QuickSort(A, start, end):
    if start <end:
        pivot_idx = partition(A,start,end)
        QuickSort(A,start ,pivot_idx - 1)
        QuickSort(A,pivot_idx + 1,end)


arr = [5,6,4,2,5,7,42,23,0]
QuickSort(arr,0,length)

for num in arr:
    result.write(f"{num} ")

result.close()

'''
Explanation:
Quick sort code is done by having one function for partition that selects the last element as pivot and then putting the pivot element in its right place. 
Quick sort function recursively calls partition function for the element from start till pivot index and after the pivot index till end.
'''