data = open('input4.txt','r')
result = open('output4.txt','w')

length = int(data.readline())

arrStr = data.readline().split(' ')
arr = [int(n) for n in arrStr]

def get_max(arr):
    if len(arr) == 2:
        return arr[0] + (arr[1])**2 
    elif len(arr) == 1:
        return float('-inf')

    left_val = get_max(arr[0:len(arr)//2])
    right_val = get_max(arr[len(arr)//2:])

    left_arr = arr[0:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    left_max = max(left_arr)
    for i in range(len(right_arr)):
        right_arr[i] = right_arr[i]**2  
    right_max = max(right_arr)
    cross_max = left_max + right_max 
    return max(left_val,right_val,cross_max)

result.write(f"{get_max(arr)}")

result.close()


"""Explanation:
This problem is solved with divide and conquer. First dividing the array recursively in to left and right sub array. 
Then we find the maximum element with the condition possible for both sub array. Also, we checked if any maximum element is possible from the crossed element from both array. 
This is done by adding the maximum element of left sub array and maximum squared value of right sub array and finally returning the maximum value among those three values.
"""