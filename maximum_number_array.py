def find_max(arr):
    #write your code here
    max_num=0
    for x in range(len(arr)): 
        if(arr[x]>max_num):
            max_num=arr[x]
    return max_num