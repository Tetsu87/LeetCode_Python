from bisect import bisect, bisect_left, bisect_right

def searchRange(nums,target):
    def bs_left(nums,target):
        left,right = 0, len(nums)-1
        
        while left <=right:
            mid = left + (right-left)//2
            
            if nums[mid] >= target:
                right = mid -1
            else:
                left = mid +1
            
        return left
        
    def bs_right(nums,target):
        left,right = 0, len(nums)-1
        
        while left <=right:
            mid = left + (right-left)//2
            
            if nums[mid] > target:
                right = mid -1
            else:
                left = mid +1
            
        return left
        
    start,end = bs_left(nums,target), bs_right(nums,target)
    
    if not nums:
        return [-1,-1]
    
    # check if nums[start] == target
    if start == len(nums) or nums[start] != target:
        return [-1,-1]
        
    return [start,end-1]

print(searchRange([5,7,7,8,8,10],8))
print(searchRange([2,2],3))