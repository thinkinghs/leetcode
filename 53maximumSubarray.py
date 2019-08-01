# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        
        if not nums:
            return 0
        
        largest = -2^31 
        curr = 0
        # curr 
        for i in nums:
            curr += i
            if curr > largest:
                largest = curr
            if curr < 0:
                curr = 0
            
        return largest
            
