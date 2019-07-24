
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        nums = []
        
        # nums가 비어있으면 바로 return. if nums가 아니라 if not nums임. 햇갈렸음.
        if not nums:
            return 0
            
        previous = nums[0]
        idx = 1
        while idx < len(nums):
            if previous == nums[idx]:
                nums.pop(idx)
            else:
                previous = nums[idx]
                idx += 1
            print(nums)
            
        return len(nums)

'''
# Java solution을 python 코드로 변경시킨 것
# process 중에 pop 시키는 작업 없이 중복되지 않은 값들로 nums의 앞에서부터 바꿈
# 중복되지 않은 숫자의 개수 i+1(i가 0부터 시작하니 length값은 1 더해줘야 함) 이용해서 slice 시켜주면 중복되지 않는 nums 구할 수 있음
# nums의 reference 값은 문제가 parameter 넘겨줄 때 가지고 있으므로, nums slice 시키는건 문제가 확인해서 채점함
# 중간에 nums에서 pop 시키지 않아 nums의 length가 바뀌지 않으니 nums의 length 이용해서 for문 돌릴 수 있음
class Solution:
    def removeDuplicates(self, nums):
        
        if not nums:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1
'''
