def maximum(arr):
    big = arr[0]
    for num in arr:
        if big < num:
            big = num
    return big
    
nums = [8,9,10,1,5,4,2,1] 
print(maximum(nums))