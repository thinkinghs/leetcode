# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        
        if not nums:
            return 0
        
        # best practice 보니 int의 lowest value를 넣을 필요 없이, largest에 nums[0] 값을 넣으면 됨
        # curr은 0부터 시작해야되니 curr=0
        # nums = [-2] 일 경우에 -2 return 해야 되고, nums[-2, -1] 일때 -1 return 해야 됨
        
        # largest = -2^31 
        # curr = 0
        largest = nums[0]
        curr = 0
        
        # curr 
        for i in nums:
            curr += i
            if curr > largest:
                largest = curr
            if curr < 0:
                curr = 0
            
        return largest
            
''' The solution that someone got many stars
def maxSubArray(self, A):
    if not A:
        return 0
    
    curSum = maxSum = A[0]
    # 
    for num in A[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)
    return maxSum

'''
