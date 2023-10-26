data = open('input6.txt','r')
result = open('output6.txt','w')

length = int(data.readline())

arrStr = data.readline().split(' ')
arr = [int(n) for n in arrStr]

no_of_queries = int(data.readline())

queries = []
for i in range(no_of_queries):
    queries.append(int(data.readline()))



def partition(A, start ,end):
    pivot = A[end]
    i = start - 1 
    for j in range(start,end):
        if A[j] <= pivot:
            i+=1 
            A[i] , A[j] = A[j], A[i]
    A[i+1] , A[end] = A[end], A[i+1]
    return i+1 


def Kth_smallest(arr,k):
    start = 0
    end = len(arr)-1

    while start <= end:
        pivot_idx = partition(arr, start, end)
        if pivot_idx == k-1:
            return arr[pivot_idx]
        elif pivot_idx > k-1:
            end = pivot_idx - 1 
        else:
            start = pivot_idx + 1 


for q in queries:
    result.write(f"{Kth_smallest(arr,q)}\n")

'''
Explanation:
For this problem partition function is kept the same in another function if k-1 as same as pivot index then return the element. 
Otherwise check two conditions. If pivot index is greater than k-1 then decrease end index by one and call partition function. 
Otherwise set start as pivot index + 1 and call partition function.
'''