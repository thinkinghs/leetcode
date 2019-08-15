# https://leetcode.com/problems/3sum-closest/
# 결국 못 풀고 다른 사람 solution code 본 후, 내가 이해한대로 직접 작성함
# https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        # index를 return 하는게 아니니 sort시켜도 됨
        # sort 시키면 숫자 크기가 큰지 작은지에 따라 index pointer를 움직여서 수치를 조절 가능해짐
        # 위와 같은 technic을 이용할 때 sort 시키면 좋음
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        
        # O(n^2)
        for i in range(len(nums)-2):
            # left와 right pointer를 지정해서 for loop으로 0 ~ n-2까지 진행되는 O(n) 동안 left와 right 조정하면서 threeSum값 유추 
            left, right = i+1, len(nums)-1
            
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                
                if threeSum == target:
                    return threeSum
                
                # 새로 구한 threeSum 값이 기존 closest보다 target에 가까우면 closest 값 변경
                if abs(threeSum - target) < abs(closest - target):
                    closest = threeSum
                
                # nums array가 sort된 상태이므로 threeSum 값이 target보다 작으면 left를 오른쪽으로 옮겨서 값을 올림
                # threeSum값이 target보다 크면 threeSum 값을 target쪽으로 낮춰야하므로 right(큰 수)값을 내림
                # left와 right 값이 조정되다가 값이 겹치게 되면 while condition에 따라 loop 나가게 되고 for loop에 따라 i값을 1 올림
                if threeSum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest
        
