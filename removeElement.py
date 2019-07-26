# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums, val):
        nums = [3,2,2,3,5]
        val = 3        
        
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        # remove안하는 개수가 i
        # nums[i] = nums[j] 과정을 거친 후 i를 1 더해주기 때문에, 결과적으로 i의 위치는 replace 되어야 할 위치를 가르친 채 loop가 종료되는 것
        # 그래서 가장 마지막으로 replace된 위치에서 +1 상태이기 때문에, 자연스럽게 새로운 nums의 크기와 일치하게 됨.
        return i
